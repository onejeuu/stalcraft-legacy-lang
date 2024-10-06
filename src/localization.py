import shutil
from functools import reduce
from pathlib import Path
from typing import TypeAlias


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
        localization[key] = new_value
    return localization


def backup(path: Path):
    bck = path.with_name(f"{path.name}.bck")

    if bck.exists():
        path.unlink(missing_ok=True)
        bck.rename(path)

    shutil.copy2(path, bck)


def apply(path: Path, mods: list[Path]):
    localization = load(path)

    updated = reduce(lambda base, mod: update(base, load(mod)), mods, localization)
    return updated
