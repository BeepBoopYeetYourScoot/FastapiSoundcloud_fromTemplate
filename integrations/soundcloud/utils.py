from integrations.conf import BASE_DIR


def get_track_filename(featured_track):
    return f"{BASE_DIR}/saved/{featured_track.artist} - {featured_track.title}.mp3"


def get_playlist_filename(featured_playlist):
    return f"./saved/{featured_playlist.artist} -" f" {featured_playlist.title}.mp3"
