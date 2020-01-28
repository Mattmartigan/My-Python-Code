from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#import requests
import csv

class Scraper:
    def __init__(self):
        self.links = []
        self.products = {}

    def get_links(self):
            cat=input('Enter product category: ')
            strlst = cat.split()
            self.site=('https://www.macys.com/shop/search?cm_sp=navigation_mew--gn--search-n-n&keyword='+"%20".join(strlst))
            page = requests.get(self.site , headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(page.text, "html.parser")
            for tag in soup.find_all('a',{'class':'productDescLink'}):
                p = tag['href']
                self.links.append(p)
            i=0
            for link in self.links:
                i+=1
                self.site = 'http://macys.com'+link
                page = requests.get(self.site , headers={'User-Agent': 'Mozilla/5.0'})
                soup = BeautifulSoup(page.text, "html.parser")
                price = soup.find('div',{'class':'price'}).text
                price = price.strip()
                prod_description = soup.find('p',{'itemprop':'description'}).text
                prod_description = prod_description.strip()
                prod_name = soup.find('h1').text
                prod_name = prod_name.strip()
                prod = [price,prod_description]
                self.products[prod_name] = prod
                if i == 6:
                    break
            scrape.create_file()    
            print(self.products)

    def create_file(self):
        with open("sd.csv","w") as w:
            wr = csv.writer(w, delimiter = ';')
            p = self.products
            n = p.keys()
            m = p.values()
            r = []
            t = []
            for x in m:
                a = x[0]
                b = x[1]
                r.append(a)
                t.append(b)
            q = list(zip(n,r,t))
            wr.writerows(q)
    def search_file(self):
        sterms = input('Search file (enter search terms): ')
        sterms = sterms.split(" ")
        with open("sd.csv","r") as r:
            reader = csv.reader(r, delimiter = ';')
            for data in reader:
                for x in data:
                    for term in sterms:
                        if term in x:
                            print(data,'\n')
                        else:
                            print('Not Found')

scrape = Scraper()
scrape.get_links()
scrape.search_file()
