import sys
from pathlib import Path

from src.consts import DATADIR
from src.enums import LangPath, ModOption


def root() -> Path:
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / DATADIR  # type: ignore
    return Path(DATADIR)


ROOT = root()


def options_to_path(mods: list[ModOption], lang: LangPath) -> list[Path]:
    paths = list(
        map(
            lambda option: ROOT / option.name.lower() / f"{lang.name.lower()}.lang",
            mods,
        )
    )

    return list(filter(lambda path: path.exists(), paths))
