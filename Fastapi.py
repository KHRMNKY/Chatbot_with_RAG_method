from fastapi import FastAPI
from chain import chainn
import uvicorn


app = FastAPI()

@app.get("")
def get_query():
    return "this is a RAG project"


@app.get("/response")
def get_query(query: str):

    result = chainn(query)
    
    return result




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)


