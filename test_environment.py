import pytest
from unittest.mock import MagicMock
from environment import Environment  # Adjust if your path is different
from core.messaging import Role #seperating import role #adding import role

@pytest.fixture
def mock_agents():
    """Mock agent setup for different roles."""
    agent1 = MagicMock()
    agent1.role = Role.PI  # Set the role of agent1 to PI

    agent2 = MagicMock()
    agent2.role = Role.GEO_AGENT  # Set the role of agent2 to GEO_AGENT

    return [agent1, agent2]


@pytest.fixture
def mock_logger():
    return MagicMock()


@pytest.fixture
def mock_env(mock_agents, mock_logger):
    return Environment(agents=mock_agents, logger=mock_logger)


def test_environment_initialization(mock_env, mock_agents, mock_logger):
    """Tests that the Environment initializes correctly."""
    assert mock_env.logger == mock_logger

    expected_agents = {agent.role: agent for agent in mock_agents}
    assert mock_env.agents == expected_agents


@pytest.mark.asyncio
async def test_environment_run(mock_env):
    """Tests that the Environment runs without exceptions."""
    try:
        await mock_env.run([], "dummy_input", "dummy_output", "v1", "dummy_task_info.json")
    except Exception as e:
        pytest.fail(f"Environment run failed: {e}")
