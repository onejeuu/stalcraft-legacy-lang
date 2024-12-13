import sys
from pathlib import Path

from src.consts import DATA_DIRECTORY
from src.enums import LangDirectory, ModOption


def data() -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / DATA_DIRECTORY  # type: ignore
    return Path(DATA_DIRECTORY)


DATA = data()


def options_to_path(mods: list[ModOption], directory: LangDirectory) -> list[Path]:
    paths = list(
        map(
            lambda option: DATA / option.name.lower() / f"{directory.name.lower()}.lang",
            mods,
        )
    )

    return list(filter(lambda path: path.exists(), paths))
