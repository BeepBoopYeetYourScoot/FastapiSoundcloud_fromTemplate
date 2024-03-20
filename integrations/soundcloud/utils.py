from integrations.conf import BASE_DIR


TRACK_FILETYPE = "mp3"
NAME_SEPARATOR = " - "


def get_track_filename(featured_track):
    return (
        f"{BASE_DIR}/saved/{featured_track.artist}"
        f"{NAME_SEPARATOR}"
        f"{featured_track.title}"
        f".{TRACK_FILETYPE}"
    )


def get_playlist_filename(featured_playlist):
    return (
        f"{BASE_DIR}/saved/{featured_playlist.artist} "
        f"{NAME_SEPARATOR}"
        f"{featured_playlist.title}"
        f".{TRACK_FILETYPE}"
    )
