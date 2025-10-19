from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="FastAPI Backend Template")

# include routers
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to your FastAPI backend!"}
