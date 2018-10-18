from contextlib import redirect_stdout

with open("collation.in", encoding="utf-8") as f:
    ordered = sorted([line.strip() for line in f.readlines()])

with open("collation.out", "w", encoding="utf-8") as f:
    with redirect_stdout(f):
        print("\n".join(ordered))