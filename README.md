# OT Community Banlist

A community-maintained banlist for **On-Together**, aggregating bans from multiple servers.

## Files

### `trolls.json`
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

Contributors may also include any additional fields with relevant information (e.g. `date`, `evidence`, `alt_accounts`). Extra fields are preserved in `trolls.json` and ignored when generating `BanData.txt`.

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
Generated from `trolls.json` using `generate_bandata.py`. This file is formatted for direct use in-game.

In-game, On-Together reads ban data from:
```
AppData\LocalLow\GigaPuff\On-Together\BanData.txt
```

Copy the generated `BanData.txt` to that path to apply the banlist.

### `personal_banlist.json` (optional, not tracked)
A local file you can create yourself following the same format as `trolls.json`. It is not committed to the repository. When present, `generate_bandata.py` merges it into `PersonalBanData.txt`.

This could contain a very young player that does not fit in your community for example.

### `PersonalBanData.txt`
Generated from `trolls.json` combined with your personal `personal_banlist.json` (if present). Use this instead of `BanData.txt` if you want to supplement the community list with your own private entries.

Copy to:
```
AppData\LocalLow\GigaPuff\On-Together\BanData.txt
```

## How to Contribute

1. Clone this repository.
2. Add your entry to `trolls.json`. Only `name` and `steamid` are required - all other fields are optional.
You may include any extra fields with additional context.
3. Run `generate_bandata.py` to regenerate `BanData.txt`:
   ```
   python generate_bandata.py
   ```
4. Commit both `trolls.json` and `BanData.txt`, then open a pull request.

Please only submit bans that are verifiable and have a legitimate reason.
False reports will not be accepted.
