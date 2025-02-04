from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda ,RunnableParallel

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp",api_key='AIzaSyA-WrW_nJnLdok50MkITXCdgmD7tcg78Pc')

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}."),
    ]
)

def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            ("human","Given these features: {features}, list the pros of these features.",)
        ]
    ) 
    return pros_template.format_prompt(features=features)

def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer. Be very concise ."),
            ("human","Given these features: {features}, list the cons of these features.",)
        ]
    ) 
    return cons_template.format_prompt(features=features)

def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"

pros_branch = (
    RunnableLambda(lambda x : analyze_pros(x)) | model | StrOutputParser() 
)
cons_branch = (RunnableLambda(lambda x : analyze_cons(x)) | model | StrOutputParser() 
)

chain = (
    prompt_template 
    | model 
    | StrOutputParser() 
    | RunnableParallel(branches={"pros":pros_branch,"cons":cons_branch}) 
    | RunnableLambda(lambda x: combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))
)

result = chain.invoke({"product_name":'Lenovo Legion Pro 5 16IRX9'})
print(result)