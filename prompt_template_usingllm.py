from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key='AIzaSyA-WrW_nJnLdok50MkITXCdgmD7tcg78Pc')

messages = [
    ("system", "Give me the information in plain text without Markdown formatting . You are a {topic} expert"),
    ("human", "give me {count} best commercial aircraft")
]
prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({"topic":'aircraft',"count":"3"})
print(prompt)

result = model.invoke(prompt)
print(result.content)
