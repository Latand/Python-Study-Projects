
# abcd
# *d%#
# abacabadaba
# #*%*d*%

dictionary = list(input())
key = list(input())


def code(letter):
    if letter in dictionary:
        return key[dictionary.index(letter)]
    else:
        return letter


def decode(letter):
    if letter in key:
        return dictionary[key.index(letter)]
    else:
        return letter


message = [code(x) for x in list(input())]
crypto_message = [decode(x) for x in list(input())]

for i in message:
    print(i, end='')
print()
for i in crypto_message:
    print(i, end='')

# a,b,c,d=input(),input(),input(),input()
# print(''.join(b[a.index(i)] for i in c))
# print(''.join(a[b.index(i)] for i in d))

# # Считываем 4 строки в цикле
# original, coding, first_string, second_string = (input() for i in range(4))
#
# # По индексу символа из оригинала берём символ на замену из кодировки,
# # для каждого символа из строки, которую нужно закодировать
# print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# # Аналогично, только наоборот :D
# print(*[original[coding.find(symbol)] for symbol in second_string], sep='')


