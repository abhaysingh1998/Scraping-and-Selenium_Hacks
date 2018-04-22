import requests
from bs4 import BeautifulSoup
import urllib2

def get_Details():
    url = "https://www.codechef.com/contests"
    contest_file = urllib2.urlopen(url)
    contest_html = contest_file.read()
    contest_file.close()

    soup = BeautifulSoup(contest_html, 'html.parser')

    table = soup.find('table', attrs={'class': 'dataTable'})

    c_li = []

    for links in table.find("tbody").find_all("a"):
        c_li.append(links.string)

    print("Following are the Live Contests going on ryt now . Do Take part . They're GOOD ^_^")

    for i in c_li:
        print(i)

get_Details()

