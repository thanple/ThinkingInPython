'使用urllib抓取信息,beautifulsoup进行解析'
#https://cuiqingcai.com/1319.html
# -*- coding: UTF-8 -*-
import os
import threading
from bs4 import BeautifulSoup

dir = 'E:\\autorun.inf\\BodyArt'
url = 'http://www.rt110.com'
threads = []

from urllib import request

class DownLoadImageThread(threading.Thread):
    def __init__(self,image_src, fileName):
        threading.Thread.__init__(self)  # 调用父类
        self.image_src = image_src
        self.fileName = fileName
        return

    def run(self):
        try:
            f = open(self.fileName, 'wb')
            f.write((request.urlopen(self.image_src)).read())
            print("write successful" , self.image_src, ",",self.fileName)
            f.close()
        except Exception as e:
            os.remove(self.fileName)
            print("write failed", self.image_src, ",", self.fileName)

def downloadAllCurrentPageImage(curentUrl, dirPath):
    response = request.urlopen(curentUrl)
    html = response.read().decode('UTF-8')
    soup = BeautifulSoup(html, "html5lib")
    try:
        image_src = soup.find('div',class_='content_pic').a.img['src']
        filename = image_src[image_src.rfind('/'):]
        thread1 = DownLoadImageThread(image_src, dirPath+filename)
        threads.append(thread1)
        thread1.start()
    except Exception as e:
        print("content_pic failed")
    pages = soup.find('div', id='pages')
    for ePage in pages.find_all('a'):
        if(ePage.text== '下一页' and ePage['href'] != curentUrl):
            downloadAllCurrentPageImage(ePage['href'],dirPath )
            break

def dealCurrentPage(page):
    response = request.urlopen(url+page)
    html = response.read().decode('UTF-8')
    soup = BeautifulSoup(html,"html5lib")
    main_column = soup.find('div', class_='main_column')
    for li in main_column.find_all('li', class_='main_column_pic'):
        if not os.path.exists(dir+"/"+li.text):
            os.makedirs(dir+"/"+li.text)
        print("--------------- Dealing " + li.a['href'], ", title=", li.text)
        downloadAllCurrentPageImage(li.a['href'],dir+"/"+li.text)
    for ePage in main_column.div.find_all('a'):
        if(ePage.text== '下一页' and ePage['href'] != page):
            dealCurrentPage(ePage['href'])
            break


if __name__ == "__main__":
    dir += "/汤加丽"
    dealCurrentPage("/tangjiali")
    for eh in  threads:
        eh.join()

    print("Download All successful!!!")

