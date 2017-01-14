"""
Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:
1c0111001f010100061a024b53535009181c

... after hex decoding, and when XOR'd against:
686974207468652062756c6c277320657965

... should produce:
746865206b696420646f6e277420706c6179
"""

inp = "1c0111001f010100061a024b53535009181c"
xorwith = "686974207468652062756c6c277320657965"
ans = "746865206b696420646f6e277420706c6179"
result = ""

inp = bytes.fromhex(inp)
xorwith = bytes.fromhex(xorwith)
ans = bytes.fromhex(ans)

for a, b in zip(inp, xorwith):
    # print("a:{}, b:{}".format(str(a), str(b)))
    c = chr(a ^ b)
    result += c
    # print(c)

result = result.encode()
print("{}\n{}".format(result, str(result == ans)))
