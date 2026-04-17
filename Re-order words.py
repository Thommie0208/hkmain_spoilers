import os

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "hk-help.txt")

def readfile(filename: str) -> list[str]:
    words = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line.lower())
    return words

def writefile(filename: str, words: list[str]) -> None:
    with open(filename, 'w') as f:
        for word in words:
            f.write(word + '\n')

writefile(path, sorted(readfile(path)))