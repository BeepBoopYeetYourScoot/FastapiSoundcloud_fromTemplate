from abc import ABC

import sclib
from sclib import Track

from integrations.soundcloud.segmentation.scripts.builders import build_full_track_name


class AbstractSoundcloudTrack(ABC):
    uuid = None
    track_name = None
    __sc_track_obj = None

    def get_full_name(self):
        pass

    def connect_to_soundcloud_track(self, track: Track):
        pass

    def clean_soundcloud_track(self):
        pass


class SoundcloudTrack(AbstractSoundcloudTrack):

    def __init__(self, uuid, track_name, sc_track_obj=None):
        self.uuid = uuid
        self.track_name = track_name
        self.__sc_track_obj = None

    def get_full_name(self):
        return build_full_track_name(self.uuid, self.track_name)

    def connect_to_soundcloud_track(self, track: sclib.Track):
        assert isinstance(track, Track), "Incorrect type"
        self.__sc_track_obj = track

    def clean_soundcloud_track(self):
        assert self.__sc_track_obj is not None, "Nothing to clear"

    @property
    def soundcloud_track(self):
        return self.__sc_track_obj


if __name__ == "__main__":
    ...
