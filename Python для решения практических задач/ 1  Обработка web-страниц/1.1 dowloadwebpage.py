from urllib.request import urlopen
text = str(urlopen('https://stepik.org/media/attachments/lesson/209717/1.html').read().decode('utf-8'))
if text.count('C++') > text.count('Python'):
    print('C++')
else:
    print('Python')