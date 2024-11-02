from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf():
    loader = PyPDFLoader("./data/cattle-diseases-farmers-guide.pdf")
    docs = loader.load()
    return docs

def split_pdf():
    docs = load_pdf()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    splitted_documents = text_splitter.split_documents(docs)
    return splitted_documents


