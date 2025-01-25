from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

messages = [
    ("system", "you are a {topic} expert"),
    ("human", "give me {count} best planes")
]
prompt_template = ChatPromptTemplate.from_messages(messages)

prompt = prompt_template.invoke({"topic":'plane',"count":"3"})
print(prompt)

