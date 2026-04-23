# OT Community Banlist

A community-maintained banlist for **On-Together**, aggregating bans from multiple servers.

## Files

### `ban_list.json`
Contains the ban data contributed by the community.

Each entry requires the following mandatory fields:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | yes | In-game player name |
| `steamid` | yes | Steam ID (64-bit) |
| `community` | no | Server or community the ban originates from |
| `reason` | no | Reason for the ban |
| `date` | no | Ban date |
| `evidence` | no | Evidence such as a snippet of Fomo ChatLog or Chalkboard Screenshot |

Contributors may also include any additional fields with relevant information (e.g. `date`, `evidence`, `alt_accounts`). Extra fields are preserved in `ban_list.json` and ignored when generating `BanData.txt`.

```json
{
  "name": "PlayerName",
  "steamid": "76561199000000000",
  "community": "Server Name",
  "reason": "reason for ban",
  "date": "2026-04-23",
  "evidence": "https://link-to-evidence"
}
```

### `BanData.txt`
Generated from `ban_list.json` using `generate_bandata.py`. This file is formatted for direct use in-game.

In-game, On-Together reads ban data from:
```
AppData\LocalLow\GigaPuff\On-Together\BanData.txt
```

Copy the generated `BanData.txt` to that path to apply the banlist.

## How to Contribute

1. Clone this repository.
2. Add your entry to `ban_list.json`. Only `name` and `steamid` are required - all other fields are optional. 
You may include any extra fields with additional context.
3. Run `generate_bandata.py` to regenerate `BanData.txt`:
   ```
   python generate_bandata.py
   ```
4. Commit both `ban_list.json` and `BanData.txt`, then open a pull request.

Please only submit bans that are verifiable and have a legitimate reason. 
False reports will not be accepted.
