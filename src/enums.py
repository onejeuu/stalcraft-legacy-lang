from enum import Enum, StrEnum
from pathlib import Path

from src.consts import LANG


class ModOption(StrEnum):
    FRACTIONS = "Фракции"
    ITEMS = "Снаряжение"
    ARTEFACTS = "Артефакты и Аномалии"
    NAMES = "Локации и Мутанты"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore") / LANG
    STALKER = Path("stalker") / LANG
