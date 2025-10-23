# The three biggest are:

# .dict() function is now renamed to .model_dump()

# schema_extra function within a Config class is now renamed to json_schema_extra

# Optional variables need a =None example: id: Optional[int] = None



from fastapi import FastAPI ,Body
from pydantic import BaseModel , Field 
from typing import Optional

app = FastAPI()

class Book:
    id:int
    title:str
    author :str
    description:str
    rating:int

    def __init__(self,id,title,author , description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create" , default=None)
    title:str = Field(min_length=3)
    author :str = Field(min_length=1)
    description:str = Field(min_length=1 , max_length= 100)
    rating:int = Field(ge=0, le=5) 
    
    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author":"anything",
                "description":"A new description of book",
                "rating":5
            }
        }
    }



BOOKS = [
    Book(
        id=1,
        title="To Kill a Mockingbird",
        author="Harper Lee",
        description="A classic novel exploring themes of racial injustice and moral growth in the American South.",
        rating=5
    ),
    Book(
        id=2,
        title="1984",
        author="George Orwell",
        description="A dystopian story about surveillance, totalitarianism, and the loss of individuality.",
        rating=5
    ),
    Book(
        id=3,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="A tragic tale of wealth, obsession, and the hollow pursuit of the American Dream.",
        rating=4
    ),
    Book(
        id=4,
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        description="A coming-of-age story following Holden Caulfield's cynical journey through New York City.",
        rating=4
    ),
    Book(
        id=5,
        title="Pride and Prejudice",
        author="Jane Austen",
        description="A witty exploration of class, marriage, and character in early 19th-century England.",
        rating=5
    ),
    Book(
        id=6,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        description="A fantasy adventure about Bilbo Baggins' journey from comfort to courage.",
        rating=5
    ),
    Book(
        id=7,
        title="The Alchemist",
        author="Paulo Coelho",
        description="A philosophical novel about following one's dreams and the search for personal legend.",
        rating=4
    ),
    Book(
        id=8,
        title="Brave New World",
        author="Aldous Huxley",
        description="A futuristic vision of a society obsessed with control, pleasure, and conformity.",
        rating=5
    ),
    Book(
        id=9,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        description="An epic saga of friendship, courage, and the battle against darkness in Middle-earth.",
        rating=5
    ),
    Book(
        id=10,
        title="Harry Potter and the Sorcerer's Stone",
        author="J.K. Rowling",
        description="The beginning of a magical journey as Harry discovers his identity as a wizard.",
        rating=5
    ),
]


@app.get("/books")
async def read_all_books():
    return BOOKS

# pydantics and data validation it's used for data validation 


@app.post("/create-book")
async def create_book(book_request:BookRequest):
    new_book = Book(**book_request.model_dump())
    print(type(new_book))
    BOOKS.append(find_book_id(new_book)) 
    
    
def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id = BOOKS[-1].id +1
    else:
        book.id = 1 
    return book 
    




