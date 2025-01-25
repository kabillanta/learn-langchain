from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key='AIzaSyA-WrW_nJnLdok50MkITXCdgmD7tcg78Pc')

messages = [
    ("system", "Give me the information in plain text without Markdown formatting . You are a {topic} expert"),
    ("human", "give me {count} best commercial aircraft")
]
prompt_template = ChatPromptTemplate.from_messages(messages)

upper_case = RunnableLambda(lambda x : x.upper())
count_words = RunnableLambda(lambda x : f'Word Count is {len(x.split())}\n{x} ')


chain = prompt_template | model | StrOutputParser() |upper_case| count_words

result = chain.invoke({"topic":'aircraft',"count":"3"})
print(result)