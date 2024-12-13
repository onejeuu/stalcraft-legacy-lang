from copy import copy
from pathlib import Path
from typing import Any

from prompt_toolkit.validation import ValidationError, Validator

from src.consts import LANGS_FILES, STEAM_DIRECTORY, RequiredPath


def validate_langs(base: Path):
    return all([Path(base / lang).exists() for lang in LANGS_FILES])


def validate_assets(path: Path, required: Path):
    # ? Если указанный путь содержит полные каталоги до lang файлов
    if validate_langs(path):
        return path

    # ? Если путь оканчивается на полный required
    if path.match(f"*{required}"):
        return path

    # ? Проверка на частичное совпадение required
    candidate = copy(required)

    while candidate.parts:
        if path.match(f"*{candidate}"):
            # ? Возвращаем полный путь именно до ассетов
            return path / required.relative_to(candidate)
        else:
            # ? Уменьшаем потенциальный путь
            candidate = candidate.parent

    return path / required


def find_assets(path: Path):
    # Определяем точность RequiredPath по наличию стима в указанном пути
    required = RequiredPath.STEAM if STEAM_DIRECTORY in path.parts else RequiredPath.LAUNCHER

    return validate_assets(path=path, required=required)


class AssetsPathValidator(Validator):
    def validate(self, document: Any) -> None:
        path = Path(document.text).expanduser()

        # Проверяем, существует ли указанный путь
        if not path.exists():
            raise ValidationError(
                message="Указанный путь не найден",
                cursor_position=document.cursor_position,
            )

        # Проверяем, является ли указанный путь директорией
        if not path.is_dir():
            raise ValidationError(
                message="Указанный путь не является директорией",
                cursor_position=document.cursor_position,
            )

        # Проверяем, находится ли в указанном пути ассеты игры
        found = find_assets(path)

        if not found or not found.exists() or not validate_langs(found):
            raise ValidationError(
                message="Указанный путь не содержит ассетов игры",
                cursor_position=document.cursor_position,
            )

        # Обновляем данные на полный путь до ассетов
        document.text = found.as_posix()
