from twython import Twython

def twitterr():

    TWITTER_APP_KEY = 'dVMuFQ9GxaUlleLVLPFJ83Vmk'
    TWITTER_APP_KEY_SECRET = 'hHY53TTowtMKlJLoif5kzknWCMVDnHMac4ApXMeFRvMV3T3eiW'
    TWITTER_ACCESS_TOKEN = '1036648680382578688-BvXPbrGch9c1aoITr9wFc99G1rajYU'
    TWITTER_ACCESS_TOKEN_SECRET ='1Wi4fzRB6kKnnlPNk2BbbjR5Ya3DvFu4k0yR78ZCGq7V8'
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
