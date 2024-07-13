from string import ascii_letters,ascii_lowercase

CODEBOOK = {x: {} for x in ascii_letters}
#print(CODEBOOK)
CODEBOOK = {x: {y: None for y in ascii_letters} for i, x in enumerate(ascii_letters)}
# print(CODEBOOK)
CODEBOOK = {x: {y: ascii_lowercase[(j + 1) % len(ascii_lowercase)]
                for j, y in enumerate(ascii_lowercase)} for i, x in enumerate(ascii_lowercase)}

print(CODEBOOK)