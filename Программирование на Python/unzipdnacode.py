with open(str(input('Укажите путь к файлу с жатым геномом:')), 'r') as file:
    zip_code = file.readline().strip()  # читаем сжатый геном
count = '0'
count_len = 1
with open(str(input('В какой файл записать расшифрованный геном:')), 'w') as file:
    for x in range(len(zip_code)):
        if not '0' <= zip_code[x] <= '9':  # если текущий симол не цифра
            while x+count_len < len(zip_code) and '0' <= zip_code[x+count_len] <= '9':  # если следующий символ цифра
                count += zip_code[x+count_len]
                count_len += 1
            file.write(zip_code[x]*int(count))  # записываем расшифровку в файл
            count = '0'
            count_len = 1
print('Расшифровка выполнена')
