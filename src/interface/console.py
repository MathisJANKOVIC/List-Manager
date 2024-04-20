import sys

# Colors are ordered according to their corresponding ANSI escape codes
_ANSI_COLORS = ("default", "red", "green", "yellow", "blue", "magenta", "cyan", "white")
_DEFAULT_MARGIN = 1

def clear_line() -> None:
    sys.stdout.write("\033[K")

def move_cursor_up(lines: int = 1) -> None:
    sys.stdout.write("\033[F" * lines)

def move_cursor_down(lines: int = 1) -> None:
    sys.stdout.write("\n" * lines)

def write(text: str, color: str | None = None, margin: int = _DEFAULT_MARGIN) -> None:
    text = " " * margin + text
    if(color is None):
        sys.stdout.write(text)
    else:
        if(color.startswith("light")):
            sys.stdout.write(f"\033[9{_ANSI_COLORS.index(color.removeprefix('light_'))}m{text}\033[0m")
        elif(color in _ANSI_COLORS):
            sys.stdout.write(f"\033[3{_ANSI_COLORS.index(color)}m{text}\033[0m")
        else:
            raise ValueError(f"'{color}' is not a valid color")

def prompt(text: str, color: str | None = None, margin: int = _DEFAULT_MARGIN) -> str:
    write(text + " ", color, margin)
    return input()
