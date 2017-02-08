#!/usr/bin/python3
# Detect single byte XOR
import collections


def charxor(string, char):
    xored = [bytes([a ^ ord(char)]) for a in string]
    return b''.join(xored)


def freqtest(string):
    commonletters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
    commonbytes = []
    for c in commonletters:
        commonbytes.append(str.encode(c))

    common = collections.Counter(string.replace(' ', '')).most_common()[0][0]
    if common in commonletters:
        return True
    else:
        return False


with open('4.txt') as f:
    ciphertexts = map(bytes.fromhex, f.read().split('\n'))

for text in ciphertexts:
    # textbytes = bytes.fromhex(text)
    # print('text: ' + text)
    for x in range(0, 255):
        char = chr(x)
        xored = charxor(textbytes, char)
        try:
            xored = str(xored, 'utf-8')
            if freqtest(xored):
                print('{}: {}'.format(char, xored))
        except UnicodeDecodeError:
            # print("failed")
            pass
