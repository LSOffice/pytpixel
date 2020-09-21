import requests
import json

class SkyblockProfile:
    def __init__(self, playerName: str = None, playeruuid: str = None, profile_name: str = None):
        self.playerName = playerName
        self.playeruuid = playeruuid
        self.profilename = profile_name
        if self.playerName == None and self.playeruuid == None:
            raise AttributeError('You need to fill in either playerName or playeruuid')
        
        if self.playerName != None and self.playeruuid != None:
            raise AttributeError("You can't fill in both playerName or playeruuid")

        if self.profilename == None:
            raise ArithmeticError("You need to fill in the self.profilename")

        self.nameValue = self.playerName if not playeruuid else playeruuid

        self.get_profiles_link = requests.get(f'https://api.slothpixel.me/api/skyblock/profiles/{self.nameValue}')
        self.profiles_data = json.loads(self.get_profiles_link.text)

        self.keys_dict = {}

        for key in self.profiles_data.keys():
            self.keys_dict[key] = self.profiles_data[key]['cute_name']

        if self.profilename in self.keys_dict.values():
            self.profile_id = list(self.keys_dict.keys())[list(self.keys_dict.values()).index(self.profilename)]
        else:
            raise KeyError(f"Profile name '{self.profilename}' does not exist in {self.nameValue}'s Skyblock database")

        self.get_attr_link = requests.get(f"https://api.slothpixel.me/api/skyblock/profile/{self.nameValue}/{self.profile_id}")
        self.attr_data = json.loads(self.get_attr_link.text)

        self.members = self.profiles_data[self.profile_id]['members']
        self.bank_balance = "{:,}".format(round(self.attr_data['banking']['balance']))
        self.purse_balance = "{:,}".format(round(self.attr_data['members'][self.nameValue]['coin_purse']))

    def get_profiles(self, item: str = None):
        self.item = item
        
        if self.profilename == None and item == None:
            return list(self.keys_dict.values())
        elif self.profilename != None and self.item != None:
            return self.profiles_data[self.profile_id][self.item]
        else:
            return self.profiles_data[self.profile_id]
    
    def get_attributes(self, attribute: str = None):
        if attribute == None:
            return self.attr_data['members'][self.nameValue]['attributes']
        else:
            attrlist = []
            if isinstance(attribute, list):
                for attr in attribute:
                    attrlist.append(self.attr_data['members'][self.nameValue]['attributes'][attr])

                return attrlist
            else:
                return self.attr_data['members'][self.nameValue]['attributes'][attribute]

    #def convert(self, value):
    #    value = str(value).upper()
    #    value = str(value).replace(" ", "_")
    #
    #    return value