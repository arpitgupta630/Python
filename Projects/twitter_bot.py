import tweepy

auth = tweepy.OAuthHandler('wHn0v65qHJjFttAPgUOewPp4X', 'eNQqIVDvSaFlUYQuUGmxgw4sfwq1zEXyD8XV61QffOf5jWJMb6')
auth.set_access_token('751016783772000256-XasVos0AmrecZYzdDXxfFpfsxE3pIcF', 'TEsWznkDF9Q4nzmXtvjoTzfJ6FUvX0YMyW4FvdkmkFX8P')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)