import os

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "ss-help.txt")


def readfile(filename: str) -> list[str]:
    words = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().lower()
            if line:
                words.append(line)
    return words


def sub_phrases(phrase: str) -> set[str]:
    parts = phrase.split()
    n = len(parts)
    result = set()
    for length in range(1, n):           
        for start in range(n - length + 1):
            result.add(" ".join(parts[start:start + length]))
    return result


def removedupes(words: list[str]) -> list[str]:
    word_set = set(words)                    
    kept = []
    for phrase in word_set:
        if sub_phrases(phrase) & word_set:
            continue
        kept.append(phrase)
    return kept


def writefile(filename: str, words: list[str]) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for word in words:
            f.write(word + '\n')


if __name__ == "__main__":
    writefile(path, sorted(removedupes(readfile(path))))
