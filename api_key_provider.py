from fastapi import FastAPI, Body, HTTPException, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse, RedirectResponse
import uvicorn
from pydantic import BaseModel
from typing import Optional, Any
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv


load_dotenv('.env')


class ResponseModel(BaseModel):
    message: str = 'Success!'
    data: Optional[Any]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Configurar para permitir todas as origens
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# define a custom exception handler for Exception
@app.exception_handler(Exception)
async def unhandled_exception_handler(request, err):
    return JSONResponse(
        status_code=500, 
        content={
            "message": "Internal Server Error", 
            "data": None,
        })

# define a custom exception handler for StarletteHTTPException
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    if isinstance(exc.detail, BaseModel):
        exc.detail = exc.detail.dict()
    return JSONResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url='/docs')


@app.get("/OPENAI_API_KEY")
async def get_openai_api_key() -> ResponseModel:
    return ResponseModel(data={
        'OPENAI_API_KEY': os.environ['OPENAI_API_KEY']
    })

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=2334)
