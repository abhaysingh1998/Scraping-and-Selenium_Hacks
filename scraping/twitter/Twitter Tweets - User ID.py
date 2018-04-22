import twitter

c_key = "Consumer Key"
c_secret = "Consumer Secret Key"
a_key = "Access Key"
a_secret = "Access Secret Key"


def get_tweets(user_id):
    api = twitter.Api(consumer_key=c_key, consumer_secret=c_secret, access_token_key=a_key,
                      access_token_secret=a_secret)

    # print api.VerifyCredentials()

    l = []
    t = api.GetUserTimeline(user_id=user_id, count=25)
    # print t
    tweets = [i.AsDict() for i in t]

    for i in tweets :
        l.append(i['text'])

    print l


ID = raw_input("Enter the user ID : ")
get_tweets(ID)

