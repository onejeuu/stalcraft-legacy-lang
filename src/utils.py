from pathlib import Path

from src.consts import DATA
from src.enums import LangPath, ModOption


def options_to_path(mods: list[ModOption], lang: LangPath) -> list[Path]:
    paths = list(
        map(
            lambda option: DATA / option.name.lower() / f"{lang.name.lower()}.lang",
            mods,
        )
    )

    return list(filter(lambda path: path.exists(), paths))
