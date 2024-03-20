import sclib
from sclib import SoundcloudAPI

from integrations.soundcloud.utils import get_track_filename

# do not pass a Soundcloud client ID that did not come from this library,
# but you can save a client_id that this lib found and reuse it

sc_client = SoundcloudAPI()
TRACK_LINK = (
    "https://soundcloud.com/soft_blade/ksv?"
    "in=soft_blade/sets/softic&"
    "si=0f2ae64eb26f439984d58ad153c7113a&"
    "utm_source=clipboard&"
    "utm_medium=text&utm_campaign=social_sharing"
)
track = sc_client.resolve(TRACK_LINK)


def save_track(featured_track: sclib.Track):
    filename = get_track_filename(featured_track)

    assert type(featured_track) is sclib.Track

    with open(filename, "wb+") as file:
        featured_track.write_mp3_to(file)


if __name__ == "__main__":
    save_track(track)
