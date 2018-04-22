import tweepy

c_key = "Consumer Key"
c_secret = "Consumer Secret Key"
a_key = "Access Key"
a_secret = "Access Secret Key"


def get_tweets(text):
    OAUTH_KEYS = {'consumer_key': c_key, 'consumer_secret': c_secret,
                  'access_token_key': a_key, 'access_token_secret': a_secret}
    auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
    api = tweepy.API(auth)

    t = tweepy.Cursor(api.search, q=text).items(25)
    l = []

    for i in t:
        l.append(i.text)

    print l


t = raw_input("Enter the text : ")
get_tweets(t)