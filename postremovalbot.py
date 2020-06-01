import praw
from configparser import ConfigParser
import requests
import json
import time

class PostRemovalBot():
    def __init__(self):
        self.user_agent = "PostRemovalBot / V1.3 by ScoopJr"
        print('Starting up...', self.user_agent)
        CONFIG = ConfigParser()
        CONFIG.read('config.ini')
        self.user = CONFIG.get('main', 'USER')
        self.password = CONFIG.get('main', 'PASSWORD')
        self.client = CONFIG.get('main', 'CLIENT_ID')
        self.secret = CONFIG.get('main', 'SECRET')
        self.subreddit = CONFIG.get('main', 'SUBREDDIT')
        #self.type = CONFIG.get('main', 'TYPE')
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
        self.header = CONFIG.get('MSG', 'HEADER')
        self.footer = CONFIG.get('MSG', 'FOOTER')
        self.footer2 = CONFIG.get('MSG', 'FOOTER2')

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

    def format_removal_message(self, author_name, removal_reason):
        try:
            header = self.header.format(author=author_name)
            message = str(header + "\n\n" + removal_reason + "\n\n" + self.footer + "\n\n" + self.footer2)
        except author_name or removal_reason is None:
            print("You must specify a removal reason or author name!")
        return message

    def main(self):
        while True:
            print("...Searching for the correct post flairs!")
            for post in self.reddit.subreddit(self.subreddit).stream.submissions(pause_after=1):
                if post is None:
                    break
                if post.link_flair_text in self.keys:
                    post.mod.remove(mod_note=str(self.flair_and_reason[post.link_flair_text])) # Removes bot with removal reason found in removalreasons.json
                    msg = self.format_removal_message(author_name=post.author.name, removal_reason=self.flair_and_reason[post.link_flair_text])
                    post.mod.send_removal_message(msg, type=self.type) # Lets user know why the bot was removed
                    print(f"Removed: {post.name}")
            print(f"...Taking a small break!  Be back in {self.delay} seconds")
            time.sleep(self.delay)




if __name__ == "__main__":
    bot = PostRemovalBot()
    bot.main()