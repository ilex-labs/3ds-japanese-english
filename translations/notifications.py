# SPDX-License-Identifier: GPL-3.0-or-later
from .common import *

LOSE = '\n' + NOTE + '(Unsaved data will\nbe lost.)' + NOTE_END
KEEP = '\n' + NOTE + '(Your data will be saved.)' + NOTE_END
SPACER = '{{0e000100000002001400}}\n\u3000{{0f0001000000}}\n'

# Notifications applet (newslist_msbt), JPN title 0004003000008E02
T = {
    0: 'Close the suspended software\nand start this one?' + LOSE,
    1: 'Close the suspended software\nand start this one?' + KEEP,
    2: 'Closing the suspended\nsoftware...',
    3: 'Close the suspended software\nand start this one?',
    4: B + ' Cancel',
    5: A + ' OK',
    6: A + ' OK',
    7: 'Start this software?',
    8: 'Start this software\nin 2D?' + SPACER + NOTE + '* A PIN is required\nto start in 3D.' + NOTE_END,
    9: 'This software is restricted\nby Parental Controls.' + SPACER + 'Unlock the restriction?',
    10: 'Incorrect PIN.' + SPACER + 'Starting in 2D.',
    11: 'Start this software\nin 2D?' + SPACER + NOTE + '* The PIN is required again\nto start in 3D.' + NOTE_END,
    12: A + ' Unlock',
    13: A + ' {{0e000100010002005300}}Start in 2D{{0f0001000100}}',
    14: B + ' {{0e000100010002005300}}Start in 3D{{0f0001000100}}',
    15: 'The Game Card could\nnot be read.' + SPACER + 'Please reinsert\nthe Game Card.',
    17: 'The SD Card can\'t be\nrecognized.',
    26: 'Notifications',
    27: 'HOME Menu',
    28: 'Unread',
    29: 'Unread ×%d',
    30: 'SpotPass\nNotifications',
    31: 'Unread ×%d',
    32: 'StreetPass\nNotifications',
    33: QUIT + ' Close',
    34: 'Close',
    35: 'Close',
    36: 'Delete',
    37: '%M/%d %H:%m',
    38: 'Delete data received\nvia StreetPass?',
    39: A + ' Delete',
    40: B + ' Cancel',
    42: 'Don\'t receive notifications\nfrom this software',
    44: ('Notifications from this\nsoftware will no longer\nbe received.\n' + NOTE +
         '(To receive them again, change\nthe setting in the software.)' + NOTE_END + SPACER + 'Is that OK?'),
    47: B + ' Cancel',
    48: A + ' OK',
    49: 'Start Software',
    50: 'Stop StreetPass for this software',
    51: 'To stop StreetPass, use\n"StreetPass Management" in\nSystem Settings.' + SPACER + 'Open System Settings now?',
    52: 'Open Internet Browser',
    53: 'Open the Internet Browser?',
    54: 'The Internet Browser will be\navailable after a system update\nover the Internet.' + SPACER + 'See Nintendo\'s website for\ndetails.',
    55: 'The Internet Browser\ncannot run while software\nis suspended.',
    56: 'The Internet Browser can\'t\nbe started right now.\n\nPress ' + HOME + ' to return to\nthe HOME Menu.',
}
