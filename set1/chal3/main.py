#!/usr/bin/python3
# Single-byte XOR cipher


def charxor(string, char):
    xored = [bytes([a ^ ord(char)]) for a in string]
    return b''.join(xored)


ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
cipherbytes = bytes.fromhex(ciphertext)

for x in range(0, 26):
    # A 65, a 97
    xor = chr(65 + x)
    print(xor, charxor(cipherbytes, xor))

# print('done\n{}\n{}'.format(plaintext, plaintext == answer))
