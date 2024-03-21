from pathlib import Path

from pydub import AudioSegment

from integrations.conf import TRACK_SAVED_DIRECTORY, TRACK_SAVED_SEGMENTED


def get_original_track_by_name(track_name: str) -> AudioSegment:
    track_path = TRACK_SAVED_DIRECTORY / Path(track_name)

    return AudioSegment.from_mp3(track_path)
