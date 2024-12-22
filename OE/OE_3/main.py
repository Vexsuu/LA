class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, followers):
        super().__init__(username, password)
        self.followers = followers


user1 = TwitterAccount("tweet_user", "pass123", 100)


print(f"Username: {user1.username}")
print(f"Number of followers: {user1.followers}")