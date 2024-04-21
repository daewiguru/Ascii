import sys
from translate.translate import save_ascii_art
from gui.inter import display_ascii_in_window

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <path_to_image>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_file = "save_ascii.txt"

    save_ascii_art(input_image, output_file)
    print("ASCII-графика сохранена в", output_file)
    display_ascii_in_window(output_file)
