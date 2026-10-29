import sys
import os

line_no = 0
output = bytearray()

def file_write(outfile: str):
    with open(outfile, "wb") as f:
        f.write(output)   

def parse():
    pass

def assemble(lines: list[str], outfile: str):
    for line in lines:
        parse()
    file_write(outfile)



def main():
    if len(sys.argv) != 2:
        print("usage: python main.py file.txt", file=sys.stderr)
        return

    input_filename = sys.argv[1]

    base_name, _ = os.path.splitext(input_filename)
    outfile = base_name + ".bin"

    with open(input_filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    print(lines, outfile)
    assemble(lines, outfile);
if __name__ == "__main__":
    main()