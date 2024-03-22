from typing import Tuple

import pydub

from integrations.conf import TRACK_FILETYPE
from integrations.soundcloud.segmentation.scripts.builders import (
    build_segmented_track_path,
)
from integrations.soundcloud.segmentation.scripts.getters import (
    get_original_track_by_name,
)

TRACK_NAME = "soft blade - Ksv.mp3"

track = get_original_track_by_name(TRACK_NAME)


def split_track_in_two_halves(
    track: pydub.AudioSegment,
) -> Tuple[pydub.AudioSegment, pydub.AudioSegment]:
    halving_point = len(track) / 2
    first_half = track[:halving_point]
    second_half = track[halving_point:]
    return first_half, second_half


def cut_by_start_and_end(
    track: pydub.AudioSegment, start_ms=0, end_ms=None
) -> pydub.AudioSegment:
    # FIXME unfinished endpoint
    starting_track_point = track[start_ms:]
    ending_track_point = track[:end_ms] if end_ms else ...
    return track


def save_changed_track(changed_track: pydub.AudioSegment):
    changed_track.export(build_segmented_track_path(TRACK_NAME), format=TRACK_FILETYPE)


if __name__ == "__main__":
    print(track.__repr__())
