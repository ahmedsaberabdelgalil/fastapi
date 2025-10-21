from fastapi import FastAPI 

app = FastAPI() 


BOOKS = [
    {'title' : 'Title One' , 'author':'Author One' , 'category' : 'Scinence'},
    {'title' : 'Title Two' , 'author':'Author Two' , 'category' : 'Scinence'},
    {'title' : 'Title Three' , 'author':'Author Three' , 'category' : 'History'},
    {'title' : 'Title Four' , 'author':'Author Four' , 'category' : 'Math'},
    {'title' : 'Title Five' , 'author':'Author Five' , 'category' : 'Math'},
    {'title' : 'Title Six' , 'author':'Author Two' , 'category' : 'Math'}
    
]

@app.get("/books")
def read_all_books():
    return BOOKS