from pathlib import Path

import loguru


TRACK_FILETYPE = "mp3"
NAME_SEPARATOR = " - "

INTEGRATIONS_DIR = Path(__file__).parent
BASE_DIR = INTEGRATIONS_DIR.parent
SOUNDCLOUD_DIR = INTEGRATIONS_DIR / Path("soundcloud")
TELEGRAM_DIR = INTEGRATIONS_DIR / Path("telegram")


TRACK_SAVED_DIRECTORY = SOUNDCLOUD_DIR / Path("saving") / Path("saved") / Path("tracks")
TRACK_SAVED_ORIGINAL = TRACK_SAVED_DIRECTORY / Path("original")
TRACK_SAVED_SEGMENTED = TRACK_SAVED_DIRECTORY / Path("segmented") / Path("storage")

PLAYLIST_SAVED_DIRECTORY = (
    SOUNDCLOUD_DIR / Path("saving") / Path("saved") / Path("playlists")
)


if __name__ == "__main__":
    # TODO check loguru message styling
    loguru.logger.info(
        {
            "INTEGRATIONS_DIR": INTEGRATIONS_DIR,
            "BASE_DIR": BASE_DIR,
            "SOUNDCLOUD_DIR": SOUNDCLOUD_DIR,
            "TELEGRAM_DIR": TELEGRAM_DIR,
            "TRACK_SAVED_DIRECTORY": TRACK_SAVED_DIRECTORY,
            "PLAYLIST_SAVED_DIRECTORY": PLAYLIST_SAVED_DIRECTORY,
        }
    )
