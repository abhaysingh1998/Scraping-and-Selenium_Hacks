import requests
import random
from bs4 import BeautifulSoup
import urllib

url = "http://www.manutd.com/Splash-Page.aspx"

def download_all_images(ex_url):
    ex_text = requests.get(ex_url)
    text_str = ex_text.text
    soup = BeautifulSoup(text_str, "lxml")

    for links in soup.find_all('img'):
        image = links.get('src')
        image_final = "http://www.manutd.com/" + image
        name = random.randrange(1,1000)
        full_name = str(name) + ".jpg"

        urllib.urlretrieve(image_final , full_name)

download_all_images(url)
