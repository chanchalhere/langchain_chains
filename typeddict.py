from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()
llm=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct",task="text-generation")
model=ChatHuggingFace(llm=llm)

# structured output
class Review(TypedDict):
    summary:str
    sentiment:str
structured_model=model.with_structured_output(Review)
result=structured_model.invoke("""This phone is kind of good, battery is fine, latency is fine, display is cool, camera is not good""") 
print(result)


