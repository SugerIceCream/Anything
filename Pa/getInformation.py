import re
def InformationGet(soup):#信息提取可最佳方案：形式解析(遍历方法) + 搜索方法(类似于find_all与正则)

    def First():
        print(soup.find_all('a'))#该项会输出搜索方法找到a的所有标签
        print('\n#################\n')
        for Name in soup.find_all(True):#该项会输出所有标签名，去掉.name后就是会显示整体信息
            print(Name.name)
        print('\n#################\n')
    
    def Second():
        for About_all_a in soup.find_all(re.compile('a')):#该项会输出搜素方法找到的包含a字母的所有标签，也就是为什么会输出head标签
            print(About_all_a)
        print('\n#################\n')
        for About_all_p in soup.find_all(re.compile('p')):
            print(About_all_p)
        print('\n#################\n')

    def Third():
        for About_all_link1 in soup.find_all('a', id='link1'):#该项会输出搜索方法找到的a标签下且名为id的属性的信息内容
            print(About_all_link1)
        print('\n#################\n')
        for About_all_link2 in soup.find_all('a', id='link2'):
            print(About_all_link2)
        print('\n#################\n')

    def Fourth():
        for Father in soup.find_all('p'):
            print(Father)
        print('\n#################\n')
        for Find_all_children1 in soup.find_all('p',recursive=False):
            print(Find_all_children)#返回空值表示在soup结点上的下一位结点中没有名为p的标签
        print('\n#################\n')
        for Find_all_children2 in soup.find_all('html',recursive=False):
            print(Find_all_children2)#由于soup的下一个结点为html，所以会返回html的内容信息，recursive表示一个是否要随之继续遍历后续标签节点的开关
        print('\n#################\n')

    def Fifth():
        print(soup.find_all(string='Advanced Python'))#string用法为输入查找非属性字符串的内容信息，看看是否有返回，注意s小写
        print(soup.find_all(string=re.compile('python')))#正则表达式则是搜索所有非属性字符串中包含python的语句

    First()
    Second()
    Third()
    Fourth()
    Fifth()