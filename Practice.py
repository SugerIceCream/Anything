import requests
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

def main():
    url = "https://python123.io/ws/demo.html"
    demo = Requests(url)
    beautiful(demo)

if __name__ == "__main__":
    main()