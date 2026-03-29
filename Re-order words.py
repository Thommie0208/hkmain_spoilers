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

writefile('ss-help.txt', sorted(readfile('ss-help.txt')))