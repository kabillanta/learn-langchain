import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.tools import Tool
import streamlit as st 

def main():
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key="AIzaSyA-WrW_nJnLdok50MkITXCdgmD7tcg78Pc")
    search = DuckDuckGoSearchRun()
    search_tool = Tool(name="DuckDuckGo", func=search.run, description="Search the web for information.")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )

    st.title("Gemini AI Agent")
    st.write("Ask me anything!")

    user_input = st.text_input("You: ")
    if user_input:
        response = agent.run(user_input)
        st.write("Agent:", response)


if __name__ == "__main__":
    main()
