
with open(str('input.txt'), "r", encoding = 'utf-8') as file:
    str = [line.split(';') for line in file.read().strip().split('\n')]
stud_res = [(int(mathematics) + int(physics) + int(russians)) / 3 for student, mathematics, physics, russians in str]
for st in stud_res:
    print(round(st, 9))
average_results_mathematics = sum([int(mathematics) for student, mathematics, physics, russians in str]) / len(str)
average_results_physics = sum([int(physics) for student, mathematics, physics, russians in str]) / len(str)
average_results_russians = sum([int(russians) for student, mathematics, physics, russians in str]) / len(str)
print(round(average_results_mathematics, 9), round(average_results_physics, 9), round(average_results_russians, 9))

#    sum([priceLow for fruit, priceLow, priceHigh in lst]) / len(lst), sum([priceHigh for fruit, priceLow, priceHigh in lst]) / len(lst))

# with open('words.txt') as f:
#     text = f.read().lower().split()
# popular_word = max(set(text), key=text.count)
# print(popular_word, text.count(popular_word))

# кто пишет на Python 3.5 и выше: решение не будет приниматься из-за точности вывода ответа.
# Точность нужна 9 знаков после запятой, по умолчанию стоит 6.
# Чтоб достичь нужного эффекта используйте функцию round(data, 9).
# Если используете СИ подобный write, то ouf.write ('%.9f %.9f %.9f' % data1, data2, data3)

# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку
# по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
# Также в конце файла, на отдельной строке, через пробел запишите средние баллы по
# математике, физике и русскому языку по всем абитуриентам.
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667



