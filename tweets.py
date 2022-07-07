import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:SirajOfficial) until:2022-06-16 since:2006-01-01"

tweets = []
limits = 20000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break
    if len(tweets) == limits:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
df = pd.DataFrame(tweets, columns=['Date', 'User','Tweet'])
print(df)
df.to_csv('sirajulhaqdataset.csv')