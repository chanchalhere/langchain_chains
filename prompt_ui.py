from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
load_dotenv()


llm=HuggingFaceEndpoint(repo_id="HuggingFaceH4/zephyr-7b-beta",
task="text-generation")
st.header('Research tool')

paper_input=st.selectbox("select research paper name",["attention is all you need","BERT:pre-training of deep bidirectional transformers"])

style_input=st.selectbox("select explanation style",["beginner-friendly","technical","code-oriented","mathematical"])

length_input=st.selectbox("select explation length",["short(1-2 paragraph)","medium(3-5 paragraphs)"])


template=load_prompt('template.json')


research=ChatHuggingFace(llm=llm)

if st.button("summarize"):
    chain=template|research
    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})
    
    st.write(result.content)
   