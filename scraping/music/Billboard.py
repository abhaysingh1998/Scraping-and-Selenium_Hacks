import requests
from bs4 import BeautifulSoup
import urllib2
import pandas as pd

def topSongs():
    url = "http://www.billboard.com/charts/hot-100"
    songs_file = urllib2.urlopen(url)
    songs_html = songs_file.read()
    songs_file.close()

    soup = BeautifulSoup(songs_html, 'html.parser')

    title = soup.find_all('div', attrs={'class' : 'chart-row__title'})

    rank = []
    song = []
    artist = []

    for i in range(1,101):
        rank.append(i)

    for i in title:
        head = i.find("h2")
        song.append(head.text)

    # for i in title:
    #     for anchor in i.find_all("a"):
    #         artist.append(anchor.text)

    # print rank
    # print song

    # artist = map(lambda s: s.strip(), artist)

    df = pd.DataFrame(columns={"Rank", "Song"})
    df["Rank"] = rank
    df["Song"] = song

    print df


topSongs()