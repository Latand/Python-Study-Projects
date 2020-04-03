
with open(str('input.txt'), 'r') as file:
    str = file.read().split()
str.sort()
count = 0
word = ''
for i in set(str):
    if str.count(i) > count:
        word = i
        count = str.count(i)
print(word, count)
#
# with open('words.txt') as f:
#     text = f.read().lower().split()
# popular_word = max(set(text), key=text.count)
# print(popular_word, text.count(popular_word))