import requests
import re
import getInformation
from bs4 import BeautifulSoup

def Requests(url):
    try:
        r = requests.get(url)#通过requests的get方法来爬取url地址的内容
        r.raise_for_status()#若返回不是200，则会产生异常
        r.encoding = r.apparent_encoding#原本的相应内容编码方式转变成我们能阅读的编码
        return r.text
    except:
        return "产生异常"

def beautiful(demo):
    soup = BeautifulSoup(demo, "html.parser")#将爬取到的初级文本通过BeautifulSoup来重新调整一下
    print("=============")
    print(soup.prettify())#prettify()方法是辅助于阅读爬取的数据格式
    print("=============")
    return soup

def GetName(soup):
    print('下行遍历的所有结点的名字：\n')
    for son in soup.html.descendants:
        if son is None:
            print(son)
        else:
            print(son.name)

    print('上行遍历的所有结点的名字：\n')
    for Parents in soup.a.parents:
        if Parents is None:
            print(Parents)
        else:
            print(Parents.name)

    print('平行遍历的本身：\n')
    for itself in soup.a:
        print(itself)#遍历的结果并非都是标签类型，也可能是NavigableString类型(标签非属性字符)
    print('平行遍历且为后续遍历的所有结点内容：\n')
    for nextbother in soup.a.next_siblings:
        print(nextbother)
    print('平行遍历且为前续遍历的所有结点内容：\n')
    for previousbother in soup.a.previous_siblings:
        print(previousbother)

def main():
    url = "https://python123.io/ws/demo.html"
    demo = Requests(url)
    soup = beautiful(demo)
    GetName(soup)
    getInformation.InformationGet(soup)

if __name__ == "__main__":
    main()