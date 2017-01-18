#!/usr/bin/python3
# Single-byte XOR cipher

import collections


def charxor(string, char):
    xored = [bytes([a ^ ord(char)]) for a in string]
    return b''.join(xored)


def freqtest(string):
    commonletters = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
    commonbytes = []
    for c in commonletters:
        commonbytes.append(str.encode(c))

    common = collections.Counter(xored.replace(' ', '')).most_common()[0][0]
    if common in commonletters:
        return True
    else:
        return False


ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
cipherbytes = bytes.fromhex(ciphertext)

for x in range(0, 26):
    # A 65, a 97
    xor = chr(65 + x)
    xored = str(charxor(cipherbytes, xor), 'utf-8')
    # print('{}\n{}'.format(xored, collections.Counter(xored.replace(' ', '')).most_common()[0:3]))
    if freqtest(xored):
        print('{}: {}'.format(xor, xored))

# print('done\n{}\n{}'.format(plaintext, plaintext == answer))
