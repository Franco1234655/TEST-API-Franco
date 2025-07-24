from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur mon API FastAPI"}

@app.get("/hello/{name}")
def greet_user(name: str):
    return {"message": f"Bonjour {name}, bienvenue sur FastAPI !"}