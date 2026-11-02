# luma-jpn-english

English HOME Menu and System Settings for Japanese-region 3DS consoles, using Luma3DS's LayeredFS. No region change, nothing written to system memory, and fully removable by deleting a folder.

This repo contains only the translation tables and the build tools. It does **not** include any Nintendo files. You dump the original files from your own console, and the build script produces the translated versions for your SD card.

## What gets translated

| App | Title ID | Status |
|---|---|---|
| HOME Menu (menus, dialogs, HOME Menu Settings, sleep/power screens, built-in tips) | `0004003000008202` | 509 of 514 lines (the other 5 are already Latin text) |
| Top-screen status bar (Wi-Fi state, date and weekday) | part of both apps above and below | Done |
| System Settings (every menu, Internet setup, Data Management, Parental Controls, first-time setup) | `0004001000020000` | 1,049 of 1,053 lines (the other 4 are already English or are prompts for other regions) |
| Notifications | `0004003000008E02` | **Not supported**, see [Known limitations](#known-limitations) |

Nintendo's usual US English names are used where they exist (Game Notes, StreetPass, SpotPass, Play Coins, Super-Stable 3D, Circle Pad).

## Why not just do a region change?

The standard way to get English menus on a Japanese 3DS is a region change with CTRTransfer. I didn't want to commit to that:

- **It's hard to back out of.** After a region change you can't uninstall custom firmware without first restoring the NAND backup you made before the change. Getting it wrong bricks the console, and restoring the backup throws away everything you did since.
- **It breaks online accounts.** Nintendo Network IDs are locked to the region they were made in, so you can lose eShop access, and anything tied to it, like Pokémon Bank.
- **It's more than I needed.** I wanted to read the menus, not change what the console is. Region-free and per-game language settings already cover games.

This approach only adds files under `luma/titles/` on the SD card. Luma swaps them in when an app reads its text, and nothing on the console itself is modified. Delete the folder and everything is back to Japanese.

The trade-off: it only covers apps Luma can patch (Notifications can't be), and it translates the interface, not text that games or Nintendo send you.

## Requirements

- A Japanese-region 3DS family console with **Luma3DS v13.4 or newer** and **GodMode9** (the standard [3ds.hacks.guide](https://3ds.hacks.guide) setup). Developed and tested on a Japanese New 3DS.
- Python 3.8+ on your computer. No extra packages needed.

## 1. Dump and decrypt the original files

You need two files from your console. In GodMode9 (hold **START** while powering on):

1. Go to `[1:] SYSNAND CTRNAND` > `title` > `00040030` > `00008202` > `content`.
2. Highlight the `.app` file, press **Y** to copy it, go to `[0:] SDCARD` > `gm9` > `out` and press **Y** to paste.
3. Do the same for System Settings: `[1:] SYSNAND CTRNAND` > `title` > `00040010` > `00020000` > `content`. There are two `.app` files here. Copy both; the build uses the larger one and skips the other, which is the digital manual.
4. In `gm9/out`, highlight each copied `.app`, press **A** > **NCCH image options...** > **Decrypt file**.

These steps only read from system memory.

Copy the decrypted `.app` files from `gm9/out` on the SD card into a `dumps/` folder in this repo. `dumps/` is git-ignored, so they can't be committed by accident.

## 2. Build

```
python3 build.py dumps/*.app
```

The script identifies each file from its header, translates it, and checks every line before writing anything:

- formatting codes, button icons and `%d`-style placeholders must match the original exactly
- labels in System Settings can't use added font-size codes (they render blank there)
- your files must match the system version the translation was made for; if they don't, it stops instead of putting text in the wrong places

Width warnings are fine. They flag lines longer than the Japanese that might wrap.

## 3. Install

1. Copy the generated `out/luma` folder onto the root of your SD card, **merging** with the existing `luma` folder.
   - On macOS, don't drag `luma` onto `luma` in Finder: that replaces the folder and wipes your Luma settings. Copy `out/luma/titles/*` into the SD card's `luma/titles/` instead.
2. Make sure **Enable game patching** is on in the Luma configuration menu (hold **SELECT** while powering on).
3. Eject the SD card properly before removing it.

## Undo

Delete these folders from the SD card:

- `luma/titles/0004003000008202` (HOME Menu)
- `luma/titles/0004001000020000` (System Settings)

If an app won't start and you can't reach a computer, hold **SELECT** while powering on and turn off **Enable game patching**. That disables all LayeredFS mods until you turn it back on.

## Known limitations

- **Notifications can't be translated.** LayeredFS needs to find five file-system functions in an app's code. The Japanese Notifications app has no general "mount archive" function (it only ever opens one fixed archive), so Luma can't hook it. With a translation folder present, Luma's loader halts the console when the app opens. The table is kept in `translations/notifications.py` for reference, but the build skips it.
- **Notification messages stay Japanese anyway.** StreetPass results, SpotPass news and game announcements are stored text written by the sender, not part of any app.
- **The Language screen** shows the language names in English, but Japanese is still the only language a Japanese system offers.
- **Some labels are shortened to fit** (for example "Conn. 1" for Connection 1, "Format System", "Manage Data"). If something wraps or gets cut off on your console, open an issue with a photo.
- **Other system apps** (Friend List, Game Notes, etc.) aren't translated. Check whether one is patchable before trying:

  ```
  python3 -m tools.lfs_check dumps/*.app
  ```

## Editing translations

The tables are in `translations/`, keyed by string number. Strings use a display form: plain text, plus `{{hex}}` tokens for Nintendo's formatting codes, copied verbatim from the original. `translations/common.py` has named constants for the button icons (`A`, `B`, `HOME`, ...) and common formatting blocks. Run the build after every change; it rejects anything that would break on the console.

## How it works

- `tools/ncch.py` reads decrypted `.app` (NCCH) files: header, RomFS, and the program code.
- `tools/msgtool.py` handles LZ11 compression and Nintendo's MSBT text format.
- `tools/darc.py` repacks the DARC archive System Settings keeps its text in.
- `tools/lfs_check.py` is a port of Luma3DS's LayeredFS function search, used to predict whether Luma can patch an app.
- `build.py` ties it together, validates, and writes the `luma/titles/...` tree.

## Credits

- [Luma3DS](https://github.com/LumaTeam/Luma3DS) for LayeredFS. `tools/lfs_check.py` ports its symbol search.
- [GodMode9](https://github.com/d0k3/GodMode9) for dumping and decrypting.
- [3dbrew](https://www.3dbrew.org) for documentation of the file formats and title IDs.

## License

GPLv3, see [LICENSE](LICENSE).

Not affiliated with or endorsed by Nintendo. This repo contains no Nintendo code, data or text; all files are generated from your own console's dumps.
