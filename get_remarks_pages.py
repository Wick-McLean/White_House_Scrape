# import requests
# from bs4 import BeautifulSoup
# import lxml

def get_remarks_urls(soup):
    mylist = []
    for url2 in soup.find_all('h2', {'class': 'briefing-statement__title'}):
        mylist.append(url2.find('a'))
    return mylist

def make_file(rawlist):
    content = []
    for url in rawlist:
        content.append(url)
    return content

def save_to_file(mylist1):
    with open('speech_list.txt', "w") as f:
        for url in mylist1:
            f.writelines(str(url) + '\n')
    f.close()
