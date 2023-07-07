from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

urls = []
clien = requests.session()

def scrape(site):
    r = clien.get(site)
    s = BeautifulSoup(r.text, "lxml")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if 'href' in i.attrs:
            href = i.attrs['href']
            urls.append(href)
            print(href)
            if href.startswith("/"):
                site = urljoin(site, href)
                if site not in urls:
                    urls.append(site)
                    print(site)
                    scrape(site)

if __name__ == "__main__":
    site = input('Enter your site: ')
    scrape(site)
