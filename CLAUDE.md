# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`chief-ai-system` is a local Python AI agent/orchestrator built on the Anthropic SDK. The user-facing surface is a small `Agent` class plus a CLI entry point; tools are plain Python functions decorated with `@beta_tool` from the SDK.

## Commands

```bash
# Install (uv preferred; pip works)
uv pip install -e ".[dev]"            # or: pip install -e ".[dev]"

# Set API key
cp .env.example .env && $EDITOR .env  # populate ANTHROPIC_API_KEY

# Run the CLI
chief-ai "list the files in the src directory and summarize what they do"
chief-ai                              # interactive mode
python -m chief_ai "..."              # same, without the console script

# Tests / lint
pytest                                # runs tests under tests/
pytest tests/test_agent.py::test_agent_defaults  # single test
ruff check .
ruff format .
```

## Architecture

The system has three layers:

1. **`Agent` (`src/chief_ai/agent.py`)** — wraps `client.beta.messages.tool_runner()`. The runner handles the entire tool-use loop: it calls the API, executes any tool calls Claude requests, feeds the results back, and iterates until Claude is done. The `Agent` instance keeps `self.history` across `.run()` calls, so a single Agent represents a multi-turn conversation. `agent.reset()` clears history.

2. **Tools (`src/chief_ai/tools.py`)** — plain Python functions decorated with `@beta_tool`. The decorator derives the JSON Schema from the function's type hints and parses the docstring's `Args:` block for parameter descriptions, so good signatures and docstrings matter more than they would in normal Python — the model only sees what those produce. Tools are passed to `Agent(tools=[...])`; `DEFAULT_TOOLS` ships with `read_file` and `list_dir`.

3. **CLI (`src/chief_ai/cli.py`)** — argparse front-end. Loads `.env`, constructs an `Agent`, and either runs a single prompt or drops into an interactive loop. The default system prompt lives here as `DEFAULT_SYSTEM`.

## Conventions

- **Model:** default is `claude-opus-4-7`. Use this exact string — never append a date suffix to an alias. To change models per-invocation, pass `--model` to the CLI or `model=` to `Agent(...)`. Adaptive thinking (`{"type": "adaptive"}`) is enabled in `Agent.run()`; this is the only on-mode for Opus 4.7 and won't work on pre-4.6 models — drop the `thinking` kwarg or switch to `{"type": "disabled"}` if downgrading.
- **System prompt caching:** `Agent.run()` sends `system` as a single block with `cache_control: ephemeral`. The cache only kicks in once the rendered prefix crosses ~4096 tokens on Opus 4.7; smaller prompts won't actually cache, but the marker is harmless. Verify with `response.usage.cache_read_input_tokens` if you instrument it.
- **Adding a tool:** write a function with full type hints and a docstring including an `Args:` section. Decorate with `@beta_tool` and append to `DEFAULT_TOOLS` (or pass directly to `Agent(tools=[...])`). The SDK generates the schema — don't write JSON Schema by hand.
- **Conversation state lives on the Agent.** The API itself is stateless; each `.run()` re-sends `self.history`. To start fresh, instantiate a new `Agent` or call `.reset()`.
- **Tool runner is beta** (`client.beta.messages.tool_runner`). If the SDK changes the namespace, the Agent class is the only place that needs to move.
