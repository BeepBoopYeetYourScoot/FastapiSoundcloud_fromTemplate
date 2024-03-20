import pathlib

INTEGRATIONS_DIR = pathlib.Path(__file__)

BASE_DIR = INTEGRATIONS_DIR.parent

SOUNDCLOUD_DIR = INTEGRATIONS_DIR / pathlib.Path("soundcloud")
TELEGRAM_DIR = INTEGRATIONS_DIR / pathlib.Path("telegram")
