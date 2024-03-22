import abc
from abc import ABC
from typing import List

from integrations.soundcloud.soundcloudtrack import SoundcloudTrack


class MultipleTracksSegmentator(ABC):
    tracks: List[SoundcloudTrack] = []

    @abc.abstractmethod
    def perform(self):
        pass

    def add_track(self, track: SoundcloudTrack):
        pass

    def list_track_uuids(self):
        return [track.uuid for track in self.tracks]
