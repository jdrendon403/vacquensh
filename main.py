from fastapi import FastAPI, Body, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Any, Coroutine, Optional, List

from starlette.requests import Request
from jwt_manager import create_token, validate_token

from routers.recipes import recipes
from routers.batch import batchs
from routers.log import log

app = FastAPI()
app.title = "Vacumm Furnace API"
app.version = "1.0"

app.include_router(recipes)
app.include_router(batchs)
app.include_router(log)

class JWTBearer(HTTPBearer):
   async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="No valid credentials")


class User(BaseModel):
    email: str
    password: str



# @app.post("/login", tags=["auth"])
# def login(user: User = Body()):
#     token = create_token(user.model_dump())
#     return JSONResponse(content=token, status_code=200)

# @app.get("/message/", tags=["home"], dependencies=[Depends(JWTBearer)])
# def message():
#     return "hello word"