import json
from pathlib import Path

import pydub
from pydub import AudioSegment

from integrations.conf import TRACK_SAVED_DIRECTORY, build_segmented_track_path
from integrations.soundcloud.saving.saved.tracks.segmented.scripts.getters import (
    get_original_track_by_name,
)

TRACK_NAME = "soft blade - Ksv.mp3"

track = get_original_track_by_name(TRACK_NAME)


def split_in_half(track_name): ...


def cut_by_start_and_end(): ...


def save_changed_track(changed_track: pydub.AudioSegment):
    track.export(build_segmented_track_path(TRACK_NAME))


if __name__ == "__main__":
    print(track.__repr__())
