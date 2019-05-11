import requests

from bs4 import BeautifulSoup

def crawl_page(max_pages,set1,keyword):

    page = 1

    while page <= max_pages:
        url = 'https://www.w3schools.com/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.findAll('a' ,{'class':"w3-bar-item w3-button"}):
            href = 'https://www.w3schools.com' + link.get('href')
            if is_link(href, keyword) == 1:
                set1.add(href)
        set1.discard(' ')
        non_repeated_list = list(set(set1))
        for items in non_repeated_list:
            crawl_link(items,keyword,set1)
        page = page + 1

def crawl_link(url,keyword,set1):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('a', {'target': "_top"}):
        if keyword == "javascript":
            href = 'https://www.w3schools.com/' + "js/" + link.get('href')
        else:
            href = 'https://www.w3schools.com/' +keyword.lower()+"/"+ link.get('href')
        if is_link(href, keyword) == 1:
            set1.add(href)


def is_link(url_add, keyword):

    source_code = requests.get(url_add)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    strng1 = soup.get_text()
    strng2=str(strng1)
    strng2=strng2.lower()
    strng = strng2.split()
    for word in strng:
        if word == keyword:
            return 1
        else:
            return 0
def c(line_final):
    line_final2 = line_final.split()
    for text in line_final2:
        if text == 'Home' or text=='Previous':
            return 1


def download(url, title):
    count = 1
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    dest_file = title + ".txt"
    fx = open(dest_file, 'w',encoding="utf-8")
    for line in soup.find_all('body'):
        data = line.get_text()
        data = data.split("\n")
        for line_final in data:
            count = count + 1
            if count >= 268:
                if c(line_final) == 1:
                    break
                else:
                    fx.write(line_final+"\n")


    fx.close()

def main_():
    keyword = input("What do you want to search? Enter keyword: ")
    print("Fetching " + keyword + " links for you please wait for a few mins")
    keyword = keyword.lower()
    count=0
    set1={' '}
    crawl_page(1,set1,keyword)
    set1.discard(' ')
    non_repeated_list=list(set(set1))
    for items in non_repeated_list:
        count=count+1
        print(items +"\n")
        download(items, keyword + str(count))

main_()


		

		

