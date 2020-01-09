import re
import bs4
import requests
from bs4 import BeautifulSoup

#尝试爬取最好大学网中的排名

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def putItAdjust(List, demo):
    soup = BeautifulSoup(demo,"html.parser")
    #观察所需提取信息的源代码
    for son in soup.find('tbody').children:#将tbody下的所有子节点都遍历出来
        if isinstance(son, bs4.element.Tag):#检测son的类型是否为element中的Tag标签类型，如果是则执行if语句
            trTag = son.find_all('td')
            List.append([trTag[0].string, trTag[1].string, trTag[3].string])
    return List
            #之所以最后一个数组序号为3是因为2为该网址中的省份信息并非排名，.string是为了提取其中的字符串属性


def ShowList(List, num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名','学校名称','总分'))
    #{:^10}表示取10位居中对齐，共10格宽，^为居中对齐，\t为横向制表字符串
    for i in (range(num)):
        u = List[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))
        #注意此处最后一个下标应为2
        
def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    List = []
    demo = getHTMLText(url)
    List = putItAdjust(List, demo)
    ShowList(List, 20)
    
if __name__ == "__main__":
    main()

