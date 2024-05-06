from colorama import init, Fore

def colorize_ascii_art(input_file, output_file):
    """Функция перекрашивающая аски арт из чб в разный
    просмотр возможен только на UNIX"""
    init(autoreset=True)

    ascii_chars = {
        "@": Fore.BLUE,
        "#": Fore.YELLOW,
        "S": Fore.RED,
        "%": Fore.GREEN,
        "?": Fore.YELLOW,
        "*": Fore.BLUE,
        "+": Fore.MAGENTA,
        ";": Fore.CYAN,
        ":": Fore.WHITE,
        ",": Fore.BLACK,
        ".": Fore.RESET
    }

    with open(input_file, "r") as f:
        ascii_art = f.readlines()

    with open(output_file, "w") as f:
        for line in ascii_art:
            for char in line:
                color = ascii_chars.get(char)
                if color:
                    f.write(color + char)
                else:
                    f.write(char)
