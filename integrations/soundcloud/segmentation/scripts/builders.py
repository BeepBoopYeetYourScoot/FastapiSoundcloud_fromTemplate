from pathlib import Path

from integrations.conf import TRACK_SAVED_SEGMENTED


def build_segmented_track_path(track_name: str):
    return TRACK_SAVED_SEGMENTED / Path(track_name)


def build_full_track_name(uu_id: str, name: str):
    return f"{uu_id}:{name}"
