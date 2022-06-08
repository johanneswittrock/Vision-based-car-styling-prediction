from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from pathlib import Path
from PIL import Image
import io
import requests
import hashlib

results = []

def scrape(req):
#    results = []
    htmldata = urlopen(req)
    soup = BeautifulSoup(htmldata, 'html.parser')
    for a in soup.findAll(attrs={'class': "item"}):
        name = a.find("img")
        if name not in results:
            results.append(name.get("src"))

def scrapeLargeCars():
    i = 1
#    results = []
    while i <= 12:
        if i == 1:
            req = Request('https://www.thecarconnection.com/category/new,large', headers={'User-Agent': 'Mozilla/5.0'})
        else:
            req = Request('https://www.thecarconnection.com/category/new,large_' + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        #results.append(scrape(req))
        scrape(req)
        i += 1

def scrapeMidSizeCars():
    i = 1
#    results = []
    while i <= 18:
        if i == 1:
            req = Request('https://www.thecarconnection.com/category/new,mid-size', headers={'User-Agent': 'Mozilla/5.0'})
        else:
            req = Request('https://www.thecarconnection.com/category/new,mid-size_' + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        #results.append(scrape(req))
        scrape(req)
        i += 1

def scrapeSmallCars():
    i = 1
#    results = []
    while i <= 16:
        if i == 1:
            req = Request('https://www.thecarconnection.com/category/new,compact', headers={'User-Agent': 'Mozilla/5.0'})
        else:
            req = Request('https://www.thecarconnection.com/category/new,compact_' + str(i), headers={'User-Agent': 'Mozilla/5.0'})
        #results.append(scrape(req))
        scrape(req)
        i += 1


#def parse_image_urls(classes, location, source):
#    for a in soup.findAll(attrs={'class': classes}):
#        name = a.find(location)
#        if name not in results:
#            results.append(name.get(source))
#    return results

scrapeLargeCars()
scrapeMidSizeCars()
scrapeSmallCars()

for b in results:
    image_content = requests.get(b).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('RGB')
    file_path = Path('pictures', hashlib.sha1(image_content).hexdigest()[:10] + '.png')
    image.save(file_path, "PNG", quality=80)

#https://oxylabs.io/blog/scrape-images-from-website