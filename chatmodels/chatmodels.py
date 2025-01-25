from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage,HumanMessage,AIMessage
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key='AIzaSyA-WrW_nJnLdok50MkITXCdgmD7tcg78Pc')

chat_history= []
sysmsg = SystemMessage(content='You are a helpful chatbot')
chat_history.append(sysmsg)

while True: 
    query = input("You: ")
    if query.lower() == 'exit': 
        break
    humanmsg = HumanMessage(content=query)
    chat_history.append(humanmsg)
    response = model.invoke(chat_history)  
    print("AI : " + response.content) 
    aimsg = AIMessage(content=response.content)  
    chat_history.append(aimsg)
