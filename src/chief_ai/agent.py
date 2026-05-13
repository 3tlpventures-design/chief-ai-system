from collections.abc import Iterable
from typing import Any

import anthropic

DEFAULT_MODEL = "claude-opus-4-7"
DEFAULT_MAX_TOKENS = 16000


class Agent:
    def __init__(
        self,
        system: str,
        tools: Iterable[Any] = (),
        model: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        client: anthropic.Anthropic | None = None,
    ) -> None:
        self.client = client or anthropic.Anthropic()
        self.model = model
        self.max_tokens = max_tokens
        self.system = system
        self.tools = list(tools)
        self.history: list[dict[str, Any]] = []

    def run(self, user_message: str) -> str:
        self.history.append({"role": "user", "content": user_message})

        runner = self.client.beta.messages.tool_runner(
            model=self.model,
            max_tokens=self.max_tokens,
            system=[
                {
                    "type": "text",
                    "text": self.system,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            tools=self.tools,
            messages=self.history,
            thinking={"type": "adaptive"},
        )

        final_text: list[str] = []
        last_message = None
        for message in runner:
            last_message = message
            for block in message.content:
                if block.type == "text":
                    final_text.append(block.text)

        if last_message is not None:
            self.history.append({"role": "assistant", "content": last_message.content})

        return "\n".join(final_text)

    def reset(self) -> None:
        self.history.clear()
