from bs4 import BeautifulSoup
from urllib import request
import time
import re

class Main(object) :
   def get_hotbook(self):
       page_url = 'http://202.198.14.5:8080/top/top_book.php'
       response = request.urlopen(page_url)
       content = response.read()
       soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
       content2 = soup.find('table', class_ = 'table_line')
       return_list = []
       for i in range(1,int(len(content2)/2)):
           index = i*2+1
           content4 = content2.contents[index].find_all('td')
           temp_list = {}
           temp_list['id'] = content4[1].find('a')['href'].strip('../opac/item.php?marc_no=')
           temp_list['book_name'] = content4[1].find('a').text
           temp_list['book_author'] = content4[2].text
           temp_list['book_publisher'] = content4[3].text
           temp_list['book_find'] = content4[4].text
           temp_list['book_num'] = content4[5].text
           #print(temp_list)
           return_list.append(temp_list)
       return return_list
