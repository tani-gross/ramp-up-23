from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Default (No Name)" }

@app.get("/{name}")
async def return_name(name):
    return {"message": "Hello, " + name}