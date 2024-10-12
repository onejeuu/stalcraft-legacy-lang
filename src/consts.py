from pathlib import Path


DATADIR = "data"

BACKUP_SUFFIX = "bck"

LANG = "lang/ru.lang"


class GamePath:
    APPDATA = Path.home() / "AppData" / "Roaming"
    STALCRAFT = APPDATA / "EXBO" / "runtime" / "stalcraft"
    DEFAULT = ASSETS = STALCRAFT / "modassets" / "assets"


class RequiredPath:
    STEAM = Path("modassets/assets")
    LAUNCHER = Path("runtime/stalcraft/modassets/assets")
