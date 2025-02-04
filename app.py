from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class IdeaRequest(BaseModel):
    idea: str

@app.post("/generate")
def generate_business(request: IdeaRequest):
    return {"business_name": f"{request.idea} Solutions"}

@app.get("/test")
def test():
    return "FastAPI is working!"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

