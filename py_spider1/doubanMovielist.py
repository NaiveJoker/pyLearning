import requests
from lxml import html

#Get url
url = "https://movie.douban.com/"
page = requests.Session().get(url)
tree = html.fromstring(page.text)
#Locate data I need
result = tree.xpath('//td[@class="title"]//a/text()')

resFile = open("result.txt", 'w')
resFile.write(str(result))
resFile.close()
