from fastapi import FastAPI
from pydantic import BaseModel
import random

class Book(BaseModel):
    id:int = None
    title:str
    author:str
    year:int

books = []

app = FastAPI()

@app.post("/books/")
async def create_book(book: Book):
    book.id = random.randrange(10000)
    books.append(book)
    return {"Book Created": book}

@app.get("/books/")
async def get_books():
    return books

@app.get("/books/{id}")
async def get_book_with_id(id: int):
    for book in books:
        if book.id == id:
            return {"Book": book}
    return {"Message": "No book found for given id"}

@app.put("/books/{id}")
async def update_book(id: int, title: str, author: str, year: int):
    for book in books:
        if book.id == id:
            book.title = title
            book.author = author
            book.year = year
            return {"New Book": book}
    return {"Message": "No book found for given id"}

@app.delete("/books/{id}")
async def delete_book(id: int):
    for book in books:
        if book.id == id:
            books.remove(book)
    return {"Removed Book": book}