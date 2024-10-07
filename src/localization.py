import shutil
from functools import reduce
from pathlib import Path
from typing import TypeAlias

from src.consts import BACKUP_SUFFIX


Localization: TypeAlias = dict[str, str]


def load(path: Path) -> Localization:
    localization: Localization = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line := line.strip():
                key, value = line.split("=", 1)
                localization[key.strip()] = value.strip()

    return localization


def save(output: Path, localization: Localization):
    with open(output, "w", encoding="utf-8") as f:
        for key, value in localization.items():
            f.write(f"{key}={value}\n")


def update(localization: Localization, modded: Localization):
    for key, new_value in modded.items():
        if key not in localization:
            raise Exception(f"key '{key}' not found in localization")

        localization[key] = new_value
    return localization


def restore(orig: Path, bck: Path):
    orig.unlink(missing_ok=True)
    bck.rename(orig)


def backup_name(path: Path):
    return path.with_name(f"{path.name}.{BACKUP_SUFFIX}")


def backup(orig: Path):
    bck = backup_name(orig)
    shutil.copy2(orig, bck)


def apply(path: Path, mods: list[Path]):
    localization = load(path)

    updated = reduce(lambda base, mod: update(base, load(mod)), mods, localization)
    return updated
