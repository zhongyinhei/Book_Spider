from bs4 import BeautifulSoup
from urllib import request
import urllib
import string
from urllib import parse

from app import app


def get_json(list1, list2):
    listn = []
    for i in range(0, len(list1)):
        jsonlist = {}
        temp_name = list1[i][0].split('.', 1)
        if len(temp_name[1]) > 15:
            jsonlist['name'] = temp_name[1][0:13] + "..."
        else:
            jsonlist['name'] = temp_name[1]
        jsonlist['num'] = temp_name[0]
        jsonlist['idd'] = list1[i][1]
        jsonlist['sum'] = list2[i][0]
        jsonlist['avi'] = list2[i][1]
        jsonlist['pub_year'] = list2[i][2]
        listn.append(jsonlist)
    return listn


def get_content(book):
    full_url = 'http://202.198.14.5:8080/opac/openlink.php?historyCount=1&strText=c语言&doctype=ALL&strSearchType=title' \
               '&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL '
    # book = input()
    half_url = "openlink.php?historyCount=1&strText=" + book + "&doctype=ALL&strSearchType=title&match_flag=forward" \
                                                               "&displaypg=20&sort=CATA_DATE&orderby=desc&showmode" \
                                                               "=list&dept=ALL "
    url = parse.urljoin(full_url, half_url)
    link = urllib.parse.quote(url, safe=string.printable)
    response = request.urlopen(link)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup


def get_numpage(book, pagenum):
    full_url = 'http://202.198.14.5:8080/opac/openlink.php?historyCount=1&strText=c语言&doctype=ALL&strSearchType=title' \
               '&match_flag=forward&displaypg=20&sort=CATA_DATE&orderby=desc&showmode=list&dept=ALL '
    # book = input()
    half_url = "openlink.php?historyCount=1&strText=" + book + "&doctype=ALL&strSearchType=title&match_flag=forward" \
                                                               "&displaypg=20&sort=CATA_DATE&orderby=desc&showmode" \
                                                               "=list&dept=ALL&page=" + pagenum
    url = parse.urljoin(full_url, half_url)
    link = urllib.parse.quote(url, safe=string.printable)
    response = request.urlopen(link)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup


def get_booklist(soup):
    content2 = soup.find_all('h3')
    list4 = []
    for i in range(0, len(content2)):
        list3 = []
        value = content2[i].find('a').text
        value2 = content2[i].find('a')
        key = value2['href']
        list3.append(value)
        list3.append(key)
        list4.append(list3)
    return list4


def get_booklistdetail(soup):
    content3 = soup.find('ol', id='search_book_list')
    lists = []
    if content3 is not None:
        for i in range(0, len(content3)):
            temp_list = []
            if i % 2 == 1:
                a2 = (content3.contents[i].find('p'))
                b2 = a2.text
                c3 = b2.split(' ')
                temp_list.append(c3[1])
                temp_list.append(c3[44])
                temp_list.append(c3[len(c3) - 4])
                lists.append(temp_list)
            else:
                continue
    else:
        lists.append("none")
    return lists


def get_index(list4):
    index = []
    for i in range(len(list4)):
        index.append(list4[i][1])
    # print(index)
    return index


def get_detail(remove):
    page_url = 'http://202.198.14.5:8080/opac/item.php?marc_no=0000241283'
    remove2 = "item.php?marc_no=" + remove
    # print(remove2)
    new_full_url = parse.urljoin(page_url, remove2)
    # print(new_full_url)
    response = request.urlopen(new_full_url)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    content5 = soup.find('div', id='item_detail')
    tempdic = {}
    for i in range(0, len(content5)):
        if content5.contents[i].find('dd') == -1 or content5.contents[i].find('dd') is None:
            continue
        else:
            temp = (content5.contents[i].find('dt'))
            temp2 = (content5.contents[i].find('dd'))
            tempdic[temp.get_text()] = temp2.get_text()
    tables = soup.findAll('table', id='item')
    tab = tables[0]
    cont = tab.findAll('tr')
    lists = []
    for i in range(1, len(tab.findAll('tr'))):
        temp_list = []
        for td in cont[i].find_all('td'):
            text = td.text
            text2 = text.split(' ')
            temp_list.append(text2)
        dic_book = {"ss_num": temp_list[0][0],
                    "tm_mun": temp_list[1][0],
                    "date": temp_list[2][0],
                    "location": temp_list[3][12],
                    "state": temp_list[4][0]}
        lists.append(dic_book)
    return_list = [lists, tempdic]
    return return_list


class main(object):
    pass
