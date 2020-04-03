
import requests
url = '699991.txt'
folder = 'https://stepic.org/media/attachments/course67/3.6.3/'
while url[0:2] != 'We':
    file = requests.get(folder + url)
    url = file.text.strip()
else:
    print(file.text)

# import requests
# url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'
# while name[:2] != 'We':
#     name = requests.get(url + name).text
# print(name)
