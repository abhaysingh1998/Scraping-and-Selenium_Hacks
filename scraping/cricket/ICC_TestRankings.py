import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import numpy as np

def getRanking():
    u = "http://www.espncricinfo.com/rankings/content/page/211271.html"
    rank_file = urllib2.urlopen(u)
    rank_html = rank_file.read()
    rank_file.close()

    soup = BeautifulSoup(rank_html, 'html.parser')

    data = []

    for table in soup.find_all('table'):
        for tr in table.find_all('tr'):
            row = []
            for td in tr.find_all('td'):
                row.append(td.get_text().encode("utf-8"))
            if len(row) == 4:
                data.append(row)
    print data

    Team = []
    for i in range(0,10):
        for j in range(0,1):
            Team.append(data[i][j])

    Matches = []
    for i in range(0,10):
        for j in range(1,2):
            Matches.append(data[i][j])

    Points = []
    for i in range(0,10):
        for j in range(2,3):
            Points.append(data[i][j])

    Rating = []
    for i in range(0,10):
        for j in range(3,4):
            Rating.append(data[i][j])

    df = pd.DataFrame(columns={"Team", "Matches", "Points", "Rating"})
    df["Team"] = Team
    df["Matches"] = Matches
    df["Points"] = Points
    df["Rating"] = Rating


getRanking()
