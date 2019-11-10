# coding=utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree

file = "pkgs"


# 追加写入文件中
def saveToFile(download_url):
    ff = open("url.txt", 'a')
    ff.write(download_url + "\r\n")
    pass


def parser(param):
    page_url = "http://android.myapp.com/myapp/detail.htm?apkName=" + param
    headers = {'User-Agent': "AndroidDownloadManager/4.1.1 (Linux; U; Android 4.1.1; Nexus S Build/JRO03E)"}

    resp = requests.get(page_url, headers=headers, timeout=30)
    # resp = requests.get(page_url, timeout=5)
    # resp= requests.get(page_url)

    # print("tx:" + resp.text)
    root = etree.HTML(resp.text)
    elem = root.xpath("//a[@class='det-down-btn']")
    download_url = None if None is elem or len(elem) == 0 else elem[0].attrib["data-apkurl"]
    print(u"[" + param + "] ===> " + download_url)
    # saveToFile(download_url)
    pass


if __name__ == '__main__':
    f = open(file, "r")
    text = f.read()
    arr = text.split("\n")
    print(len(arr))
    print(arr)
    for pkg in arr:
        # print("pkg:" + pkg)
        parser(pkg)
        # parser('com.taobao.live')
