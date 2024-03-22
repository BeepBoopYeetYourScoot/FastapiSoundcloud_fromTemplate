import abc
from abc import ABC

from pydub import AudioSegment

from integrations.soundcloud.soundcloudtrack import SoundcloudTrack


class SingleTrackSegmentator(ABC):
    track = None

    @abc.abstractmethod
    def perform(self):
        pass

    def add_track(self, track: SoundcloudTrack):
        self.track = track

    def clean_track(self):
        self.track = None


class TrackSplitter(SingleTrackSegmentator):
    pass


class TrackGluer(SingleTrackSegmentator):
    pass


class TrackSilencer(SingleTrackSegmentator):
    pass
