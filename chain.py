from FAISS_db import *
from load_and_split_pdf import *

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
import os 
from langchain_groq import ChatGroq

def chainn(input):
    db, retriever = create_db()

    llm = ChatGroq(
        model="llama3-groq-70b-8192-tool-use-preview",
        api_key=os.environ.get("Grok_Api_Key"),
    )

    prompt = ChatPromptTemplate.from_template("""
            Answer the following question based only on the provided context. 
            Think step by step before providing a detailed answer. 
            I will tip you $1000 if the user finds the answer helpful. 
            <context>
            {context}
            </context>
            Question: {input}""")
    
    document_chain = create_stuff_documents_chain(llm, prompt)
    

    #relevant_docs = retriever.get_relevant_documents(input)
    #context = "\n".join([doc.page_content for doc in relevant_docs])
    
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": input})

    return response['answer']

print(chainn("what is Bovine Johne’s disease (BJD)"))