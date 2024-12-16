import os
from pathlib import Path

from src import ask, localization, resources
from src.consts import LANGS_FILES, GamePath
from src.enums import LangDirectory, LangFile, ModOption
from src.validator import validate_langs


def define_assets_path():
    """Определить путь до ассетов игры"""
    default = GamePath.DEFAULT
    if default.exists() and validate_langs(default) and ask.confirm_default_path():
        return default

    return ask.enter_assets_path()


def mod_is_installed(assets: Path):
    """Проверка на наличие любых резервных копий"""
    langs = map(lambda lang: assets / lang, LANGS_FILES)
    backups = map(localization.backup_filename, langs)
    return any([bck.exists() for bck in backups])


def apply(lang: Path, options: list[ModOption], directory: LangDirectory):
    """Применение модификации на локализацию"""
    mods = resources.options_to_path(options, directory)
    updated = localization.apply(path=lang, mods=mods)
    localization.save(lang, updated)


def install(assets: Path, file: LangFile, options: list[ModOption]):
    """Установка модификации"""
    for directory in LangDirectory:
        lang = assets / directory.value / file.value

        backup = localization.backup_filename(lang)
        if not backup.exists():
            localization.backup(lang)

        apply(lang, options, directory)


def uninstall(assets: Path):
    """Удаление модификации"""
    for directory in LangDirectory:
        for file in LangFile:
            orig = assets / directory.value / file.value

            backup = localization.backup_filename(orig)
            if backup.exists():
                localization.restore(orig, backup)


def main():
    localization.backup_prepare()

    assets = define_assets_path()

    if mod_is_installed(assets) and ask.uninstall_mod():
        uninstall(assets)
        return

    file = ask.lang_file()
    options = ask.mod_options()
    install(assets, file, options)


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
