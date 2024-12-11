from dotenv import load_dotenv
import os
import re
from langchain_core.tools import tool
from datetime import datetime
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import streamlit as st




load_dotenv()

groq_api=os.getenv("Groq_Api")


llm=ChatGroq(api_key=groq_api,model="llama3-8b-8192")




@tool ("weather_details")
def weather_details(response):

    """This tool give you the details of the weather"""
    date=datetime.now().strftime("%Y-%m-%d")
    time=datetime.now().time()
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a very helpful assistant that can read the weather query and split that into the time-based instructions."),
            ("user", f"""
                I will give you today's date. If the response mentions a date for the next day, provide it. If the response mentions a date more than 4 days away, reply with "none". 
                Provide the output in the a accruate weather report kind of manner like a news reproter for the given question
                
               
                
                **response: {response}**
                **date:{date}**
                **time:{time}**
            """)
        ]
    )
    input_data={
        "response":response,
        "date":date,
        "time":time
    }
    chain =prompt|llm
    answer=chain.invoke(input_data)
    return answer.content








@tool ("Fact_search")
def Fact_search(response):
    """this gives you the right facts based on wiki search"""
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return wikipedia.run(response)



@tool ('General_topics')
def General_topics(response):
    """Use this tool if you think the topic is genral chit chat"""
    answer=llm.invoke(response)
    return answer.content



def Oracle(response):

    system_prompt = """You are the oracle, the great AI decision maker.
    Given the user's query, you must decide what to do with it based on the
    list of tools provided to you."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{input}")
    ])
    tools=[weather_details, Fact_search, General_topics]
    oracle=prompt | llm.bind_tools(tools=tools,tool_choice="auto")
    answer=oracle.invoke({"input":response})
    return answer.tool_calls[0]['name']


def final_llm(response):
    tools={'weather_details':weather_details,
           'Fact_search':Fact_search,
           'General_topics':General_topics}
    tool=Oracle(response)

    result=tools[tool].invoke(response)
    system_prompt = """So you basically reciving data from either weather details or Fact searcher or General Topics so based on your 
    undrestanding from the response the user and the answer you have to make a very good output for user """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", f" so this the response form the client{response} and this the result from the tools{result}",)
    ])
    oracle=prompt | llm
    answer=oracle.invoke({"response":result,'result':result})
    st.write( answer.content)



answer=st.write('hi hello this is your regular chatbot')
query=st.text_input('Enter your query')
final_llm(query)
