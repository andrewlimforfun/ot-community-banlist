import json
import os

INPUT_FILE = "trolls.json"
OUTPUT_FILE = "BanData.txt"
CHAT_BROADCAST_FILE = "ChatBroadcast.txt"

PERSONAL_FILE = "personal_banlist.json"
PERSONAL_OUTPUT_FILE = "PersonalBanData.txt"
PERSONAL_CHAT_BROADCAST_FILE = "PersonalChatBroadcast.txt"


def make_bandata(entries):
    return {
        "MutedPlayers": [],
        "MutedPlayerNicks": [],
        "IgnorePlayers": [],
        "IgnorePlayerNicks": [],
        "BanServerPlayers": [e["steamid"] for e in entries],
        "BanServerPlayerNicks": [e["name"] for e in entries]
    }


def make_chat_broadcast(entries):
    lines = []
    for e in entries:
        name = e.get("name", "Unknown")
        steamid = e.get("steamid", "Unknown")
        communities = e.get("communities") or []
        if isinstance(communities, str):
            communities = [communities]
        communities_text = ", ".join(communities) if communities else "Unknown"
        reason = e.get("reason") or "No reason provided"
        lines.append(
            f"Name: {name} | SteamID: {steamid} | Communities: {communities_text} | Reason: {reason}"
        )
    return "\n".join(lines) + ("\n" if lines else "")


with open(INPUT_FILE, "r", encoding="utf-8") as f:
    trolls = json.load(f)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(make_bandata(trolls), f, indent=4)
print(f"Written {len(trolls)} banned players to {OUTPUT_FILE}")

with open(CHAT_BROADCAST_FILE, "w", encoding="utf-8") as f:
    f.write(make_chat_broadcast(trolls))
print(f"Written chat broadcast list for {len(trolls)} players to {CHAT_BROADCAST_FILE}")

if os.path.isfile(PERSONAL_FILE):
    with open(PERSONAL_FILE, "r", encoding="utf-8") as f:
        personal = json.load(f)
    combined = trolls + personal
    with open(PERSONAL_OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(make_bandata(combined), f, indent=4)
    print(f"Merged {len(personal)} personal entries, written {len(combined)} total to {PERSONAL_OUTPUT_FILE}")

    with open(PERSONAL_CHAT_BROADCAST_FILE, "w", encoding="utf-8") as f:
        f.write(make_chat_broadcast(combined))
    print(
        f"Written merged chat broadcast list for {len(combined)} players to {PERSONAL_CHAT_BROADCAST_FILE}"
    )
else:
    print(
        f"{PERSONAL_FILE} not found, skipping {PERSONAL_OUTPUT_FILE} and {PERSONAL_CHAT_BROADCAST_FILE}"
    )

