from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda ,RunnableParallel , RunnableBranch
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key='AIzaSyA-WrW_nJnLdok50MkITXCdgmD7tcg78Pc')

positive_fb_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Helpful Assistant, Give feed back in single line be very consise."),
        ("human", "Write a return message for this positive feedback : {feedback}."),
    ]
)

negative_fb_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Helpful Assistant, Give feed back in single line be very consise"),
        ("human", "Write a thanking message for this negative  feedback : {feedback}."),
    ]
)
neutral_fb_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Helpful Assistant, Give feed back in single line be very consise"),
        ("human", "Write a return/thanking message for this nuetral feedback , try to get more comments: {feedback}."),
    ]
)
esclate_fb_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Helpful Assistant, Give feed back in single line be very consise"),
        ("human", "Generate a message to escalate this feedback to a human agent : {feedback}."),
    ]
)

classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helpful assistant"),
        ("human","Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}.")])

branches = RunnableBranch(
    (
        lambda x : "positive" in x , positive_fb_template | model | StrOutputParser()
    ),
    (
        lambda x : "negative" in x , negative_fb_template | model | StrOutputParser()
    ),
    (
        lambda x : "neutral" in x , neutral_fb_template | model | StrOutputParser()
    ),
    esclate_fb_template | model | StrOutputParser()
)

classification_chain = classification_template | model | StrOutputParser()     
chain = classification_chain | branches

result = chain.invoke({"feedback":'The product is terrible. It broke after just one use and the quality is very poor'})
print(result)