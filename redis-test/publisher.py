from fastapi import FastAPI
import aioredis

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"here"}

@app.post("/publish")
async def publish_message(message:str):
    redis = await aioredis.Redis.from_url("redis://localhost")
    await redis.publish("channel", message)
    redis.close()
    return {"message": "Published Successfully"}