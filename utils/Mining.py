import os
import time
import sys
import json


def Salad_Mining():
    with open('config.json') as f:
        js = json.load(f)
    eth_wallet = js['eth_wallet']
    mon_wallet = js['mon_wallet']

    sys.stdout.write("\x1b]2;Choose miner...\x07")
    color = "\033[32m"  # this is green

    os.system('echo ' + color)
    select = input("Select miner! \n1. Phoenixminer 5.5c (GPU) \n2. XMRig 6.11.2 (CPU) \n3. t-rex (GPU, NVIDIA) \n"
                   "4. Return \nSelect: ")
    if select == "1" or select.lower() == "phoenixminer":
        os.system('clear')
        sys.stdout.write("\x1b]2;Mining ethash with PhoenixMiner\x07")
        while True:
            os.system(r"nice -n1"
                r" miners/PhoenixMiner-5.5c/PhoenixMiner -logfile phoenixlog.txt -rmode 0 -rvram 1"
                r" -pool stratum+tcp://daggerhashimoto.usa.nicehash.com:3353"
                r" -pool2 stratum+tcp://daggerhashimoto.eu.nicehash.com:3353 -ewal " + (
                    eth_wallet) + " -esm 3 -allpools 1 -allcoins 0 -mi 3 -li 35 -acm")
            print("Restarting in 10 seconds")
            time.sleep(10)


    elif select == "2" or select.lower() == "xmrig":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining monero with XMRig miner\x07")
        os.system("nice -n1"
            r" miners/XMRig-6.11.2/xmrig --donate-level=1 -o stratum+tcp://randomxmonero.usa.nicehash.com:3380"
            r" --coin=monero -u " + (
                mon_wallet) + " -k --nicehash -o stratum+tcp://randomxmonero -t 5")

    elif select == "3" or select.lower() == "t-rex" or select.lower() == "trex":
        os.system("clear")
        sys.stdout.write("\x1b]2;Mining ethash with T-Rex miner\x07")
        os.system(
            r"miners/t-rex-0.20.3/t-rex -a ethash -o"
            r" stratum+tcp://daggerhashimoto.usa.nicehash.com:3353"
            r" -u " + (
                eth_wallet))
    input("Returning to main menu...")
