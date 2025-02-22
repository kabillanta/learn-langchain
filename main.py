from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

web_agent = Agent(
    name="Web Agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)
web_agent.print_response("Tell me about OpenAI Sora?", stream=True)