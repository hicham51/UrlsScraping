from selenium import webdriver
from bs4 import BeautifulSoup

urls = []

def scrape(site):
    driver = webdriver.Chrome('chromedriver.exe')  # تحديد مسار ملف تنفيذ ChromeDriver
    driver.get(site)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    for i in soup.find_all("a"):
        if 'href' in i.attrs:
            href = i.attrs['href']
            urls.append(href)
            print(href)
    
    driver.quit()

if __name__ == "__main__":
    site = input('Enter your site: ')
    scrape(site)
