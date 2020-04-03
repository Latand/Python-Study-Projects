
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
matchs = [input().split(';') for _ in range(int(input()))]
res_tab = {}
for x in matchs:
    res_tab[x[0]] = [0, 0, 0, 0, 0]
    res_tab[x[2]] = [0, 0, 0, 0, 0]
for a, b, c, d in matchs:
    res_tab[a][0] += 1
    res_tab[c][0] += 1
    if int(b) > int(d):
        res_tab[a][1] += 1
        res_tab[a][4] += 3
        res_tab[c][3] += 1
    elif int(b) < int(d):
        res_tab[c][1] += 1
        res_tab[c][4] += 3
        res_tab[a][3] += 1
    else:
        res_tab[a][2] += 1
        res_tab[c][2] += 1
        res_tab[a][4] += 1
        res_tab[c][4] += 1
for key, values in res_tab.items():
    print((key + ':'), *values)


# a=[input().split(';') for i in range(int(input()))]
# b={i:[] for i in set([i[0] for i in a])|set([i[2] for i in a])}
# for i in a:
# 	b[i[0]].append(1 if i[1]==i[3] else 3 if i[1]>i[3] else 0)
# 	b[i[2]].append(1 if i[1]==i[3] else 3 if i[1]<i[3] else 0)
# for i in b: print('%s:%i %i %i %i %i'%(i,len(b[i]),b[i].count(3),b[i].count(1),b[i].count(0),sum(b[i])))


# def command(c, res):
#     if not c in dct: dct[c] = [0, 0, 0, 0, 0]
#     dct[c] = [dct[c][0] + 1,
#                 dct[c][1] + 1 if res == 3 else dct[c][1],
#                 dct[c][2] + 1 if res == 1 else dct[c][2],
#                 dct[c][3] + 1 if res == 0 else dct[c][3],
#                 dct[c][4] + res,]
# dct = {}
# for i in range(int(input())):
#     c1, g1, c2, g2 = input().split(';')
#     command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
#     command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
# for c in dct:
#     print('{}:{} {} {} {} {}'.format(c, *dct[c]))

# *что-то 1* if *условие* else *что-то 2* - это аналог тернарного оператора, если вы знакомы с C/C++.
# Возвращает *что-то 1*, если *условие* истинно, *что-то 2* в противном случае.
# command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
# #полностью эквивалентно следующей конструкции
# if g1 > g2:
#     res = 3
# elif g1 == g2:
#     res = 1
# else:
#     res = 0
# command(c1, res)
