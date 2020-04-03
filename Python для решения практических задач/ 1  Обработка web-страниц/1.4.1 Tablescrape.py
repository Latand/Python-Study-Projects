from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

text = str(urlopen('https://stepik.org/media/attachments/lesson/209723/3.html').read().decode('utf-8'))

opentag = '<td>'
closetag = '</td>'
ans = 0
while text.find(opentag) != -1:
    ans += int(text[text.find(opentag) + len(opentag):text.find(closetag)])
    text = text[text.find(closetag) + len(closetag):]
print(ans)


# import requests as req
# from bs4 import BeautifulSoup
# res = req.get('https://stepik.org/media/attachments/lesson/209723/3.html')
# soup = BeautifulSoup(res.text, 'html.parser')
# print(sum(int(td.text) for td in soup.find_all('td')))
