from twython import Twython

def twitterr():

    TWITTER_APP_KEY = ''
    TWITTER_APP_KEY_SECRET = ''
    TWITTER_ACCESS_TOKEN = ''
    TWITTER_ACCESS_TOKEN_SECRET =''
    my_tweet = Twython(app_key=TWITTER_APP_KEY,
                app_secret=TWITTER_APP_KEY_SECRET,
                oauth_token=TWITTER_ACCESS_TOKEN,
                oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)



    search = my_tweet.search(q='#pycon2019',count=1000)
    tweets = search['statuses']
    no=1
    for tweet in tweets:
        tweet_list=tweet['text']
        print ("Tweet: ",no,"-->",end="")
        print(tweet_list,end="\n\n")
        no+=1
twitterr()
