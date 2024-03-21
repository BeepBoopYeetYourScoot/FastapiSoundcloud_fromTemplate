import uvicorn
from fastapi import FastAPI, Response, status
from fastapi.websockets import WebSocket

from fastapi_controllers import Controller, get, websocket


class TrackSplitter(Controller):
    @get("/example", response_class=Response)
    async def example(self) -> Response:
        return Response("Successful response", status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    app = FastAPI()
    app.include_router(TrackSplitter.create_router())
    uvicorn.run(app)
