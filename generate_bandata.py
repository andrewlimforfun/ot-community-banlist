import json
import os

INPUT_FILE = "trolls.json"
OUTPUT_FILE = "BanData.txt"

PERSONAL_FILE = "personal_banlist.json"
PERSONAL_OUTPUT_FILE = "PersonalBanData.txt"


def make_bandata(entries):
    return {
        "MutedPlayers": [],
        "MutedPlayerNicks": [],
        "IgnorePlayers": [],
        "IgnorePlayerNicks": [],
        "BanServerPlayers": [e["steamid"] for e in entries],
        "BanServerPlayerNicks": [e["name"] for e in entries]
    }


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    trolls = json.load(f)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(make_bandata(trolls), f, indent=4)
print(f"Written {len(trolls)} banned players to {OUTPUT_FILE}")

if os.path.isfile(PERSONAL_FILE):
    with open(PERSONAL_FILE, "r", encoding="utf-8") as f:
        personal = json.load(f)
    combined = trolls + personal
    with open(PERSONAL_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(make_bandata(combined), f, indent=4)
    print(f"Merged {len(personal)} personal entries, written {len(combined)} total to {PERSONAL_OUTPUT_FILE}")
else:
    print(f"{PERSONAL_FILE} not found, skipping {PERSONAL_OUTPUT_FILE}")

