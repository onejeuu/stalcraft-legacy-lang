from pathlib import Path

import PyInstaller.__main__

from src.consts import DATADIR


NAME = "stalcraft-legacy-lang"

ROOT = Path(__file__).parent.absolute()

ENTRYPOINT = str(ROOT / "src" / "__main__.py")
ICON = str(ROOT / "assets" / "icon.ico")
SPECPATH = str(ROOT / "build")

DATA = str(ROOT / DATADIR)


def build():
    PyInstaller.__main__.run(
        [ENTRYPOINT, "-i", ICON, "--name", NAME, "--specpath", SPECPATH, "--add-data", f"{DATA}:{DATADIR}", "--onefile"]
    )


if __name__ == "__main__":
    build()
