from pathlib import Path

from src import ask, localization, utils
from src.consts import GamePath
from src.enums import LangPath, ModOption


def define_path():
    if GamePath.ASSETS.exists():
        if ask.confirm_default_path():
            return GamePath.ASSETS

    return ask.enter_assets_path()


def apply(original: Path, options: list[ModOption], lang: LangPath):
    mods = utils.options_to_path(options, lang)

    updated = localization.apply(path=original, mods=mods)

    localization.save(original, updated)


def install():
    assets = define_path()

    options = ask.mod_options()

    for lang in LangPath:
        original = assets / lang.value
        localization.backup(original)
        apply(original, options, lang)


def main():
    try:
        install()

    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
