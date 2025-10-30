# The three biggest are:

# .dict() function is now renamed to .model_dump()

# schema_extra function within a Config class is now renamed to json_schema_extra

# Optional variables need a =None example: id: Optional[int] = None



from fastapi import FastAPI ,Body , Path , Query , HTTPException
from pydantic import BaseModel , Field 
from typing import Optional 
from starlette import status

app = FastAPI()

class Book:
    id:int
    title:str
    author :str
    description:str
    rating:int
    published_date:int

    def __init__(self,id,title,author , description,rating , published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date
        
        
class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create" , default=None)
    title:str = Field(min_length=3)
    author :str = Field(min_length=1)
    description:str = Field(min_length=1 , max_length= 100)
    rating:int = Field(ge=0, le=5) 
    published_date:int  
    
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
        rating=5,
        published_date= 2012
    ),
    Book(
        id=2,
        title="1984",
        author="George Orwell",
        description="A dystopian story about surveillance, totalitarianism, and the loss of individuality.",
        rating=5,
        published_date= 2011
    ),
    Book(
        id=3,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="A tragic tale of wealth, obsession, and the hollow pursuit of the American Dream.",
        rating=4,
        published_date= 2010
    ),
    Book(
        id=4,
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        description="A coming-of-age story following Holden Caulfield's cynical journey through New York City.",
        rating=4,
        published_date= 2009
    ),
    Book(
        id=5,
        title="Pride and Prejudice",
        author="Jane Austen",
        description="A witty exploration of class, marriage, and character in early 19th-century England.",
        rating=5,
        published_date= 2020
    ),
    Book(
        id=6,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        description="A fantasy adventure about Bilbo Baggins' journey from comfort to courage.",
        rating=5,
        published_date= 2012
    ),
    Book(
        id=7,
        title="The Alchemist",
        author="Paulo Coelho",
        description="A philosophical novel about following one's dreams and the search for personal legend.",
        rating=4 ,
        published_date= 2012
    ),
    Book(
        id=8,
        title="Brave New World",
        author="Aldous Huxley",
        description="A futuristic vision of a society obsessed with control, pleasure, and conformity.",
        rating=5 ,
        published_date= 2012
    ),
    Book(
        id=9,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        description="An epic saga of friendship, courage, and the battle against darkness in Middle-earth.",
        rating=5 ,
        published_date= 2012
    ),
    Book(
        id=10,
        title="Harry Potter and the Sorcerer's Stone",
        author="J.K. Rowling",
        description="The beginning of a magical journey as Harry discovers his identity as a wizard.",
        rating=5 
        ,published_date= 2025
    ),
]


@app.get("/books" , status_code= status.HTTP_200_OK)
async def read_all_books():
    return BOOKS 


# end point find a book based on id 

@app.get("/books/{book_id}" , status_code= status.HTTP_200_OK) 
async def read_book(book_id:int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book 
    raise HTTPException(status_code= 404 , detail="item not found ")
        
        
# end point based on rating 
@app.get("/books/by-rating/",status_code= status.HTTP_200_OK)
async def read_book_by_rating(book_rating:int = Query(gt=0 , lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return

# pydantics and data validation it's used for data validation 


@app.post("/create-book" , status_code= status.HTTP_201_CREATED)
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



# put request method 

@app.put("/books/update_book" , status_code= status.HTTP_204_NO_CONTENT)
async def update_book(book:BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book  
            book_changed = True
    if not book_changed:
         raise HTTPException(status_code= 404 , detail="NOT FOUND")
            
            
# Delete request method 

@app.delete("/books/{book_id}" , status_code= status.HTTP_204_NO_CONTENT) 
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    global BOOKS
    for i, book in enumerate(BOOKS):
        if book.id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
         raise HTTPException(status_code= 404 , detail="NOT FOUND")


# Assignment problem 

@app.get("/books/by-date/" , status_code= status.HTTP_200_OK)
async def get_book_by_date(publish_date:int = Query(gt = 1999 , lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == publish_date:
            books_to_return.append(book)
    return books_to_return
            



