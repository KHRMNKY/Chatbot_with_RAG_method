from langchain_ollama import OllamaLLM, OllamaEmbeddings

def initialize_ollama_model():
    print("starting Ollama model...")  
    Ollama_model = OllamaLLM(model="gemma2")
    OllamaEmbedding = OllamaEmbeddings(model="gemma2")
    print("Ollama model loaded.") 

    return Ollama_model, OllamaEmbedding

