from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel
from typing import Annotated

Zoona = FastAPI()
templates = Jinja2Templates(directory="templates")
class Product(BaseModel):
    title: str
    description: str
    price: float

# def create-product (product:Product):

@Zoona.get("/create-product")
def productpage(request:Request):
    return templates.TemplateResponse(request=request, name="createproduct.html", context={})

@Zoona.post("/create-product")
def productpage(request:Request, product:Annotated[Product, Form()]):
    print(product)
    return templates.TemplateResponse(request=request, name="createproduct.html", context={})


