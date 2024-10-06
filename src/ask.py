from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from src.assets_validator import AssetsPathValidator
from src.consts import GamePath


def confirm_default_path():
    return inquirer.select(  # type: ignore
        message=f"Найден стандартный путь до ассетов игры: {GamePath.ASSETS.as_posix()}. Всё верно?",
        choices=[
            Choice(True, name="Да, продолжить"),
            Choice(False, name="Нет, изменить"),
        ],
    ).execute()


def enter_assets_path():
    return inquirer.filepath(  # type: ignore
        message="Введите путь до папки ассетов игры",
        validate=AssetsPathValidator(),
        only_directories=True,
    ).execute()
