from pathlib import Path


BACKUP_SUFFIX = "bck"

DATA = Path("data")


class GamePath:
    APPDATA = Path.home() / "AppData" / "Roaming"
    STALCRAFT = APPDATA / "EXBO" / "runtime" / "stalcraft"
    ASSETS = STALCRAFT / "modassets" / "assets"

    # TODO: delete test value
    ASSETS = Path("G:/SCASSETS.LANG")


class RequiredPath:
    LAUNCHER = Path("runtime/stalcraft/modassets/assets")
    STEAM = Path("modassets/assets")
