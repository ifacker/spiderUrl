import bs4
import requests

def demo(url):
    listLink = []
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0"}
    req = requests.get(url=url, headers=header)
    # req.encoding = 'gb2312'
    html = req.text
    # print(html)
    soup = bs4.BeautifulSoup(html, "html.parser")
    # print(soup)
    for link in soup.find_all('a'):
        l = link.get("href")
        if (l is not None) and ('http' in l) :
            listLink.append(l)
    for link in listLink:
        print(link)

def main():
    # demo("http://www.hmc68.com")
    # demo("https://www.baidu.com")
    # demo("https://blog.csdn.net/qq_38412868/article/details/82080260")
    demo("https://jingyan.baidu.com/article/358570f6232a648e4624fc18.html")

if __name__ == '__main__':
    main()