import time
import requests
from data.common import *

def get_all_friends(token):
    set_console_title("DisKiller | Insta: 0xmrjoex | Get Friends")
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    print("\n")
    for friend in r.json():
        print(f"{rr}[ {w}+ {rr}]{w} {friend['user']['username']}#{friend['user']['discriminator']}")
    time.sleep(2)
    print("\n")
    input("Press any key to continue...")