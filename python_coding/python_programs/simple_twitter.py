class Twitter:
    '''defining class variables. user and tweet and incremental variables. user hash has details on every user created'''

    user = 1
    user_hash = {}
    tweet = 1

    def __init__(self):
        '''Initialization of user by assigning userId and adding them to user_hash'''
        self.userId = Twitter.user
        Twitter.user_hash[self.userId] = {"tweets" : [] ,"follow" : []}
        Twitter.user += 1

    def postTweet(self):
        '''New tweet posted added to user_hash'''
        Twitter.user_hash[self.userId] ["tweets"].append(Twitter.tweet)
        Twitter.tweet += 1

    def getNewsFeed(self):
        '''Printing the last 10 tweets by a user'''
        num_tweets = len(Twitter.user_hash[self.userId]["tweets"])
        print('Tweets from userId '+str(self.userId)+' are :')
        for i in range(num_tweets-1 , num_tweets-11 , -1) :
            if i >= 0:
                print('Tweet Id :'+str(Twitter.user_hash[self.userId]["tweets"][i]))

    def follow(self,followeeId):
        '''Adding whom the userid whom the user starts following'''
        Twitter.user_hash[self.userId]['follow'].append(followeeId.userId)
        print(str('UserId '+str(self.userId)+' now follows UserId '+str(followeeId.userId)))

    def unfollow(self, followeeId):
        '''removing whom the userid whom the user starts unfollowing'''
        Twitter.user_hash[self.userId]['follow'].remove(followeeId.userId)
        print(str('UserId '+str(self.userId)+' now unfollows UserId '+str(followeeId.userId)))

# Creating the users
obj1 = Twitter()
obj2 = Twitter()
obj3 = Twitter()

# posting the tweets
obj1.postTweet()
obj2.postTweet()
obj1.postTweet()
obj3.postTweet()
obj2.postTweet()
obj1.postTweet()

# Generating news feed for last 10 tweets by users
obj1.getNewsFeed()
obj2.getNewsFeed()
obj3.getNewsFeed()

# Users follows
obj1.follow(obj2)
obj2.follow(obj3)
obj1.follow(obj3)

# Users unfollows
obj1.unfollow(obj2)
