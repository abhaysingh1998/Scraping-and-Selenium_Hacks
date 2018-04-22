from bs4 import BeautifulSoup
import urllib2
import pandas as pd


def getRankings():
    url = "https://en.wikipedia.org/wiki/ICC_Player_Rankings#Top_10_Test_Batsmen"
    rank_file = urllib2.urlopen(url)
    rank_html = rank_file.read()
    rank_file.close()

    soup = BeautifulSoup(rank_html, "html.parser")

    data = []

    for table in soup.find_all('table', attrs={'class':'multicol'}):
        for td in table.find_all('td', attrs={'style' : 'width: 33.33%;text-align:left;vertical-align:top;'}):
            for table in td.find_all('table', attrs={'class':'wikitable'}):
                for tr in table.find_all('tr'):
                    row =[]
                    for td in tr.find_all('td'):
                        row.append(td.get_text().encode("utf-8"))
                    if len(row) == 3:
                        data.append(row)

    rank = []
    for i in range(0, 10):
        rank.append(i+1)

    # ---------------- Batsmen --------------------#
    test_batsmen_name = []
    for i in range(0,10):
        test_batsmen_name.append(data[i][1])

    test_batsmen_rating= []
    for i in range(0,10):
        test_batsmen_rating.append(data[i][2])

    sequence = ["Rank", "Player", "Rating"]
    df_bt = pd.DataFrame()
    df_bt = df_bt.reindex(columns=sequence)
    df_bt["Rank"] = rank
    df_bt["Player"] = test_batsmen_name
    df_bt["Rating"] = test_batsmen_rating

    # ---------------- Bowlers --------------------#
    test_bowler_name = []
    for i in range(10, 20):
        test_bowler_name.append(data[i][1])

    test_bowler_rating = []
    for i in range(10, 20):
        test_bowler_rating.append(data[i][2])

    sequence = ["Rank", "Player", "Rating"]
    df_bo = pd.DataFrame()
    df_bo = df_bo.reindex(columns=sequence)
    df_bo["Rank"] = rank
    df_bo["Player"] = test_bowler_name
    df_bo["Rating"] = test_bowler_rating

    # ---------------- All-Rounders--------------------#
    test_all_name = []
    for i in range(20, 30):
        test_all_name.append(data[i][1])

    test_all_rating = []
    for i in range(20, 30):
        test_all_rating.append(data[i][2])

    sequence = ["Rank", "Player", "Rating"]
    df_ar = pd.DataFrame()
    df_ar = df_ar.reindex(columns=sequence)
    df_ar["Rank"] = rank
    df_ar["Player"] = test_all_name
    df_ar["Rating"] = test_all_rating

    print "Top 10 Test Batsmen"
    print df_bt

    print "\nTop 10 Test Bowlers"
    print df_bo

    print "\nTop 10 Test All-Rounders"
    print df_ar


getRankings()
