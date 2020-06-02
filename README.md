# PostRemovalBot

### Description
Flair posts that break your rules and this bot will remove them and leave a comment

### Preqs
```
altgraph==0.17
certifi==2020.4.5.1
chardet==3.0.4
future==0.18.2
idna==2.9
pefile==2019.4.18
praw==7.0.0
prawcore==1.3.0
pywin32-ctypes==0.2.0
requests==2.23.0
six==1.15.0
update-checker==0.17
urllib3==1.25.9
websocket-client==0.57.0

```

```
python pip install requirements.txt
```
(Everything else included in Python library)

### Installing Python
* Download Python 3.7: https://www.python.org/downloads/release/python-370/
* Add Python to Path by selecting box during installation or manually adding to Path(https://datatofish.com/add-python-to-windows-path/)
* Open up Command Prompt and type "python", it should tell you the version if its installed correctly.

### Removal Flairs
* Go to your subreddit, www.reddit.com/r/subreddit 
* Select Mod Tools, near the "About Community" section
* Once inside Mod Tools, select Post flair in the Flairs & Emojis section
* In the top right, select Add Flair
* For flair text, put a unique rule name.  In our case, our flair text is, Rule1
* In flair settings, select Mod Only and select Save

*Repeat for every rule you want to add.  Please remember the "flair text" for later!*

*My saved flair text*
```
Rule1
Rule2
Rule3
```

### Secret and Client_ID
* Go to reddit.com and select user settings
* Select Privacy & Security
* At the very bottom, select Manage third-party app authorization
* At the very bottom again, select create another app..
* In the name, type "PostRemovalBot by ScoopJr"
* Select the bubble: script
* In description, type "Bot that removes rulebreaking posts by flair."
* For about url, type "http://localhost"
* For redirect url, type "http://localhost"
* Select create app

**Secret**
* look next to the text, "Secret", and copy this text down somewhere

*mysecret*
```
daklfanlfkanl392r29neorfjs
```

**Client_ID**
* Look at PostRemovalBot by ScoopJr, and right under Personal Use Script, is our client_id
* Copy the text and save it somewhere

*myclient_id*
```
ddMaksjJsuyeb
```

### Installation for Home PC
* Open up your Command Prompt again, type 
```
python pip install praw
```
* Download the ZIP file and extract the contents to your desktop
* Open the config.ini file and place your information inside and save the file

**NEW HEADER/FOOTER** 
* Add a customized header/footer by editing the HEADER text.  
* {author} is author's name.  Please leave {author} inside HEADER.
```
[main]
USER = example
PASSWORD= ex_password
CLIENT_ID= ddMaksjJsuyeb
SECRET= daklfanlfkanl392r29neorfjs
SUBREDDIT= mysubredditexample
TYPE="public"
DELAY_BETWEEN_RUNS=180

[MSG]
HEADER=Hey {author}! Your submission has been removed for the following reason:
FOOTER=Check out the rules of the subreddit [here.](yourruleslink)
FOOTER2=Disagree with this ruling? Please contact the moderators.
```
* Open the removalreasons.json file, and start adding in your removal flairs and your reasons.
```
{
  "Rule1": "Your post was removed for profanity.  Be Civil!",
  "Rule2": "Your post was removed for trolling.",
  "Rule3": "Your post was removed for reposting deleted content."
}
```

### Running the bot
* Open up your command prompt
* Navigate to the directory your bot is in
```
cd desktop/PostRemovalBot
```
* Type the following
```
python postremovalbot.py
```
* Press the enter key

*The bot is now running!*

### Contributing
Issue Tracker: https://github.com/AkitotheExiled/PostRemovalBot/issues

### Contact
https://www.reddit.com/user/ScoopJr
