from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace 
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder

load_dotenv()
llm=HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct",task="text-generation")
chatmodel=ChatHuggingFace(llm=llm)
chat_history=[SystemMessage(content="you are helpful human assistant"),
              ]
while True:
    user_input=input('you: ')
    chat_history.append(HumanMessage(content=user_input))
    ChatPromptTemplate([
    ('system','you are helpful customer support chatbot')
    ('human','{query}')])
    prompt=chat_template.invoke({'query':'where is my order'})
    if (user_input=='exit'):
        break
   
    result=chatmodel.invoke(prompt)
    chat_history.append(AIMessage(content=result.content))
    print('AI:',result.content)
print(chat_history)




ChatPromptTemplate([
    ('system','you are helpful customer support chatbot')
    ('human','{query}')
])
prompt=chat_template.invoke({'query':'where is my order'})





