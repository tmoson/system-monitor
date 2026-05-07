from .display import Display
import asyncio


def main() -> None:
    display = Display()
    asyncio.run(display.run())
    print("Goodbye.")
