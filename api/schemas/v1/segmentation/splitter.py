from pydantic import BaseModel


class SplitterRequestData(BaseModel):
    track_uuid: str
    track_name: str
    download: bool
