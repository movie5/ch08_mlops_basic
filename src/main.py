# pip install uvicorn
# pip install "fastapi[all]"
# uvicorn src.main:app

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI - Hello World code",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
)

#unit test for python -m 

@app.get("/")
def hello_world():
    return {"Hello": "World"}
