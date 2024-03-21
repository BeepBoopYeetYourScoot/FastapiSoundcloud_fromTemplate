from fastapi import FastAPI

from api.controllers.v1.segmentation import TrackSplitter

app = FastAPI()


@app.get("/root")
def root():
    return {"message": "Hello World"}


app.include_router(TrackSplitter.create_router())
