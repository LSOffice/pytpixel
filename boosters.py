import json
import requests
import datetime

class Boosters:
    def __init__(self, gamemode: str):
        self.gamemode = gamemode
        self.get_boosters_link = requests.get(f'https://api.slothpixel.me/api/boosters/{self.gamemode}')
        self.boosters_data = json.loads(self.get_boosters_link.text)

        self.amount = len(self.boosters_data)

    def get_user(self, booster_number: int):
        booster_number -= 1
        self.booster_number = booster_number
        return self.boosters_data[int(self.booster_number)]['uuid']

    def get_multiplier(self, booster_number: int):
        booster_number -= 1
        self.booster_number = booster_number
        return self.boosters_data[int(self.booster_number)]['multiplier']

    def get_activated(self, booster_number: int):
        booster_number -= 1
        self.booster_number = booster_number
        return datetime.datetime.fromtimestamp(round(self.boosters_data[int(self.booster_number)]['activated']/1000))

    def get_length(self, booster_number: int):
        booster_number -= 1
        self.booster_number = booster_number
        self.original_length = self.boosters_data[int(self.booster_number)]['original_length']
        self.length = self.boosters_data[int(booster_number)]['length']

    def get_active(self, booster_number: int):
        booster_number -= 1
        self.booster_number = booster_number
        return self.boosters_data[int(self.booster_number)]['active']
        
def get_gamemodes():
    get_boosters_link = requests.get(f'https://api.slothpixel.me/api/boosters')
    boosters_data = json.loads(get_boosters_link.text)

    gamemode_list = []

    for gameMode in boosters_data['boosters']:
        gamemode_list.append(gameMode)

    return gamemode_list