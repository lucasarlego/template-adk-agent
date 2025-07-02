# LLM Model
MODEL="gemini-2.5-flash-preview-04-17" # Example

# Agent Name
AGENT_NAME="movie_cast_agent"

# Agent Skill Variables
AGENT_SKILL_ID="search_movie_cast"
AGENT_SKILL_NAME="Search Movie Cast"
AGENT_SKILL_DESCRIPTION="Uses Google Search to find the cast of a given movie."
AGENT_SKILL_TAGS=["movies", "cast", "search"]
AGENT_SKILL_EXAMPLES=["Who is in the cast of Interstellar?", "List the actors in Star Wars."]

# Agent Card Variables
AGENT_CARD_NAME="Movie Cast Finder Agent"
AGENT_CARD_DESCRIPTION="An agent that finds and lists the castof movies using Google Search."
AGENT_CARD_VERSION="1.0.0"
AGENT_INPUT_MODES=["text/plain"]
AGENT_OUTPUT_MODES=["text/plain"]