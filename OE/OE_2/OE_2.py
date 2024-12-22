class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        return f"{self.username} logged in successfully"
    
    def post(self):
        return f"{self.username} created a post"

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, followers=0):
        super().__init__(username, password)
        self.followers = followers
    
    def share_story(self):
        return f"{self.username} shared an Instagram story"

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, tweets=0):
        super().__init__(username, password)
        self.tweets = tweets
    
    def tweet(self):
        self.tweets += 1
        return f"{self.username} posted a tweet"


if __name__ == "__main__":
    
    insta = InstagramAccount("user1", "pass123", 1000)
    twitter = TwitterAccount("user1", "pass123")
    
    
    print(insta.login())  
    print(insta.share_story())  
    print(twitter.login())  
    print(twitter.tweet()) 