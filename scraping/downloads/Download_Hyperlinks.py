import requests
from bs4 import BeautifulSoup
import urllib

url = "https://www.google.co.in/"

#Function Begins
def download_links(ex_url):
    ex_text = requests.get(ex_url)
    text_str = ex_text.text

    soup = BeautifulSoup(text_str , "lxml")

    dest_url = r'links.txt'
    fx = open(dest_url, "w")

    for links in soup.find_all('a'):
        anchor = links.get('href')
        fx.write(str(anchor) + "\n")

    fx.close()
#Function Ends

download_links(url)