from langchain_community.vectorstores import FAISS
from load_and_split_pdf import split_pdf
from ollamaa import initialize_ollama_model


def create_db():
    Ollama_model, OllamaEmbedding = initialize_ollama_model()
    splitted_documents = split_pdf()
    db = FAISS.from_documents(documents=splitted_documents, embedding=OllamaEmbedding)
    print("db created")
    retriever = db.as_retriever(search_type="similarity",search_kwargs={"k":3})

    return db, retriever



"""
import faiss

# CUDA'nın kullanılabilirliğini kontrol etme
gpu_count = faiss.get_num_gpus()
if gpu_count > 0:
    print(f"CUDA destekli GPU sayısı: {gpu_count}")
else:
    print("CUDA kullanılabilir değil, CPU üzerinde çalışıyor.")

"""


