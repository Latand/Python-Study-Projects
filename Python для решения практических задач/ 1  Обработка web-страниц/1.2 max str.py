from urllib.request import urlopen

text = str(urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8'))
opentag = '<code>'
closetag = '</code>'
ans = {}
while text.find(opentag) != -1:
    if text[text.find(opentag) + len(opentag):text.find(closetag)] not in ans:
        ans[text[text.find(opentag) + len(opentag):text.find(closetag)]] = 1
    else:
        ans[text[text.find(opentag) + len(opentag):text.find(closetag)]] += 1
    text = text[text.find(closetag) + len(closetag):]
res = [key for key, value in ans.items() if value > 3]
res.sort()
print(*res)


# import requests, collections, re
# res = requests.get(' https://stepik.org/media/attachments/lesson/209719/2.html').text
# print(*collections.Counter(re.findall(r'<code>(.*?)</code>', res)).most_common())
