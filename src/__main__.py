from src import ask
from src.consts import GamePath


def define_path():
    if GamePath.ASSETS.exists():
        if ask.confirm_default_path():
            return GamePath.ASSETS

    return ask.enter_assets_path()


def install():
    path = define_path()
    print(path)


def main():
    try:
        install()

    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
