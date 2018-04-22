import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib2

url1 = "http://www.espncricinfo.com/ci/engine/match/index.html?view=live"

# Function begins
def view_score():
    cric_file = urllib2.urlopen(url1)
    cric_html = cric_file.read()
    cric_file.close()

    soup = BeautifulSoup(cric_html, 'html.parser')

    #print soup

    a = soup.find_all('div', attrs={'class': 'innings-info-1'})
    b = soup.find_all('div', attrs={'class': 'innings-info-2'})
    c = soup.find_all('div', attrs={'class': 'match-status'})

    output1 = []
    output2 = []
    output3 = []

    for results in a:
        output1.append(results.text)

    for results in b:
        output2.append(results.text)

    for results in c:
        output3.append(results.text)

    # Strip Characters
    output1 = map(lambda s: s.strip(), output1)
    output2 = map(lambda s: s.strip(), output2)
    output3 = map(lambda s: s.strip(), output3)

    df = pd.DataFrame(columns={"Team 1", "Team 2", "Status"})
    df["Team 1"] = pd.Series(output1)
    df["Team 2"] = pd.Series(output2)
    df["Status"] = pd.Series(output3)

    print df

view_score()
