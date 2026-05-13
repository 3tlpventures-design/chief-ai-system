from unittest.mock import MagicMock

from chief_ai.agent import DEFAULT_MODEL, Agent
from chief_ai.tools import DEFAULT_TOOLS, list_dir, read_file


def test_agent_defaults():
    agent = Agent(system="test", tools=DEFAULT_TOOLS, client=MagicMock())
    assert agent.model == DEFAULT_MODEL
    assert agent.history == []
    assert len(agent.tools) == 2


def test_agent_reset():
    agent = Agent(system="test", client=MagicMock())
    agent.history.append({"role": "user", "content": "hi"})
    agent.reset()
    assert agent.history == []


def test_default_tools_present():
    assert read_file in DEFAULT_TOOLS
    assert list_dir in DEFAULT_TOOLS
