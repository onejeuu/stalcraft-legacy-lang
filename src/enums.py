from enum import Enum, StrEnum
from pathlib import Path


class ModOption(StrEnum):
    LOCATIONS = "Локации"
    MOBS = "Мутанты"
    EQUIPMENTS = "Снаряжение"
    ARTEFACTS = "Артефакты"
    ITEMS = "Предметы"
    SKINS = "Облики"


class LangPath(Enum):
    GLOOMYCORE = Path("gloomycore/lang/ru.lang")
    STALKER = Path("stalker/lang/ru.lang")
