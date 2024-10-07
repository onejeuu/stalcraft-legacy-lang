from pathlib import Path


BACKUP_SUFFIX = "bck"

DATA = Path("data")


class GamePath:
    APPDATA = Path.home() / "AppData" / "Roaming"
    STALCRAFT = APPDATA / "EXBO" / "runtime" / "stalcraft"
    DEFAULT = ASSETS = STALCRAFT / "modassets" / "assets"


class RequiredPath:
    LAUNCHER = Path("runtime/stalcraft/modassets/assets")
    STEAM = Path("modassets/assets")
