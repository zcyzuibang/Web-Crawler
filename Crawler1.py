#作者：张长宇 
#功能：实现爬取顶点小说网小说《大道朝天》前165章，并保存在文件“大道朝天.txt”中 
#日期：2018.04.05   

import re
import requests
from bs4 import BeautifulSoup

def GetHtmltext(url):
    try:
        r=requests.get(url,timeout=20)
        r.encoding=r.apparent_encoding
        r.raise_for_status()
        return r.text
    except:
        print ('requests error')

if __name__=='__main__':
    file = open('大道朝天.txt', 'w', encoding='utf-8')
    root_url='http://www.ddxs.cc'
    url='/ddxs/1/617768.html'
    x=0
    t='html'
    while x<165:
        count = 0
        now_url='%s%s' % (root_url, url,)
        print (now_url)
        html=GetHtmltext(now_url)
        soup=BeautifulSoup(html,'html.parser')
        for i in soup.find_all("h1") :
            file.writelines(i)
        file.write('\n')
        file.write('\n')
        file.write('\n')
        for j in soup.find_all(id='content') :
            dr = re.compile(r'<[^>]+>',re.S)
            dd = dr.sub('',str(j))
            file.writelines(str(dd))
        file.write('\n')
        file.write('\n')
        file.write('\n')
        for i in soup.find_all('a'):
            str_str=str(i.get('href'))
            if str_str.find(t)!=-1:
                count += 1
                if count==2:
                    url=str_str
            else:
                continue
        x+=1
    file.close()