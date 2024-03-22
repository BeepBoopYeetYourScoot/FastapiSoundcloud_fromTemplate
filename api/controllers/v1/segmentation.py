import uvicorn
from fastapi import FastAPI, Response, status
from fastapi_controllers import Controller, get

from api.schemas.v1.segmentation.splitter import SplitterRequestData
from integrations.soundcloud.segmentation.scripts.builders import build_full_track_name
from integrations.soundcloud.segmentation.scripts.getters import (
    get_original_track_by_name,
)
from integrations.soundcloud.segmentation.scripts.segment import (
    split_track_in_two_halves,
)


class TrackSplitter(Controller):
    prefix = "/splitter"
    tags = ["splitter"]

    @get("/example", response_class=Response)
    async def split_track_into_two_parts(self, data: SplitterRequestData) -> Response:
        full_track_name = build_full_track_name(data.track_uuid, data.track_name)
        track = get_original_track_by_name(full_track_name)
        first, second = split_track_in_two_halves(track)
        return Response([first, second], status_code=status.HTTP_200_OK)


if __name__ == "__main__":
    app = FastAPI()
    app.include_router(TrackSplitter.create_router())
    uvicorn.run(app)
