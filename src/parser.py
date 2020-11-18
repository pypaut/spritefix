import argparse


def parse():
    parser = argparse.ArgumentParser(description="Fix your sprite sheet.")
    parser.add_argument(
        "-r",
        "--rows",
        help="number of rows in the sprite sheet",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--columns",
        help="number of columns in the sprite sheet",
        required=True,
    )
    return parser.parse_args()
