from fastapi import FastAPI
from pydantic import BaseModel
import redis

cache = redis.Redis(host="redis", port=6379, decode_responses=True)
app = FastAPI()

class DataModel(BaseModel):
    key: str
    value: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/data/{key}")
def read_data(key: str):
    value = cache.get(key)
    return {"key": key, "value": value}

@app.post("/data")
def write_data(data: DataModel):
    cache.set(data.key, data.value)
    return {"message": "saved", "data": data}