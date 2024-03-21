from pathlib import Path

from integrations.conf import TRACK_SAVED_SEGMENTED


def build_segmented_track_path(track_name: str):
    return TRACK_SAVED_SEGMENTED / Path(track_name)
