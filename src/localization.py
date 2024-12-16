import shutil
from functools import reduce
from pathlib import Path
from tkinter.tix import Tree
from typing import TypeAlias

from src.consts import BACKUP_DIRECTORY


Localization: TypeAlias = dict[str, str]


def load(path: Path) -> Localization:
    """Загрузить локализацию"""
    localization: Localization = {}

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line := line.strip():
                # Разделяем строку на ключ и значение
                key, value = (line.split("=", maxsplit=1) + [""])[:2]

                # ? Значение может быть пустым или пробелы могут иметь важную роль
                localization[key.strip()] = value

    return localization


def save(output: Path, localization: Localization) -> None:
    """Сохранить локализацию"""
    with open(output, "w", encoding="utf-8") as file:
        for key, value in localization.items():
            file.write(f"{key}={value}\n")


def update(localization: Localization, modded: Localization) -> Localization:
    """Обновить словарь локализации"""
    for key, new_value in modded.items():
        localization[key] = new_value
    return localization


def restore(orig: Path, bck: Path) -> None:
    """Восстановить файл локализации"""
    orig.unlink(missing_ok=True)
    bck.rename(orig)


def backup_prepare() -> None:
    """Создает директорию для резервных копий"""
    BACKUP_DIRECTORY.mkdir(exist_ok=True, parents=True)


def backup_filename(path: Path) -> Path:
    """Название файла резервной копии"""
    return BACKUP_DIRECTORY / path.name


def backup(orig: Path) -> None:
    """Восстановить оригинальный файл"""
    backup_prepare()
    bck = backup_filename(orig)
    shutil.copy2(orig, bck)


def apply(path: Path, mods: list[Path]) -> Localization:
    """Применить легаси локализацию"""
    localization = load(path)

    updated = reduce(lambda base, mod: update(base, load(mod)), mods, localization)
    return updated
