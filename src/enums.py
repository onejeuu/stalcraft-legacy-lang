from enum import Enum, StrEnum
from pathlib import Path


class ModOption(StrEnum):
    LOCATIONS = "Локации"
    FRACTIONS = "Фракции"
    EQUIPMENTS = "Снаряжение"
    ARTEFACTS = "Артефакты"
    ANOMALIES = "Аномалии"
    MOBS = "Мутанты"
    SKINS = "Облики"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore/lang/ru.lang")
    STALKER = Path("stalker/lang/ru.lang")
