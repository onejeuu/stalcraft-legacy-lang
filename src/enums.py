from enum import Enum, StrEnum
from pathlib import Path

from src.consts import LangFile


class ModOption(StrEnum):
    FRACTIONS = "Фракции"
    ARTEFACTS = "Артефакты и Аномалии"
    ITEMS = "Снаряжение (Броня и Оружие)"
    NAMES = "Лор (Локации, Мутанты, Расходники)"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore") / LangFile.PATH
    STALKER = Path("stalker") / LangFile.PATH
