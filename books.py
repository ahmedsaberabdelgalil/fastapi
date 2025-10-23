from fastapi import Body, FastAPI 

app = FastAPI() 


BOOKS = [
    {'title' : 'Title One' , 'author':'Author One' , 'category' : 'Science'},
    {'title' : 'Title Two' , 'author':'Author Two' , 'category' : 'Science'},
    {'title' : 'Title Three' , 'author':'Author Three' , 'category' : 'History'},
    {'title' : 'Title Four' , 'author':'Author Four' , 'category' : 'Math'},
    {'title' : 'Title Five' , 'author':'Author Five' , 'category' : 'Math'},
    {'title' : 'Title Six' , 'author':'Author Two' , 'category' : 'Math'}
    
]

@app.get(f"/books")
async def read_all_books():
    return BOOKS 


#Order matters here!  

# Should use the static first and then dynamic cuz it's order matters

#Path parameters 

@app.get(f"/books/mybook")
async def read_all_books():
    return{"books_title" : "My favorite book!" }


@app.get("/books/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

#Querey parameters
# away to filter data based on url provided -> Querey parameters 
@app.get("/books/")
async def read_category_by_query(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/{category}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold()\
            and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return 



#post request method used to create data 
# have a body that "get" does not have 

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book) 
    
    
#Put request method used to update data
#Put can have a body that has additional information like Post that Get does not have 

@app.put('/books/update_book')
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book
    

# DELETE request Method used to delete data  

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break



'''
Get all the books from any author 
'''
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return










#todo: add two mroe apis:
