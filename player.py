import requests
import json
import datetime
from .translator import Translator

class User:
    def __init__(self, playerName: str = None, playeruuid: str = None):
        self.playerName = playerName
        self.playeruuid = playeruuid
        if self.playerName == None and self.playeruuid == None:
            raise AttributeError('You need to fill in either playerName or playeruuid')
        
        if self.playerName != None and self.playeruuid != None:
            raise AttributeError("You can't fill in both playerName or playeruuid")

        self.nameValue = self.playerName if not playeruuid else playeruuid

        self.get_username_link = requests.get(f'https://api.slothpixel.me/api/players/{self.nameValue}')
        self.user_data = json.loads(self.get_username_link.text)

        self.rank = self.user_data['rank']

    def get_info(self, item, rewards_object=None, voting_object=None, links_object=None):
        """
        To get the info of a user. The user does not have to be on Hypixel for this to work. 
        They have to be at least logged in once to hypixel, however.
        https://docs.slothpixel.me/#operation/getPlayer

        Items:
        - :uuid:`string`
        - :username:`string`
        - :online:`boolean`
        - :rank:`string`
        - :rank plus color:`string`
        - :rank formatted:`string`
        - :prefix:`string`
        - :karma:`integer`
        - :exp:`integer`
        - :level:`integer`
        - :achievment_points:`integer`
        - :quests completed:`integer`
        - :total kills:`integer`
        - :total wins:`integer`
        - :total coins:`integer`
        - :mc_version:`string`
        - :first login:`integer`
        - :last login:`integer`
        - :last logout:`integer`
        - :last game:`string`
        - :language:`string`
        - :gifts sent:`integer`
        - :gifts received:`integer`
        - :is contributor:`boolean`
        - :rewards:`object`
        - :voting:`object`
        - :links:`object`
        - :stats:`object`

        Params:
        - :item:`string`
        - :rewards_object:`string` (optional)
        - :voting_object:`string` (optional)
        - :links_object:`string` (optional)
        - :stats_object:`string` (optional)

        `versionadded`: 1.0
        """
        self.item = item
        self.item = str(self.item).replace(" ", "_")

        if self.item == 'rewards':
            if rewards_object == None:
                raise AttributeError('Attribute `rewards_object` has to be filled in for :rewards: object')
            else:
                return self.user_data[self.item][rewards_object]
        elif self.item == 'voting':
            if voting_object == None:
                raise AttributeError('Attribute `voting_object` has to be filled in for :voting: object')
            else:
                return self.user_data[self.item][rewards_object]
        elif self.item == 'links':
            if links_object == None:
                raise AttributeError('Attribute `links_object` has to be filled in for :links: object')
            else:
                return self.user_data[self.item][rewards_object]
        elif self.item == 'first_login':
            return datetime.datetime.fromtimestamp(round(self.user_data[self.item]/1000))
        elif self.item == 'last_login':
            return datetime.datetime.fromtimestamp(round(self.user_data[self.item]/1000))
        elif self.item == 'last_logout':
            return datetime.datetime.fromtimestamp(round(self.user_data[self.item]/1000))
        elif self.item == '':
            return self.user_data
        else:
            return self.user_data[self.item]

    def get_status(self, item, game_object=None):
        """
        To get the status of a user. The user has to be on Hypixel for this status to work. Try `get_info` for more information
        https://docs.slothpixel.me/#operation/getPlayerStatus

        Items:
        - :online:`boolean`
        - :game:`object`

        Params:
        - :item:`string`
        - :game_object:`string` (optional)

        `versionadded`: 1.0
        """
        self.item = item
        self.get_status_link = requests.get(f'https://api.slothpixel.me/api/players/{self.nameValue}/status')
        self.user_status = json.loads(self.get_status_link.text)
        if self.item == 'game':
            if game_object == None:
                raise AttributeError('Attribute `game_object` has to be filled in for :game: object')
            else:
                return self.user_status[self.item][game_object]
        else:
            return self.user_status[self.item]

    def get_achievements(self, item, rewards_object=None):
        """
        To get the achievements of a user. The user does not have to be on Hypixel for this to work.
        https://docs.slothpixel.me/#operation/getPlayerAchievements

        Items:
        - :achievement points:`integer`
        - :completed tiered:`integer`
        - :completed one time:`integer`
        - :completed total:`integer`

        Params:
        - :item:`string`
        - :game_object:`string` (optional)

        `versionadded`: 1.0
        """
        self.item = item
        self.get_achievements_link = requests.get(f'https://api.slothpixel.me/api/players/{self.nameValue}/achievements')
        self.achievements_status = json.loads(self.get_achievements_link.text)
        self.item = str(self.item).replace(" ", "_")

        return self.achievements_status[self.item]

    def get_quests(self, item):
        """
        To get the quests of a user. The user does not have to be on Hypixel for this to work.
        https://docs.slothpixel.me/#operation/getPlayerQuests

        Items:
        - :quests completed:`integer`
        - :challenges completed:`integer`
        Params:
        - :item:`string`
        - :game_object:`string` (optional)

        `versionadded`: 1.0
        """
        self.item = item
        self.get_quests_link = requests.get(f'https://api.slothpixel.me/api/players/{self.nameValue}/quests')
        self.quest_data = json.loads(self.get_quests_link.text)
        self.item = str(self.item).replace(" ", "_")

        return self.quest_data[item]

    def get_recentGames(self, gameNumber: int, item=None):
        """
        To get the recent games of a user. The user does not have to be on Hypixel for this to work.
        https://docs.slothpixel.me/#operation/getPlayerQuests

        Items:
        - :date:`datetime`
        - :gameType:`string`
        - :mode:`string`
        - :map:`string`
        - :ended:`datetime`
        Params:
        - :item:`string`
        - :game_object:`string` (optional)

        `versionadded`: 1.0
        """
        gameNumber -= 1
        self.game_number = gameNumber
        self.item = item

        self.get_RC_link = requests.get(f'https://api.slothpixel.me/api/players/{self.nameValue}/recentGames')
        self.recentGames_data = json.loads(self.get_RC_link.text)

        if self.item == 'date' or self.item == 'ended':
            return datetime.datetime.fromtimestamp(round(self.recentGames_data[gameNumber][self.item]/1000))
        elif self.item == 'mode':
            return Translator(self.recentGames_data[gameNumber]['mode'])
        else:
            return self.recentGames_data[gameNumber][self.item]
    
def get_username(*uuid):
    """
    Get the username of a uuid.

    Params:
    - :uuid:`string`, `array`

    Returns:
    - :username:`string`, `array`

    `versionadded`: 1.0
    """
    uuids = []

    for arg in uuid:
        if isinstance(arg, list):
            for uuid2 in arg:
                get_username_link = requests.get(f'https://api.slothpixel.me/api/players/{uuid2}')
                user_data = json.loads(get_username_link.text)

                uuids.append(user_data['username'])
        else:
            get_username_link = requests.get(f'https://api.slothpixel.me/api/players/{arg}')
            user_data = json.loads(get_username_link.text)

            uuids.append(user_data['username'])
    
    if len(uuids) == 1:
        return uuids[0]
    else:
        return uuids

def get_uuid(*username):
    """
    Get the uuid of a username

    Params:
    - :username:`string`, `array`

    Returns:
    - :uuid:`string`, `array`

    `versionadded`: 1.0
    """
    usernames = []

    for arg in username:
        if isinstance(arg, list):
            for username2 in arg:
                get_username_link = requests.get(f'https://api.slothpixel.me/api/players/{username2}')
                user_data = json.loads(get_username_link.text)

                usernames.append(user_data['uuid'])
        else:
            get_username_link = requests.get(f'https://api.slothpixel.me/api/players/{arg}')
            user_data = json.loads(get_username_link.text)

            usernames.append(user_data['uuid'])
    
    if len(usernames) == 1:
        return usernames[0]
    else:
        return usernames