from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Home Page Data" : "Welcome to Home Page of the Web App"}