import sclib
from sclib import SoundcloudAPI

# do not pass a Soundcloud client ID that did not come from this library, but you can save a client_id that this lib found and reuse it
# FIXME Definitely mock for new things
sc_client = SoundcloudAPI()
LINK = (
    "https://soundcloud.com/soft_blade/"
    "sets/softic?si=c849f884c0314b18945d7ada540c83ee&"
    "utm_source=clipboard&"
    "utm_medium=text&utm_campaign=social_sharing"
)
track = sc_client.resolve(LINK)


def save_track(featured_track: sclib.Track | sclib.Playlist):
    filename = f"./{featured_track.artist} - {featured_track.title}.mp3"

    assert type(featured_track) is sclib.Track

    with open(filename, "wb+") as file:
        featured_track.write_mp3_to(file)


if __name__ == "__main__":
    save_track(track)
