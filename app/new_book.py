from bs4 import BeautifulSoup
from urllib import request
import time
import re

class Main(object) :
   def get_newbook(self,page):
    url = 'http://202.198.14.5:8080/newbook/newbook_cls_book.php?back_days=15&loca_code=ALL&cls=ALL&s_doctype=ALL&clsname=%E5%85%A8%E9%83%A8%E6%96%B0%E4%B9%A6&page='+page
    r = request.urlopen(url)
    content = r.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    newbook = soup.find_all('div',class_='list_books')
    listsum = []
    for i in newbook:
        list_info = {}
        list_info['book_name'] = i.find('strong').text
        list_info['book_info'] = i.find('p').text.strip()
        book_id = i.find('span')['id'].strip('info_')
        list_info['book_id'] = book_id
        timenow = time.time()
        timestr = int(timenow)
        url2 = 'http://202.198.14.5:8080/opac/ajax_lend_avl.php?marc_no=' + book_id + '&time=' + str(timestr)
        content_time = request.urlopen(url2)
        r = content_time.read()
        strr = str(r, encoding="utf-8")
        res_tr = r'<b>(.*?)</b>'
        list_info['book_num'] = re.findall (res_tr, strr, re.S | re.M)
        listsum.append(list_info)
    return listsum
