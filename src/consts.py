from itertools import product
from pathlib import Path

from src.enums import LangDirectory, LangFile


DATA_DIRECTORY = "data"

STEAM_DIRECTORY = "steamapps"

BACKUP_DIRECTORY = Path.home() / "sclegacylang" / "backup"


class GamePath:
    APPDATA = Path.home() / "AppData" / "Roaming"
    STALCRAFT = APPDATA / "EXBO" / "runtime" / "stalcraft"
    DEFAULT = STALCRAFT / "modassets" / "assets"


class RequiredPath:
    STEAM = Path("modassets/assets")
    LAUNCHER = Path("runtime/stalcraft/modassets/assets")


LANGS_FILES = [Path(directory.value, file.value) for directory, file in product(LangDirectory, LangFile)]
"""Все известные файлы локализации"""
