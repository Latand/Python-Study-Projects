
dic = [input().strip().lower() for _ in range(int(input()))]
user_input = [[x for x in input().strip().split() if x.lower() not in dic] for _ in range(int(input()))]
wrongs = set()
for row in user_input:
    for elem in row:
        if elem not in wrongs and elem.lower() not in wrongs:
            wrongs.add(elem)
            print(elem)


# words = set(input().lower() for i in range(int(input())))
# text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
# print('\n'.join(text - words))


# dic = {input().lower() for i in range(int(input()))}
#
# wrd = set()
# for w in range(int(input())):
#     wrd |= {i.lower() for i in input().split()}
#
# print(*wrd.difference(dic), sep="\n")


# know = {input().lower() for i in range(int(input()))}
# new_text = []
# for j in range(int(input())):
#     new_text+=(input().lower().split())
# for g in set(new_text) - know:
#         print(g,end='\n')
