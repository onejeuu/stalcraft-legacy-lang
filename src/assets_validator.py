from pathlib import Path
from typing import Any

from prompt_toolkit.validation import ValidationError, Validator

from src.consts import RequiredPath


class AssetsPathValidator(Validator):
    def _find_assets(self, path: Path):
        if "steamapps" in path.parts:
            return self._validate_assets(path, RequiredPath.STEAM)
        return self._validate_assets(path, RequiredPath.LAUNCHER)

    def _validate_assets(self, path: Path, required: Path):
        parts = list(path.parts)

        # Очищаем введеный путь от частей required
        for target in required.parts:
            if parts and parts[-1] == target:
                parts.pop()
            else:
                break

        # Возвращаем полный путь до ассетов
        return Path(*parts) / required

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
        finded = self._find_assets(path)

        if not finded.exists():
            raise ValidationError(
                message="Указанный путь не содержит путь до ассетов игры.",
                cursor_position=document.cursor_position,
            )

        # Обновляем данные на полный путь до ассетов
        document.text = finded.as_posix()
