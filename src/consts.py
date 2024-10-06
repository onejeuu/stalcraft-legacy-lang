from pathlib import Path


class GamePath:
    APPDATA = Path.home() / "AppData" / "Roaming"
    STALCRAFT = APPDATA / "EXBO" / "runtime" / "stalcraft"
    ASSETS = STALCRAFT / "modassets" / "assets"

    # TODO: delete test value
    ASSETS = Path("G:/SCASSETS.LANG")


class RequiredPath:
    LAUNCHER = Path("runtime/stalcraft/modassets/assets")
    STEAM = Path("modassets/assets")


class LangPath:
    GLOOMY = Path("gloomycore/lang/ru.lang")
    STALKER = Path("stalker/lang/ru.lang")
