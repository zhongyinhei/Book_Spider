from bs4 import BeautifulSoup
from urllib import request


def get_notice_content(href):
    response = request.urlopen(href)
    content = response.read()
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    content = soup.find('div', class_="content-article")
    title = soup.find('p', class_="tit content-tit").text
    final_data = {'title': title,
                  'content': str(content)}
    return final_data


class Main(object):
    pass
