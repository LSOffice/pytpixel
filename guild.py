import requests
import json
import datetime

class Guild:
    def __init__(self, playerName: str = None, playeruuid: str = None):
        self.playerName = playerName
        self.playeruuid = playeruuid
        if self.playerName == None and self.playeruuid == None:
            raise AttributeError('You need to fill in either playerName or playeruuid')
        
        if self.playerName != None and self.playeruuid != None:
            raise AttributeError("You can't fill in both playerName or playeruuid")

        self.nameValue = self.playerName if not playeruuid else playeruuid

        self.get_stats_link = requests.get(f'https://api.slothpixel.me/api/guilds/{self.nameValue}')
        self.stats_data = json.loads(self.get_stats_link.text)
    
    def get_stats(self, item):
        """
        To get the guild stats of a user's guild. The user does not have to be on Hypixel for this to work.
        However, they must belong in a guild.
        https://docs.slothpixel.me/#operation/getGuildFromPlayer

        Items:
        - :name:`string`
        - :id:`string`
        - :created`string`
        - :tag:`string`
        - :tag color:`string`
        - :tag formatted:`string`
        - :exp:`integer`
        - :level:`integer`
        - :exp by game:`integer`
        - :description:`object`
        - :preferred games:`list`

        - :legacy_ranking:`integer` (LEGACY)

        Params:
        :item:`string`

        `versionadded`: 1.0
        """
        self.item = item
        self.item = str(self.item).replace(" ", "_")

        if self.item == 'created':
            return datetime.datetime.fromtimestamp(round(self.stats_data[self.item]/1000))
        elif self.item == 'preferred_games':
            return list(self.stats_data[self.item])

        return self.stats_data[self.item]
    
    def get_exp_history(self, date: str):
        """
        To get the guild exp history of a user. The user does not have to be on Hypixel for this to work.
        https://docs.slothpixel.me/#operation/getGuildFromPlayer

        Params:
        - :date:`string` (e.g YYYY-MM-DD, 2020-01-26)

        `versionadded`: 1.0
        """
        self.date = date

        return self.stats_data['exp_history'][self.date]