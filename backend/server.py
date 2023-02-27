from fastapi import FastAPI

api = FastAPI()

@api.get('/')
async def home():
    return {"bioinformatics": "is awesome"}