#根据百度ai平台提供的爬虫教程完成
#爬取豆瓣电影top250
import sys
from bs4 import BeautifulSoup
import re
import urllib.request
import xlwt

#得到页面全部内容
def askURL(url):
    #发送请求
    request = urllib.request.Request(url)
    try:
        #获取相应，获取网页内容
        response = urllib.request.urlopen(request)
        html = response.read()
        print (html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print (e.code)
        if hasattr(e,"reason"):
            print (e.reason)
    return html

#获取相关内容
def getData(baseurl):
    #根据豆瓣电影页面DOM结构来获取相关内容
    #获取电影链接，图片，片名，评分，评价人数，概况和其他信息
    findLink = re.compile(r'<a href="(.*?)">')
    findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
    #去掉无关内容
    remove = re.compile(r'                            |\n|</br>|\.*')
    datalist = []
    #豆瓣电影每页展示25部电影，因此要爬取前250需要10页
    for i in range(0, 10):
        #每页共25项，爬取完成后翻页
        #新页面仅在首页url中添加了字符串序列数（该页第一项序号，从零开始）
        url = baseurl + str(i*25)
        #请求新页面
        html = askURL(url)
        #html分词器
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_='item'):
            #找到每一个影片项
            data = []
            item = str(item)
            # 影片详情链接
            link = re.findall(findLink,item)[0]
            #添加详情链接  
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            #添加图片链接
            data.append(imgSrc)
            titles = re.findall(findTitle,item)
            #片名可能只有一个中文名，没有外国名
            if(len(titles) == 2):
                ctitle = titles[0]
                #添加中文片名
                data.append(ctitle)
                #去掉无关符号
                otitle = titles[1].replace("/","")
                #添加外国片名
                data.append(otitle)
            else:
                #缺失外文名，需添加占位，否则List超范围
                data.append(titles[0])
                data.append(' ')
            #添加评分，评论人数
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq,item)
            #可能没有概况
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(' ')
            bd = re.findall(findBd,item)[0]
            bd = re.sub(remove,"",bd)
            bd = re.sub('<br(\s+)?\/?>(\s+)?'," ",bd)
            bd = re.sub('/', " ",bd)
            data.append(bd.strip())
            datalist.append(data)
    return datalist

#将爬取的数据写入excel中
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)
    col = ('电影链接', '图片链接','中文名','外文名','评分','评价数','概况','相关信息')
    for i in range(0, 8):
        #添加列名
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        data = datalist[i]
        for j in range(0, 8):
            #添加数据
            sheet.write(i+1, j, data[j])
    book.save(savepath)
def main():
    print ("开始爬取......")
    #豆瓣电影首页地址，此后每次翻页加25
    baseurl = 'https://movie.douban.com/top250?start='
    datalist = getData(baseurl)
    savepath = u'豆瓣电影列表.xls'
    saveData(datalist, savepath)

main()
print ("爬取完成，请查看")
