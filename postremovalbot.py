import praw
from configparser import ConfigParser
import requests
import json
import time

class PostRemovalBot():
    def __init__(self):
        self.user_agent = "PostRemovalBot / V1.1 by ScoopJr"
        print('Starting up...', self.user_agent)
        CONFIG = ConfigParser()
        CONFIG.read('config.ini')
        self.user = CONFIG.get('main', 'USER')
        self.password = CONFIG.get('main', 'PASSWORD')
        self.client = CONFIG.get('main', 'CLIENT_ID')
        self.secret = CONFIG.get('main', 'SECRET')
        self.subreddit = CONFIG.get('main', 'SUBREDDIT')
        self.type = CONFIG.get('main', 'TYPE')
        self.type = "public"
        self.token_url = "https://www.reddit.com/api/v1/access_token"
        self.token = ""
        self.t_type = ""
        self.flair_and_reason = None
        self.delay = CONFIG.getint('main', 'DELAY_BETWEEN_RUNS')
        self.reddit = praw.Reddit(client_id=self.client,
                                  client_secret=self.secret,
                                  password=self.password,
                                  user_agent=self.user_agent,
                                  username=self.user)
        self.get_json_file()
        self.keys = self.flair_and_reason.keys()

    def get_json_file(self):
        """Gets removal reason json file"""
        try:
            with open("removalreasons.json", "r") as f:
                self.flair_and_reason = json.loads(f.read())
        except FileNotFoundError:
            print("removalreasons.json could not be found!")

    def get_token(self):
        """ Retrieves token for Reddit API."""
        client_auth = requests.auth.HTTPBasicAuth(self.client, self.secret)
        post_data = {'grant_type': 'password', 'username': self.user, 'password': self.password}
        headers = {'User-Agent': self.user_agent}
        response = requests.Session()
        response2 = response.post(self.token_url, auth=client_auth, data=post_data, headers=headers)
        self.token = response2.json()['access_token']
        self.t_type = response2.json()['token_type']


    def main(self):
        while True:
            print("...Searching for the correct post flairs!")
            for post in self.reddit.subreddit(self.subreddit).stream.submissions(pause_after=1):
                if post is None:
                    break
                if post.link_flair_text in self.keys:
                    post.mod.remove()
                    post.mod.send_removal_message(self.flair_and_reason[post.link_flair_text], type=self.type)
                    print(f"Removed: {post.name}")
            print(f"...Taking a small break!  Be back in {self.delay} seconds")
            time.sleep(self.delay)




if __name__ == "__main__":
    bot = PostRemovalBot()
    bot.main()