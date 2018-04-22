from bs4 import BeautifulSoup
import urllib2

def getlyrics():
    artist = raw_input("Enter the name of the artist : ")
    artist = artist.lower()
    song = raw_input("Enter the name of the song : ")
    song = song.lower()
    url = "http://www.azlyrics.com/lyrics/" + artist + "/" + song + ".html"

    # add header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    request = urllib2.Request(url, headers = headers)
    lyrics_file = urllib2.urlopen(request)
    lyrics_html = lyrics_file.read()
    lyrics_file.close()

    soup = BeautifulSoup(lyrics_html, 'html.parser')

    l = []

    for div in soup.find_all('div', attrs={'class':'col-xs-12 col-lg-8 text-center'}):
        for sub_div in div.find_all('div'):
            l.append(sub_div.text)

    l = map(lambda s: s.strip(), l)

    print "\nLyrics" + "\n"
    print l[6]

getlyrics()