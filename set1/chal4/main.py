#!/usr/bin/python3
# Detect single byte XOR


def charxor(string, char):
    xored = [bytes([a ^ ord(char)]) for a in string]
    return b''.join(xored)


with open('4.txt') as f:
    ciphertexts = f.read().split('\n')

for text in ciphertexts:
    textbytes = bytes.fromhex(text)
    for x in range(0, 26):
        char = chr(65 + x)
        xored = charxor(textbytes, char)
        try:
            print(char, str(xored, 'utf-8').encode('utf-8'))
        except UnicodeDecodeError:
            # print("failed")
            pass
