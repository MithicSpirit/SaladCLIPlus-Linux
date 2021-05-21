#!/usr/bin/env python
import sys
import os
import json

try:
    from utils import Start
    from utils import Balance
except ModuleNotFoundError:
    pass


def setup():
    sys.stdout.write("\x1b]2;Salad CLI+ SETUP\x07")
    salad_key = input("Insert your salad Authentication token: ")
    eth_wallet = input("Insert your salad  Ethereum wallet address: ")
    mon_wallet = input("Insert your salad Monero wallet address: ")
    data = {"salad_key": salad_key, "eth_wallet": eth_wallet, "mon_wallet": mon_wallet}
    with open("config.json", "w+") as file:
        json.dump(data, file)


options = [
    "Balance.Salad_Balance()",
    "Lifetime.Salad_Lifetime()",
    "XP.Salad_XP()",
    "salad_earnings_update.Salad_Earnings()",
    "Mining.Salad_Mining()",
    "exit()",
]
switch = {i: option for i, option in enumerate(options)}

try:
    with open("config.json") as file:
        pass
except FileNotFoundError:
    setup()

from utils import Start
from utils import Balance
from utils import Mining
from utils import XP
from utils import Lifetime
from utils import salad_earnings_update

while True:
    info = Start.get_info()
    dun = False
    while not dun:
        # os.system('clear')
        action = Start.starting(info, options)
        try:
            int(action)
            dun = True
        except TypeError or KeyError:
            pass
        if dun:
            exec(switch[int(action)])
            dun = True
