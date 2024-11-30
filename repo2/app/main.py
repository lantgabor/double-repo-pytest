from fastapi import FastAPI
from repo1.lib import hello

fastapi = FastAPI()


@fastapi.get("/")
async def root():
    return hello()
