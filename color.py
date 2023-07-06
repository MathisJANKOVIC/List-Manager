class Color :
    def red(string: str):
        return f"\033[31m{string}\033[0m"

    def magenta(string: str):
        return f"\033[95m{string}\033[0m"