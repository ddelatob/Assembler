import sys
import os

class Token:
    def __init__(self):
        pass


def tokenize_line(line: str):
    pass


def main():
    if len(sys.argv) != 2:
        print(f"usage: python {os.path.basename(sys.argv[0])} file.txt", file=sys.stderr)

    input_filename = sys.argv[1]

    base_name, _ = os.path.splitext(input_filename)
    outfile = base_name + ".bin"

    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    print(lines)
if __name__ == "__main__":
    main()