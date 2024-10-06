from pathlib import Path

from src import ask, localization, utils
from src.consts import GamePath
from src.enums import LangPath, ModOption


def define_path():
    if GamePath.ASSETS.exists():
        if ask.confirm_default_path():
            return GamePath.ASSETS

    return ask.enter_assets_path()


def mod_is_installed(assets: Path):
    return any([localization.backup_name(assets / lang.value).exists() for lang in LangPath])


def apply(orig: Path, options: list[ModOption], lang: LangPath):
    mods = utils.options_to_path(options, lang)

    updated = localization.apply(path=orig, mods=mods)

    localization.save(orig, updated)


def install(assets: Path, options: list[ModOption]):
    for lang in LangPath:
        orig = assets / lang.value
        apply(orig, options, lang)


def uninstall(assets: Path):
    for lang in LangPath:
        orig = assets / lang.value
        bck = localization.backup_name(orig)
        localization.restore(orig, bck)


def main():
    assets = define_path()

    if mod_is_installed(assets) and ask.uninstall_mod():
        uninstall(assets)
        return

    options = ask.mod_options()

    install(assets, options)


if __name__ == "__main__":
    try:
        main()

    except (KeyboardInterrupt, SystemExit):
        pass
