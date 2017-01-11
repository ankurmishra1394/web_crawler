import urllib2  
from bs4 import BeautifulSoup

quote_page = 'http://www.firstpost.com/'
page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('div', attrs={'class': 'section-body trending-news'})
for y in name_box.find_all(["a","img"]):
    w = y
    print w, w.text.strip()
    print "-------------"
