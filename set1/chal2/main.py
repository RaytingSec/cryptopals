#!/usr/bin/python3
# Fixed XOR

import base64


def bytexor(a, b):
    if len(a) != len(b):
        print('inputs not same len')
        return
    xored = [bytes([aa ^ bb]) for aa, bb in zip(a, b)]
    return b''.join(xored)


ciphertext = '1c0111001f010100061a024b53535009181c'
xor = '686974207468652062756c6c277320657965'
answer = '746865206b696420646f6e277420706c6179'

xored = bytexor(bytes.fromhex(ciphertext), bytes.fromhex(xor))
plaintext = bytes.hex(xored)

print('done\n{}\n{}'.format(plaintext, plaintext == answer))
