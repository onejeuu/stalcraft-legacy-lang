from enum import Enum, StrEnum
from pathlib import Path


class ModOption(StrEnum):
    FRACTIONS = "Фракции"
    ARTEFACTS = "Артефакты"
    ANOMALIES = "Аномалии"
    NAMES = "Наименования (Локации, Мутанты, Прочее)"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore/lang/ru.lang")
    STALKER = Path("stalker/lang/ru.lang")
