import sclib
from sclib import SoundcloudAPI

from integrations.soundcloud.utils import get_playlist_filename

# do not pass a Soundcloud client ID that did not come from this library, but you can save a client_id that this lib found and reuse it
# FIXME Definitely mock for new things
sc_client = SoundcloudAPI()
PLAYLIST_LINK = (
    "https://soundcloud.com/soft_blade/"
    "sets/softic?si=c849f884c0314b18945d7ada540c83ee&"
    "utm_source=clipboard&"
    "utm_medium=text&utm_campaign=social_sharing"
)
playlist = sc_client.resolve(PLAYLIST_LINK)


def save_playlist(featured_playlist: sclib.Track):
    filename = get_playlist_filename(featured_playlist)
    assert type(featured_playlist) is sclib.Playlist

    with open(filename, "wb+") as file:
        featured_playlist.write_mp3_to(file)


if __name__ == "__main__":
    save_playlist(playlist)
