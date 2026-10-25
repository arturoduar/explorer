"""Entry point for the explorer project."""

from explorer import __version__


def greet(name: str = "world") -> str:
    return f"Hello, {name}! (explorer v{__version__})"


def main() -> None:
    print(greet())


if __name__ == "__main__":
    main()
