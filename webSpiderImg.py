import bs4
import requests

def demo(url):
    links = []
    header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0"}
    req = requests.get(url=url, headers=header)
    html = req.text
    # print(html)
    soup = bs4.BeautifulSoup(html, "html.parser")
    for link in soup.find_all("img"):
        l = link.get("src")
        if (l is not None) and (("http://" in l) or ("https://" in l)):

            # print(l)
            links.append(l)

    return links

def donwload(url):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0"}
    req = requests.get(url=url, headers=header)
    path = "image//" + url.split('/')[-1]
    open(path, "wb").write(req.content)

def main():
    # links = demo("https://baike.baidu.com/item/JVM/2902369?fr=aladdin")
    links = demo("https://blog.51cto.com/hui90877/2163265")
    for link in links:
        donwload(link)


if __name__ == '__main__':
    main()