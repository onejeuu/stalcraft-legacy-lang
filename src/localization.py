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


def save(original: Path, localization: Localization):
    with open(original, "w", encoding="utf-8") as f:
        for key, value in localization.items():
            f.write(f"{key}={value}\n")


def update(original: Localization, modded: Localization):
    for key, new_value in modded.items():
        original[key] = new_value
    return original


def backup(original: Path):
    bck = original.with_name(f"{original.name}.bck")

    if bck.exists():
        original.unlink()
        bck.rename(original.name)

    shutil.copy2(original, bck)


def apply(original: Path, mods: list[Path]):
    backup(original)

    localization = load(original)

    updated = reduce(lambda base, mod: update(base, load(mod)), mods, localization)

    save(original, updated)
