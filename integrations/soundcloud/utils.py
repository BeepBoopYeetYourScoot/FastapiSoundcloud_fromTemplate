from integrations.conf import (
    TRACK_SAVED_DIRECTORY,
    PLAYLIST_SAVED_DIRECTORY,
    NAME_SEPARATOR,
    TRACK_FILETYPE,
)


def get_track_file_path(featured_track):
    return (
        f"{TRACK_SAVED_DIRECTORY}/{featured_track.artist}"
        f"{NAME_SEPARATOR}"
        f"{featured_track.title}"
        f".{TRACK_FILETYPE}"
    )


def get_playlist_file_path(featured_playlist):
    return (
        f"{PLAYLIST_SAVED_DIRECTORY}/saved/{featured_playlist.artist} "
        f"{NAME_SEPARATOR}"
        f"{featured_playlist.title}"
        f".{TRACK_FILETYPE}"
    )
