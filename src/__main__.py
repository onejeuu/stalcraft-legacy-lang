import os
from pathlib import Path

from src import ask, localization, resources
from src.consts import GamePath
from src.enums import LangPath, ModOption


def define_path():
    if GamePath.DEFAULT.exists():
        if ask.confirm_default_path():
            return GamePath.DEFAULT

    return ask.enter_assets_path()


def mod_is_installed(assets: Path):
    return any([localization.backup_name(assets / lang.value).exists() for lang in LangPath])


def apply(orig: Path, options: list[ModOption], lang: LangPath):
    mods = resources.options_to_path(options, lang)
    updated = localization.apply(path=orig, mods=mods)
    localization.save(orig, updated)


def install(assets: Path, options: list[ModOption]):
    for lang in LangPath:
        orig = assets / lang.value
        localization.backup(orig)
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


def change_encoding():
    os.system("chcp 65001 > NUL")


def cli():
    change_encoding()
    main()
    print("\nГотово")
    input("Нажмите Enter для закрытия...")


if __name__ == "__main__":
    try:
        cli()

    except (KeyboardInterrupt, SystemExit):
        pass
