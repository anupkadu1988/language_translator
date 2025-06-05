import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

## Build a model
groq_api_key=os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"]=groq_api_key
groq_model=ChatGroq(model="llama-3.3-70b-versatile")

## Prompt
gen_message="Translate given input in language {language}"
prompt=ChatPromptTemplate.from_messages(
    [("system", gen_message), ("user", "{query}")]
)

## parser
parser=StrOutputParser()

## chain
chain=prompt|groq_model|parser

st.title("language translator")

target_language=st.text_input("Mention your target language here")
query=st.text_input("Mention query to translate here")

if st.button('translate'):
    response=chain.invoke({"language":target_language,"query":query})
    st.write(response)

