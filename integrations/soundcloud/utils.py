from integrations.conf import SOUNDCLOUD_DIR, INTEGRATIONS_DIR, TRACK_SAVED_DIRECTORY

TRACK_FILETYPE = "mp3"
NAME_SEPARATOR = " - "


def get_track_filename(featured_track):
    return (
        f"{TRACK_SAVED_DIRECTORY}/{featured_track.artist}"
        f"{NAME_SEPARATOR}"
        f"{featured_track.title}"
        f".{TRACK_FILETYPE}"
    )


def get_playlist_filename(featured_playlist):
    return (
        f"{INTEGRATIONS_DIR}/saved/{featured_playlist.artist} "
        f"{NAME_SEPARATOR}"
        f"{featured_playlist.title}"
        f".{TRACK_FILETYPE}"
    )
