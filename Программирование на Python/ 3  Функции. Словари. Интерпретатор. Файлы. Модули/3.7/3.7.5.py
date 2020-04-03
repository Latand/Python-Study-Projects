with open(str('C:\\Users\\semen\\PycharmProjects\\untitled2\\input.txt'), 'r', encoding = "utf-8") as file:
    data = [line.split('\t') for line in file.read().strip().split('\n')]
students = {x: [0, 0] for x in range(1, 12)}
for i in data:
    students[int(i[0])][0] += int(i[2])
    students[int(i[0])][1] += 1
for key in students:
    print(key, end = ' ')
    if students[key][0] == 0:
        print('-')
    else:
        print(students[key][0] / students[key][1])

#
# c = {str(i):[0]*2 for i in range(1,12)}
# for l in open('in'):
#     s = l.strip().split()[::2]
#     c[s[0]] = [c[s[0]][0] + int(s[1]), c[s[0]][1] + 1]
# [print(k + ' ', v[0]/v[1] if v[0] else '-') for k, v in c.items()]
#
#
# d = {i: [] for i in range(1,12)}
# with open(r'D:\Новая папка\dataset_3380_5.txt','r', encoding='utf-8') as f1:
#   for i in f1:
#     d[int(i.split()[0])].append(float(i.split()[2]))
#
# for i in range(1,12):
#   if d[i]:
#     print(i, sum(d[i])/len(d[i]))
#   else:
#     print(i, '-')
#
#     import pandas as pd
#
# df = pd.read_table('C:\\Users\\User\\Desktop\\py_course\\dataset_3380_5.txt', header = None, sep = r'\s{1,}')
# print(df.groupby(0).mean())
#
#
# inf = [l.split('\t') for l in open('file.txt', 'r').read().strip().splitlines()]
# #подгружаем файл в виде массива вида [[класс, фамилия, рост],...]
#
# d = {}                                #создаём словарь вида{класс:суммарный рост}
# for y in range(1,12):             #для каждого класса
#     d[y], c = 0, 0                    #создаём нулевое значение суммарного роста и счётчика учеников
#     for i in inf:                    #пробегаемся по строкам файла
#         if int(i[0]) == y:            #если нашли нужный класс, то
#             d[y] += int(i[2])           #увеличиваем суммарный рост
#             c += 1                   #увеличиваем счётчик количества учеников
#     print(y, '-' if c == 0 else str(d[y] / c)) #печатаем класс и средний рост
