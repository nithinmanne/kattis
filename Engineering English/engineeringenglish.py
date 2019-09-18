from sys import stdin
words = set()
for line in stdin:
    for word in line.split():
        cword = word.lower()
        if cword in words:
            print('.', end=' ')
        else:
            print(word, end=' ')
            words.add(cword)
    print()