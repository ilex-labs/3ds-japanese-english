# 3ds-jpn-english

English menus for a Japanese 3DS: the HOME Menu and System Settings, without a region change. Nothing on the console itself is changed, and you can undo it by deleting its folders from the SD card.

> **Maintained fork.** This is a fork of [imphuochuynh/luma-jpn-english](https://github.com/imphuochuynh/luma-jpn-english), which its author released as is and isn't updating. This fork fixes bugs and adds a script and double-click launchers, so you don't have to dump files by hand or use the command line. See [Changes from upstream](#changes-from-upstream).

**Important:** This repo contains only the translation tables and the build tools. It does **not** include any Nintendo files. You dump the original files from your own console, and the build script produces the translated versions for your SD card.

**Download:** Get the latest zip file from the [Releases](https://github.com/ilex-labs/3ds-jpn-english/releases) page.

## What you get

| App | Title ID | Status |
|---|---|---|
| HOME Menu (menus, dialogs, HOME Menu Settings, sleep/power screens, built-in tips) | `0004003000008202` | 509 of 514 lines (the other 5 are already Latin text) |
| System Settings (every menu, Internet setup, Data Management, Parental Controls, first-time setup) | `0004001000020000` | 1,049 of 1,053 lines (the other 4 are already English or are prompts for other regions) |
| Top-screen status bar (Wi-Fi state, date and weekday) | Covered in both apps above | Done |
| Notifications | `0004003000008E02` | **Not supported**, see [Known limitations](#known-limitations) |

Nintendo's usual US English names are used where they exist (Game Notes, StreetPass, SpotPass, Play Coins, Super-Stable 3D, Circle Pad).

## Why not just do a region change?

The usual way to get English menus on a Japanese 3DS is a region change. This tool avoids it because:

- **A region change is hard to undo.** Removing custom firmware afterwards means restoring the NAND backup you made before the change, and getting that wrong can brick the console.
- **It can break your online account.** Nintendo Network IDs are tied to the region they were made in, so you can lose eShop access and anything linked to it, like Pokémon Bank.
- **It's more than most people need** if you just want to read the menus. Region-free and per-game language settings already cover games.

This approach only adds files under `luma/titles/` on the SD card. It works like a game mod: whenever the HOME Menu or System Settings reads its text, Luma hands it the English version from the SD card instead, on the fly. Nothing on the console itself is modified. Delete the folder and everything is back to Japanese.

**The trade-off:** it only covers apps Luma can patch (Notifications can't be), and it translates the interface, not text that games or Nintendo send you.

## What you need

- A Japanese-region 3DS family console (3DS, 2DS, New 3DS or New 2DS, any size) with **[Luma3DS v13.4](https://github.com/LumaTeam/Luma3DS/releases/tag/v13.4) or newer** and **[GodMode9 v2.2.3](https://github.com/d0k3/GodMode9/releases/tag/v2.2.3) or newer**. If you followed the standard [3ds.hacks.guide](https://3ds.hacks.guide) setup guide, you already have both, but if you set it up a while ago they may be older versions (see below).
- A Windows or Mac computer with **Python 3.8 or newer** (see [Install Python](#install-python)).

<details>
<summary><b>Checking and updating Luma3DS and GodMode9</b></summary>

**Check which versions you have:**

- **Luma3DS:** hold **SELECT** while powering on. The version is shown at the top of the Luma configuration menu. Press **START** to continue booting.
- **GodMode9:** hold **START** while powering on. The version is shown on the bottom screen. Hold **R** and press **START** to power off.

**Update Luma3DS** if it's older than v13.4:

1. Download the Luma3DS zip from its [latest release](https://github.com/LumaTeam/Luma3DS/releases/latest) (the `Luma3DS` zip, not "Source code").
2. Put your SD card in your computer and copy everything from the zip to the root of the SD card, replacing the existing files.
3. Put the SD card back and power on. Luma updates itself from there.

**Update GodMode9** if it's older than v2.2.3:

1. Download the GodMode9 zip from its [latest release](https://github.com/d0k3/GodMode9/releases/latest).
2. Put your SD card in your computer. Copy `GodMode9.firm` from the zip into the `luma/payloads` folder on the SD card, replacing the old one.
3. Copy the `gm9` folder from the zip to the root of the SD card, replacing the existing files.

3ds.hacks.guide has more detail on [updating GodMode9](https://3ds.hacks.guide/godmode9-usage).

</details>

**Tested on** these Japanese consoles: New 3DS (by the original author), New 3DS LL and New 2DS LL. This fork was tested with Luma3DS v13.4 and GodMode9 v2.2.3, the latest releases in November 2026. Other models should work the same way; if you try one, please let us know in an issue.

## Install Python

The tool runs on Python, a free program. You only need to install it once.

**Windows** (10 or 11)

1. Open the **Microsoft Store** app, search for **Python install manager** and click **Install**. (It's also available to download from [python.org/downloads](https://www.python.org/downloads/).)
2. Open **Terminal** from the Start menu, type `python` and press Enter. If it asks setup questions, accept the suggested answers. When you see `>>>`, type `exit()`, press Enter and close the window.

If you already have Python 3.8 or newer, that works too.

**macOS**

1. Go to [python.org/downloads](https://www.python.org/downloads/) and click **Download Python**.
2. Open the downloaded file and click through the installer.

> **Note:** if your Mac ever offers to install "command line developer tools" for `python3`, click **Cancel**. You don't need them; the python.org installer is enough.

If the tool later says Python wasn't found, restart your computer and try again.

## 1. Copy and decrypt the original files

The zip includes a GodMode9 script that copies the relevant app files from your console to your SD card and decrypts them. It only reads from the console and writes to the `gm9/out` folder on the SD card.

1. Put your SD card in your computer. Copy `gm9/scripts/dump_system_apps.gm9` from the zip into the `gm9/scripts` folder on the SD card (create `scripts` if it isn't there).
2. Put the SD card back in the console. Hold **START** while powering on to open GodMode9.
3. Press **HOME** → **Scripts...** → **dump_system_apps**, then press **A** to confirm.
4. Wait until the bottom screen shows a summary, then press **A**. Hold **R** and press **START** to power off.
5. Put the SD card in your computer. Copy the folder `gm9/out/3ds-jpn-english` into the folder where you unzipped this tool, and rename the copy to `dumps`.

If the script is interrupted, just run it again.

<details>
<summary><b>Dumping by hand instead</b></summary>

If you'd rather not use the script, or would only like to translate certain files for some reason, boot up GodMode9 and:

1. Go to `[1:] SYSNAND CTRNAND` > `title` > navigate to the correct title folder > `content`.
2. Highlight the relevant `.app` file(s), press **Y** to copy them, go to `[0:] SDCARD` > `gm9` > `out` and press **Y** to paste.
3. In `gm9/out`, highlight each copied `.app`, press **A** > **NCCH image options...** > **Decrypt file**.

Then put the decrypted `.app` files in a folder called `dumps` next to `build.bat` and `build.command`.

</details>

> **Important:** don't share the dumped files or anything the tool builds from them, whether you used the script or dumped them by hand. They contain copyrighted system software from your console.

## 2. Build

**Windows:** double-click `build.bat`. It uses the `dumps` folder next to it; if there isn't one, it asks you to drag your dumps folder into the window. You can also drag the folder straight onto `build.bat`. If Windows warns you about it, choose **Run** (or **More info** and then **Run anyway**).

**macOS:** double-click `build.command`. It uses the `dumps` folder next to it; if there isn't one, it asks you to drag your dumps folder into the window. The first time the script is run, it is likely that macOS will block it because it is a downloaded file:

- **macOS 15 or newer:** click **Done** (not **Move to Trash**). Open **System Settings** > **Privacy & Security**, scroll down, click **Open Anyway** next to `build.command`, then **Open Anyway** again and confirm with your password or Touch ID.
- **macOS 14 or older:** right-click `build.command`, choose **Open**, then **Open** again.
- **Or:** open **Terminal**, type `bash` and a space, drag `build.command` into the window and press Return.

If macOS asks whether Terminal can access a folder, click **Allow**.

When it's done, the `out` folder opens.

The script identifies each file from its header, translates it, and checks every line before writing anything:

- formatting codes, button icons and `%d`-style placeholders must match the original exactly
- labels in System Settings can't use added font-size codes (they render blank there)
- your files must match the system version the translation was made for; if they don't, it stops instead of putting text in the wrong places

If any check fails, nothing is written. Some lines are a little longer than the Japanese and may show on two lines; that's normal. They're listed in `out/long-lines.txt` in case one looks wrong on your console. If you'd like to shorten one yourself, see [Editing translations](#editing-translations).

## 3. Install

1. Copy the folders inside `out/luma/titles` into the `luma/titles` folder on your SD card (create `titles` if it isn't there). Copy just those folders, not the whole `luma` folder, so your Luma settings stay as they are.
   - **Important:** On macOS, don't drag `luma` onto `luma` in Finder: that replaces the folder and wipes your Luma settings. Copy `out/luma/titles/*` into the SD card's `luma/titles/` instead.
2. Hold **SELECT** while powering on to open the Luma menu and make sure **Enable game patching** is on.
3. Eject the SD card properly before taking it out.

## Undo

To undo the changes, delete these folders from the SD card:

- `luma/titles/0004003000008202` (HOME Menu)
- `luma/titles/0004001000020000` (System Settings)

You can do this on a computer, or on the console:

- **With GodMode9:** hold **START** while powering on, go to `[0:] SDCARD` > `luma` > `titles`, highlight a folder, press **X** and confirm. If it asks you to unlock writing, enter the buttons it shows. This works even if the HOME Menu won't start.
- **With 3DShell:** browse to `luma/titles`, highlight a folder, press **X** and choose delete.

**If the HOME Menu won't start:** hold **SELECT** while powering on and turn off **Enable game patching**. The console then starts normally in Japanese. Delete the folders with 3DShell (or GodMode9), then turn **Enable game patching** back on if you use other Luma mods.

## Known limitations

- **Notifications can't be translated.** Luma can't patch that app on Japanese consoles; trying makes the console stop when it opens.
- **Only HOME Menu and System Settings** are translated, not other system apps.
- **Messages from games and Nintendo stay in Japanese.** StreetPass results, SpotPass news and announcements are written by the sender, not part of the menus.
- **The Language setting** shows the language names in English, but Japanese is still the only choice on a Japanese console.
- **Some labels are shortened to fit** (for example "Conn. 1" for Connection 1). If something looks cut off on your console, please open an issue with a photo.

## For developers

### Building from a terminal

```
python3 build.py dumps
```

(`py build.py dumps` on Windows.) You can pass `.app` files instead of a folder.

Folders named `dumps` or `dumps-anything` are git-ignored, so dumps can't be committed by accident.

### Checking whether Luma can patch an app

```
python3 -m tools.lfs_check dumps
```

Not every app can be patched. LayeredFS needs to find five file-system functions in an app's code; the Japanese Notifications app, for example, has no general "mount archive" function, so Luma halts the console when it opens with a translation folder present. Its table is kept in `translations/notifications.py` for reference; the build skips it.

### Editing translations

The tables are in `translations/`, keyed by string number. Strings use a display form: plain text, plus `{{hex}}` tokens for Nintendo's formatting codes, copied verbatim from the original. `translations/common.py` has named constants for the button icons (`A`, `B`, `HOME`, ...) and common formatting blocks. Run the build after every change; it rejects anything that would break on the console.

### How it works

- `tools/ncch.py` reads decrypted `.app` (NCCH) files: header, RomFS, and the program code.
- `tools/msgtool.py` handles LZ11 compression and Nintendo's MSBT text format.
- `tools/darc.py` repacks the DARC archive System Settings keeps its text in.
- `tools/lfs_check.py` is a port of Luma3DS's LayeredFS function search.
- `tools/inputs.py` turns folders and wildcards into a list of `.app` files, and keeps user names out of the output.
- `build.py` ties it together, validates, and writes the `luma/titles/...` tree. `build.bat` and `build.command` find Python and run it.
- `gm9/scripts/dump_system_apps.gm9` is generated by `tools/gen_dump_script.py`, which also checks the script's structure. It's written for GodMode9 v2.2.3. Edit the generator, then run `python3 -m tools.gen_dump_script`.

Releases are built by GitHub Actions (`.github/workflows/release.yml`) from the tagged commit with `git archive`, so a release zip contains only files in this repo.

## Changes from upstream

Upstream is [imphuochuynh/luma-jpn-english](https://github.com/imphuochuynh/luma-jpn-english) at commit `e205d57` (2 November 2026), counted here as v1.0.

**v1.1** (November 2026)

- New: a GodMode9 script that dumps and decrypts HOME Menu and System Settings in one go.
- New: double-click launchers `build.bat` (Windows) and `build.command` (macOS).
- New: the build accepts a whole dumps folder as well as `.app` files.
- Fixed: on Windows, `build.py dumps\*.app` failed because the shell doesn't expand wildcards.
- Fixed: the build wrote output files even when a check failed. It now writes nothing unless every check passes.
- Fixed: `tools.lfs_check` crashed on manual and data `.app` files.
- Fixed: the build no longer crashes if the window can't display a character.
- The build output is shorter (lines that may show on two lines are listed in `out/long-lines.txt`) and no longer shows your user name, so it's safe to paste into an issue.
- `.gitignore` also blocks console-unique files (`essential.exefs`, `movable.sed`, `otp.bin`) and `dumps-*` folders.
- README rewritten for the fork.

The full list is in the commit history.

## AI disclosure

**Original project.** The upstream README's disclosure, unchanged, by its author [imphuochuynh](https://github.com/imphuochuynh) ("I" and "this README" refer to them and their README):

> This project was built with [Claude](https://claude.ai), Anthropic's AI assistant. Claude wrote the build tools, the validator and the Luma compatibility checker, translated the Japanese text into English, and drafted this README. I directed the project, made the design decisions, and tested every change on my own Japanese New 3DS. That's how the problem labels, the System Settings font-size issue and the Notifications crash were found and fixed.
>
> The translations are AI-generated and have only been checked on screen, not reviewed line by line by a fluent Japanese speaker. Some wording may be off, especially in screens I rarely see. If you spot a mistranslation, you can fix it in `translations/` and rebuild.

**This fork.** It's made the same way. The code, the GodMode9 script and the translation work are written by Claude. The maintainer decides what to change and tests every change on real Japanese consoles before it's released, but doesn't read Japanese and doesn't review the code line by line. As above, the translations haven't been reviewed by a fluent Japanese speaker; if you spot a mistranslation, please open an issue.

## Credits

- [imphuochuynh](https://github.com/imphuochuynh) for the original project.
- [Luma3DS](https://github.com/LumaTeam/Luma3DS) for LayeredFS. `tools/lfs_check.py` ports its symbol search.
- [GodMode9](https://github.com/d0k3/GodMode9) for dumping and decrypting, and its scripting language.
- [3dbrew](https://www.3dbrew.org) for documentation of the file formats and title IDs.

## License

GPLv3, see [LICENSE](LICENSE), the same as upstream.

Not affiliated with or endorsed by Nintendo. This repo contains no Nintendo code, data or text; all files are generated from your own console's dumps.
