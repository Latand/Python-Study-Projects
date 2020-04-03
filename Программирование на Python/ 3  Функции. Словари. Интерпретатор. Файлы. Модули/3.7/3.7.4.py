
# 4
# север 10
# запад 20
# юг 30
# восток 40

dic = [[x for x in input().split()] for _ in range(int(input()))]
cord = {'север' : 0, 'восток': 0, 'запад': 0, 'юг': 0}
for i in dic:
    cord[i[0]] += int(i[1])
print(cord['восток'] - cord['запад'], cord['север'] - cord['юг'], end = ' ')
