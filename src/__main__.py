import os
from pathlib import Path

from src import ask, localization, resources
from src.consts import GamePath
from src.enums import LangPath, ModOption


def define_path():
    """Определить путь до ассетов игры"""
    if GamePath.DEFAULT.exists() and ask.confirm_default_path():
        return GamePath.DEFAULT

    return ask.enter_assets_path()


def mod_is_installed(assets: Path):
    """Проверка на наличие backup файлов"""
    langs = [localization.backup_filename(assets / lang.value) for lang in LangPath]
    return any([lang.exists() for lang in langs])


def apply(orig: Path, options: list[ModOption], lang: LangPath):
    """Применение модификации на локализацию"""
    mods = resources.options_to_path(options, lang)
    updated = localization.apply(path=orig, mods=mods)
    localization.save(orig, updated)


def install(assets: Path, options: list[ModOption]):
    """Установка модификации"""
    for lang in LangPath:
        orig = assets / lang.value

        backup = localization.backup_filename(orig)
        if not backup.exists():
            localization.backup(orig)

        apply(orig, options, lang)


def uninstall(assets: Path):
    """Удаление модификации"""
    for lang in LangPath:
        orig = assets / lang.value

        backup = localization.backup_filename(orig)
        if backup.exists():
            localization.restore(orig, backup)


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
