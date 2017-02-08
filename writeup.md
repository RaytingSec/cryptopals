Cryptopals
==============================

## Set 1: Basics

### 1. Convert hex to base64

The challenge simple gives a starting string with that should result in another. While that's all it tells you, the title basically tells you what to do. The start string is hex, end result is base64. THe process should be:

> hex -> bytes -> base64

Interpreters are helpful for things like this, and along with python documentation and Google searching, I found `bytes.fromhex` and `base64.encodebytes` to be the cornerstone. I ended up with the following.

```python
import base64

ciphertext = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
answer = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

textbytes = bytes.fromhex(ciphertext)
plaintext = str(base64.encodebytes(textbytes), 'utf-8').strip('\n')

print('done\n{}\n{}'.format(plaintext, plaintext == answer))
```

Along the way I noticed the easteregg `textbytes` is the bytes for the string `b"I'm killing your brain like a poisonous mushroom"`

### 2. Fixed XOR

Same general idea, this time there's two staring strings xor-ed with each other, with an end result appearing to be hex. I began with a `bytesa ^ bytesb`, except the operator can't be used on bytes.

```
>>> cipherbytes ^ xorbytes
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ^: 'bytes' and 'bytes'
```

But the operator is usable on ints, and since bytes are iterables of ints, a solution is to iterate, xor, and join the result. The resulting process:

> split -> xor -> join -> hex

And resulting code:

```python
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
```

### 3. Single-byte XOR cipher

A given hex string is XORed, this time with an unknown char. Two possible approaches, although it hints at using character frequency, the alternative and simple solution is to bruteforce as the keyspace is just the alphabet.

I recycle the xor function from the previous challenge so it accepts just a character.

```python
def charxor(string, char):
    xored = [bytes([a ^ ord(char)]) for a in string]
    return b''.join(xored)
```

And the rest is done with a for loop:

```python
for x in range(0, 26):
    xor = chr(65 + x)
    print(xor, charxor(cipherbytes, xor))
```

output

```
...
W b'L``dfah/BL(|/cfdj/n/\x7f`zak/`i/mnl`a'
X b"Cooking MC's like a pound of bacon"
Y b'Bnnjhof!LB&r!mhjd!`!qntoe!ng!c`bno'
...
```

Since the prompt didn't specify which case the key was, I tried both capitol starting at 65, and lowercase at 97. `X` turned out to be the key.

I notice that while capitol produced the correct string, lower case with produce inverted case. Google searching indicates it's a known trick to xor the byte `\x20`, or the space character, to invert case.

### 4. Detect single byte XOR

