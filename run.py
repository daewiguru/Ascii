import sys
import logging
from translate.translate import save_ascii_art
from translate.asn_translate import colorize_ascii_art
from gui.inter import display_ascii_in_window

logging.basicConfig(filename='ascii_conversion.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: python run.py <path_to_image> [<width> <height>]")
        sys.exit(1)
    elif len(sys.argv) > 4:
        logging.error("Too many arguments provided.")
        sys.exit(1)

        
    input_image = sys.argv[1]
    output_file = "save_ascii.txt"
    asn_output = 'output.asn'
    
    if len(sys.argv) == 2:
        save_ascii_art(input_image, output_file, size=(None, None))
        logging.info(f'Ascii art savet to {output_file}')
        display_ascii_in_window(output_file)
        colorize_ascii_art(output_file, asn_output)

    if len(sys.argv) == 4:
        width = int(sys.argv[2])
        height = int(sys.argv[3])
        size = (width, height)

        try:
            save_ascii_art(input_image, output_file, size=size)
            logging.info(f"Ascii art saved to {output_file} with custom size: {size}")
            colorize_ascii_art(output_file, asn_output)

        except Exception as e:
            logging.error(f'An error occurred: {e}')
