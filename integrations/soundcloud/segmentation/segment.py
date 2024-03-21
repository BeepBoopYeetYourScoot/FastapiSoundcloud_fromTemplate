import pydub

from integrations.conf import TRACK_FILETYPE
from integrations.soundcloud.saving.saved.tracks.segmented.scripts.builders import (
    build_segmented_track_path,
)
from integrations.soundcloud.saving.saved.tracks.segmented.scripts.getters import (
    get_original_track_by_name,
)

TRACK_NAME = "soft blade - Ksv.mp3"

track = get_original_track_by_name(TRACK_NAME)


def split_in_half(track_name): ...


def cut_by_start_and_end(): ...


def save_changed_track(changed_track: pydub.AudioSegment):
    changed_track.export(build_segmented_track_path(TRACK_NAME), format=TRACK_FILETYPE)


if __name__ == "__main__":
    print(track.__repr__())
