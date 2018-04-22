import urllib
import random

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.urlretrieve(url, full_name)

download_image("http://www.ozassignmenthelp.com.au/wp-content/uploads/2013/07/python-programming-assignment-help.png")