from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.validator import EmptyInputValidator

from src.assets_validator import AssetsPathValidator
from src.consts import GamePath
from src.enums import ModOption


def confirm_default_path():
    return inquirer.select(  # type: ignore
        message=f"Найден стандартный путь до ассетов игры\n{GamePath.ASSETS.as_posix()}\nВсё верно?",
        pointer=">",
        choices=[
            Choice(True, name="Да, продолжить"),
            Choice(False, name="Нет, изменить"),
        ],
    ).execute()


def enter_assets_path():
    return inquirer.filepath(  # type: ignore
        message="Введите путь до папки ассетов игры:",
        validate=AssetsPathValidator(),
        only_directories=True,
    ).execute()


def mod_options():
    return inquirer.checkbox(  # type: ignore
        message="Выберите опции модификации (на пробел):",
        choices=[Choice(option, name=option.value, enabled=True) for option in ModOption],
        validate=EmptyInputValidator(),
        transformer=lambda result: ", ".join(result),
        pointer=">",
        enabled_symbol="✅",
        disabled_symbol="❌",
        keybindings={
            "toggle": [
                {"key": "space"},
                {"key": "left"},
                {"key": "right"},
            ],
        },
    ).execute()


def uninstall_mod():
    return inquirer.select(  # type: ignore
        message="Похоже мод уже установлен. Вы хотите удалить мод или продолжить установку?",
        pointer=">",
        choices=[
            Choice(False, name="Продолжить установку"),
            Choice(True, name="Удалить модификацию"),
        ],
    ).execute()
