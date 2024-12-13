from enum import Enum, StrEnum
from pathlib import Path


class ModOption(StrEnum):
    FRACTIONS = "Фракции (Долг и Свобода)"
    ARTEFACTS = "Артефакты (Аномалии и Протоаномалии)"
    ITEMS = "Снаряжение (Броня и Оружие)"
    NAMES = "Лор (Локации, Мутанты, Расходники)"


class LangDirectory(Enum):
    GLOOMYCORE = Path("gloomycore/lang")
    STALKER = Path("stalker/lang")


class LangFile(Enum):
    RU = RUSSIAN = "ru.lang"
    EN = ENGLISH = "en.lang"
