import json
import requests

class Watchdog:
    def __init__(self):
        self.get_watchdog_link = requests.get(f'https://api.slothpixel.me/api/bans')
        self.watchdog_data = json.loads(self.get_watchdog_link.text)

        self.last_minute = self.watchdog_data['watchdog']['last_minute']
        self.daily = self.watchdog_data['watchdog']['daily']
        self.total = self.watchdog_data['watchdog']['total']

class Staff:
    def __init__(self):
        self.get_staff_link = requests.get(f'https://api.slothpixel.me/api/bans')
        self.staff_data = json.loads(self.get_staff_link.text)

        self.daily = self.staff_data['staff']['daily']
        self.total = self.staff_data['staff']['total']

