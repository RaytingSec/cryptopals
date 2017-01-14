#!/usr/bin/python3
# Convert hex to base64

import base64

ciphertext = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

print('start')

textbytes = bytes.fromhex(ciphertext)
plaintext = str(base64.encodebytes(textbytes), 'utf-8').strip('\n')

print('done\n{}\n{}'.format(plaintext, plaintext == answer))
