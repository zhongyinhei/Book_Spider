from bs4 import BeautifulSoup
from urllib import request
import time
import re

class Main(object) :
   def get_notice_list(self,page):
       url = "http://lib.neepu.edu.cn/list.php?fid=6&page="+page
       response = request.urlopen(url)
       content = response.read()
       soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
       content = soup.find('ul', class_="sarae")
       content2 = content.find_all('li')
       sum_list = []
       for i in range(0, len(content2)):
           value = content2[i].find('a')
           value2 = content2[i].find('span')
           temp_list = {}
           temp_list['title'] = value['title']
           temp_list['href'] = "http://lib.neepu.edu.cn/" + value['href']
           temp_list['date'] = value2.text[6:16]
           sum_list.append(temp_list)
       return sum_list