from random import randint


dec = randint(0, 100)
divided = dec
result = []

while divided != 0:
    result.append(divided % 2)
    divided = divided // 2

result = ''.join(str(i) for i in result[::-1])
print(dec, '->', result)
