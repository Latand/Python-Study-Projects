
import requests as req
from bs4 import BeautifulSoup
res = req.get('https://stepik.org/media/attachments/lesson/209723/4.html')
soup = BeautifulSoup(res.text, 'html.parser')
print(sum(int(td.text) for td in soup.find_all('td')))


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html')
# table = BeautifulSoup(resp.read().decode('utf8'), 'html.parser').select('table > tr > td')
# print(sum([int(t.text) for t in table]))
