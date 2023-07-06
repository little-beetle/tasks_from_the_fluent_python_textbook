# Initializing a tuple and an array from a generator expression

import array

symbols = '$¢£¥€¤'

answer_1 = tuple(ord(symbol) for symbol in symbols)
print(answer_1)

answer_2 = array.array('I', (ord(symbol) for symbol in symbols))
print(answer_2)