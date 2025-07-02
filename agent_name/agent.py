from google.adk.agents import LlmAgent

from agent_name.prompt import AGENT_PROMPT
from agent_name.tools import TOOLS
from agent_name.config import MODEL, AGENT_NAME

def create_agent() -> LlmAgent:
    """Constructs the ADK Agent."""
    return LlmAgent(
        model=MODEL,
        name=AGENT_NAME,
        instruction=AGENT_PROMPT,
        tools=TOOLS,
    )

root_agent = create_agent()