from bs4 import BeautifulSoup
from urllib import request
import time
import re

class Main(object) :
   def get_notice_content(self,href):
       response = request.urlopen(href)
       content = response.read()
       soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
       content = soup.find('div', class_="content-article")
       title = soup.find('p', class_="tit content-tit").text
       final_data = {}
       final_data['title'] = title
       final_data['content'] = str(content)
       return final_data