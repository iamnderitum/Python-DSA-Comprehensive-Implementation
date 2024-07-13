with open("sample1.txt") as f:
    text = "".join(f)
print(text)

def concordance(text):
    freq = {}
    for word in text.split():
        if word not in freq:
            freq[word] = 0
        freq[word] += 1

    return freq

word_count = concordance(text)
for word in word_count:
    print(word_count,end="\n")

from re import sub