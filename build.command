#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
#
# macOS launcher for build.py. Double-click it in Finder. It uses a folder
# named "dumps" next to this file, or asks you to drag your dumps folder
# into the Terminal window. From Terminal you can also pass the folder:
#   bash build.command path/to/dumps

cd "$(dirname "$0")" || exit 1
export PYTHONIOENCODING=utf-8

finish() {
    echo
    read -r -n 1 -s -p "Press any key to close this window."
    echo
    exit "$1"
}

# A fresh Mac has /usr/bin/python3, but it's only a placeholder: running it
# opens Apple's "install command line developer tools" dialog instead of
# Python. It's real only once those tools are installed, which is what
# xcode-select -p checks (without opening any dialog). So never run it
# unless that check passes.
is_placeholder() {
    case "$1" in
        /usr/bin/python3|/usr/bin/python) ! xcode-select -p >/dev/null 2>&1 ;;
        *) return 1 ;;
    esac
}

PY=
SAW_PLACEHOLDER=
for c in /Library/Frameworks/Python.framework/Versions/Current/bin/python3 \
         /usr/local/bin/python3 /opt/homebrew/bin/python3 python3 python; do
    p=$(command -v "$c" 2>/dev/null) || continue
    if is_placeholder "$p"; then
        SAW_PLACEHOLDER=1
        continue
    fi
    if "$p" -c 'import sys; sys.exit(sys.version_info < (3, 8))' >/dev/null 2>&1; then
        PY=$p
        break
    fi
done
if [ -z "$PY" ]; then
    echo "Python 3.8 or newer wasn't found."
    if [ -n "$SAW_PLACEHOLDER" ]; then
        echo "(Your Mac's built-in python3 is only a placeholder that offers to"
        echo "install Apple's developer tools. You don't need those.)"
    fi
    echo
    echo "Install Python from https://www.python.org/downloads/ (the macOS"
    echo 'installer), then double-click build.command again. See "Install Python"'
    echo "in README.md."
    finish 1
fi

if [ $# -gt 0 ]; then
    "$PY" build.py "$@"
elif [ -d dumps ]; then
    echo "Using the dumps folder next to build.command."
    echo
    "$PY" build.py dumps
else
    echo "Drag your dumps folder into this window, then press Return."
    echo "(That's the 3ds-jpn-english folder from gm9/out on your SD card.)"
    echo
    # No -r: Terminal escapes spaces in dragged paths with backslashes,
    # and plain read removes them.
    # shellcheck disable=SC2162
    read -p "Folder: " DUMPS
    DUMPS=${DUMPS%\"}; DUMPS=${DUMPS#\"}; DUMPS=${DUMPS%\'}; DUMPS=${DUMPS#\'}
    if [ -z "$DUMPS" ]; then
        echo "No folder given, nothing built."
        finish 1
    fi
    # Clear the screen and scrollback so the dragged-in path (which includes
    # the user name) isn't left in the window if someone pastes the output.
    printf '\033[3J\033[H\033[2J'
    echo "Building from the folder you dragged in."
    echo
    "$PY" build.py "$DUMPS"
fi
rc=$?

echo
if [ $rc -eq 0 ]; then
    echo "Opening the out folder. Copy the folders inside out/luma/titles"
    echo "into luma/titles on your SD card (see README, step 3)."
    open out
else
    echo "The build stopped. Nothing was written; read the messages above."
fi
finish $rc
