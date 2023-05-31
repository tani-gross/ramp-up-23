from fastapi import FastAPI

name = input("What's your name? ")

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello, " + name}