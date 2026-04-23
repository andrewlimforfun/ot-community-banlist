import json

INPUT_FILE = "ban_list.json"
OUTPUT_FILE = "BanData.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    banned = json.load(f)

steamids = [entry["steamid"] for entry in banned]
nicks = [entry["name"] for entry in banned]

output = {
    "MutedPlayers": [],
    "MutedPlayerNicks": [],
    "IgnorePlayers": [],
    "IgnorePlayerNicks": [],
    "BanServerPlayers": steamids,
    "BanServerPlayerNicks": nicks
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print(f"Written {len(steamids)} banned players to {OUTPUT_FILE}")
