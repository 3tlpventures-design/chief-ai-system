from pathlib import Path

from anthropic import beta_tool


@beta_tool
def read_file(path: str) -> str:
    """Read a text file from the local filesystem.

    Args:
        path: Path to the file (absolute or relative to the current working directory).
    """
    return Path(path).expanduser().resolve().read_text(encoding="utf-8")


@beta_tool
def list_dir(path: str = ".") -> str:
    """List the contents of a directory.

    Args:
        path: Directory path (default: current working directory).
    """
    p = Path(path).expanduser().resolve()
    entries = sorted(p.iterdir(), key=lambda e: (not e.is_dir(), e.name.lower()))
    return "\n".join(f"{'d' if e.is_dir() else 'f'} {e.name}" for e in entries)


DEFAULT_TOOLS = [read_file, list_dir]
