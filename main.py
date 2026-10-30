import sys
import os

line_no = 0
addr = 0
num_pass = 0



output = bytearray()

def err(msg: str):
    print(f"main.py: {line_no + 1}: {msg}")
    exit()

def file_write(outfile: str):
    with open(outfile, "wb") as f:
        f.write(output)   

def process():
    pass

def parse(line: str):
    lab = None
    op = None
    a1 = None
    a2 = None
    comm = None

    line = line.strip()

    if not line or line.startswith(";"):
        return lab, op, a1, a2, comm

    if ";" in line:
        line, _, comm = line.partition(";")
        comm = comm.strip()
        line = line.strip()

    if ":" in line:
        lab, _, line = line.partition(":")
        lab = lab.strip()
        line = line.strip()

    if line:
        parts = line.split(maxsplit=1)
        op = parts[0]
        if len(parts) > 1:
            args = [arg.strip() for arg in parts[1].split(",")]
            if len(args) > 0:
                a1 = args[0]
            if len(args) > 1:
                a2 = args[1]
    print(lab, op, a1, a2, comm)
    return lab, op, a1, a2, comm




def assemble(lines: list[str], outfile: str):
    num_pass = 1
    for line in lines:
        parse(line)
        process()
    
    num_pass = 2
    for line in lines:
        parse()
    
    # file_write(outfile)



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