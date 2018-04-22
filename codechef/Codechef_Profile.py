import requests
from bs4 import BeautifulSoup
import urllib2

type = ['Long', 'Short', 'LTime (All)']
rank = [ ]

def get_Details():

    x = raw_input("Enter the Username : ")
    url = "https://www.codechef.com/users/" + x
    user_file = urllib2.urlopen(url)
    user_html = user_file.read()
    user_file.close()

    soup = BeautifulSoup(user_html, 'html.parser')

    table = soup.find('table', attrs={'class': 'rating-table'}).find_all('hx')

    for i in table:
        rank.append(i.text)

    print "User Details"
    print "Long Challenge Rank : " + str(rank[0]) + " / " + str(rank[1])
    print "Short Challenge Rank : " + str(rank[2]) + " / " + str(rank[3])
    print "Lunchtime Challenge Rank : " + str(rank[4]) + " / " + str(rank[5])

get_Details()



