from enum import Enum, StrEnum
from pathlib import Path

from src.consts import LangFile


class ModOption(StrEnum):
    FRACTIONS = "Фракции"
    ITEMS = "Снаряжение"
    ARTEFACTS = "Артефакты"
    NAMES = "Лор"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore") / LangFile.PATH
    STALKER = Path("stalker") / LangFile.PATH
