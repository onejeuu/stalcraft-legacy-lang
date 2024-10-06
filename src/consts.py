from pathlib import Path


class GamePath:
    APPDATA = Path.home() / "AppData" / "Roaming"
    STALCRAFT = APPDATA / "EXBO" / "runtime" / "stalcraft"
    ASSETS = STALCRAFT / "modassets" / "assets"


class PathRequired:
    LAUNCHER = Path("runtime/stalcraft/modassets/assets")
    STEAM = Path("modassets/assets")
