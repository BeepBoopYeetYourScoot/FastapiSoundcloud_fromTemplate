from fastapi import FastAPI

app = FastAPI()


@app.get("/root")
def root():
    return {"message": "Hello World"}
