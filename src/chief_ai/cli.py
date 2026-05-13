import argparse
import sys
from typing import Any

from dotenv import load_dotenv

from chief_ai.agent import Agent
from chief_ai.tools import DEFAULT_TOOLS

DEFAULT_SYSTEM = """You are Chief, a local AI assistant with read-only filesystem access.
Use the available tools to investigate files and directories when the question calls for it.
Be concise and direct."""


def main(argv: list[str] | None = None) -> int:
    load_dotenv()
    parser = argparse.ArgumentParser(prog="chief-ai", description="Chat with the Chief agent.")
    parser.add_argument(
        "prompt",
        nargs="?",
        help="Single prompt to run. Omit for interactive mode.",
    )
    parser.add_argument("--model", default=None, help="Override the default model.")
    args = parser.parse_args(argv)

    kwargs: dict[str, Any] = {"system": DEFAULT_SYSTEM, "tools": DEFAULT_TOOLS}
    if args.model:
        kwargs["model"] = args.model
    agent = Agent(**kwargs)

    if args.prompt:
        print(agent.run(args.prompt))
        return 0

    print("Chief AI — interactive mode (Ctrl-D or empty line to exit)")
    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if not user:
            return 0
        print(agent.run(user))


if __name__ == "__main__":
    sys.exit(main())
