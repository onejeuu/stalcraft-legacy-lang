from enum import Enum, StrEnum
from pathlib import Path


class ModOption(StrEnum):
    FRACTIONS = "Фракции"
    ITEMS = "Снаряжение"
    ARTEFACTS = "Артефакты и Аномалии"
    NAMES = "Локации и Мутанты"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore/lang/ru.lang")
    STALKER = Path("stalker/lang/ru.lang")
