# SPDX-License-Identifier: GPL-3.0-or-later
from .common import *

SIG = '\n\nNintendo'

def tips7(sleep_line, extra_settings, extra_features):
    return ('Touch "HOME Menu Settings" in\nthe upper left of the HOME\nMenu\'s bottom screen (see\nabove) to change these:\n\n'
            '■Change the HOME Menu theme\n■Display badges* on the\n\u3000HOME Menu\n■Save and load HOME Menu\n■Change screen brightness\n'
            + sleep_line + extra_settings +
            '\nEven while playing Nintendo\n3DS software, you can press\n' + HOME + 'HOME to return to the\nHOME Menu and change these\nsettings anytime.\n\n'
            'You can also:\n\n■Use Image Share\n■Start amiibo Settings\n■Start Nintendo eShop\n■Start System Settings\n'
            + extra_features +
            '\nHandy features to remember!\n\n'
            '*Badges can be displayed once\n you get them from the 3DS\n\u3000download software\n\u3000"Nintendo Badge Arcade".' + SIG)

SD_TIP = ('{sys} uses an {card} to\nstore software, save data,\nphotos and music.\n\n'
          'Always turn the power OFF\nbefore inserting or\nremoving the {card}.\n\n'
          'Inserting or removing the\n{card} while the power is\nON can damage data, so\nplease be careful.')

MICRO_NOTE = '\n\n*A "microSD Card" is a small\n\u3000SD Card. It comes inserted\n\u3000in the system\'s microSD\n\u3000Card slot.'

STEPS_BODY = ('\n\nToday\'s step count appears on\nthe HOME Menu\'s top screen,\nlike "' + STEPS + '12121" (see above).\n\n'
              'You can see your daily step\nhistory in "Activity Log".\n\n'
              'Carry it every day and\nbuild up your records!' + SIG)

COINS_BODY = ('\n100 steps earns 1 Play Coin.\n\n'
              'You can earn up to 10 Play\nCoins a day, and hold up\nto 300 in total.\n\n'
              'Your Play Coin total appears\non the HOME Menu\'s top\nscreen, like "' + COIN + '123" (see above).\n\n'
              'Use Play Coins in StreetPass\nMii Plaza, AR Games and many\nother games to trade for\nitems or get an edge.\n\n'
              'Collect lots of them!' + SIG)

DS_TIP = ('A note for anyone playing\nDS software.\n\n'
          'While DS software is running,\nthe following features\ncan\'t be used:\n\n'
          '{sp}'
          '■Receiving data via SpotPass\n'
          '■HOME Menu features such as\n\u3000Friend List, Notifications\n\u3000and Game Notes' + SIG)

AUTODL = ('{intro}\n\n'
          'If the system sleeps where it\ncan connect to the Internet,\nnew software may appear on\nyour HOME Menu.\nLook forward to it!\n\n'
          '*To receive software, set\nSystem Settings > "Internet\nSettings" > "SpotPass" >\n"Automatically Download\nSoftware" to "Receive".' + SIG)

T = {
    542: 'About Notifications',
    543: ('Hello!\nThis is "Notifications".\n\nHere you\'ll receive:\n'
          '■News from your games\n■News from Nintendo\n■StreetPass results\nand more.\n\n'
          'When new notifications\narrive, the notification\nlight glows blue.\n(It glows green for\nStreetPass.)\n\n'
          'The "Notifications" icon on\nthe HOME Menu\'s bottom screen\nalso shows a "new" mark.\n(See above.)\n\n'
          'When new notifications\narrive, take a look!' + SIG),
    544: 'When inserting or removing\nthe SD Card...',
    545: 'When inserting or removing\nthe microSD Card...',
    546: 'When inserting or removing\nthe microSD Card...',
    547: SD_TIP.format(sys='Nintendo 3DS', card='SD Card') + SIG,
    548: SD_TIP.format(sys='This system', card='microSD Card') + MICRO_NOTE + SIG,
    549: SD_TIP.format(sys='This system', card='microSD Card') + MICRO_NOTE + SIG,
    550: SD_TIP.format(sys='Nintendo 2DS', card='SD Card') + SIG,
    551: 'About Sleep Mode',
    552: ('Closing the system while it\'s\non puts it in "Sleep Mode".\n\n'
          'In Sleep Mode...\n■Your steps are counted\n■Nintendo 3DS software can\n\u3000use StreetPass\n'
          '■SpotPass can receive\n\u3000all kinds of data\n\n'
          'Closing the system during\na game also enters Sleep\nMode, but some Sleep Mode\nfeatures may not work, such\nas while playing DS software.' + SIG),
    553: ('Sliding the sleep switch to\nthe right while the Nintendo\n2DS is on puts it in\n"Sleep Mode".\n\n'
          'In Sleep Mode...\n■Your steps are counted\n■StreetPass and SpotPass\n\u3000work while using\n\u3000less power\n'
          '■Buttons are locked to\n\u3000prevent accidental presses\n\n'
          'You can use Sleep Mode during\na game, but some features\nmay not work, such as while\nplaying DS software.\n\n'
          'Slide the switch back to the\nleft to continue right where\nyou left off.' + SIG),
    554: 'About the Pedometer',
    555: ('This system has a built-in\npedometer.\n\n'
          'Carry it closed with the\npower on, and your steps\nwill be counted.' + STEPS_BODY),
    556: ('The Nintendo 2DS has a\nbuilt-in pedometer.\n\n'
          'Put the Nintendo 2DS in\n"Sleep Mode" and your steps\nwill be counted.' + STEPS_BODY),
    557: 'You earned Play Coins!',
    558: ('Congratulations!\nYou earned your first Play\nCoin!\n\nCarry this system around and' + COINS_BODY),
    559: ('Congratulations!\nYou earned your first Play\nCoin!\n\nCarry the Nintendo 2DS and' + COINS_BODY),
    560: 'When playing DS software...',
    561: DS_TIP.format(sp='■StreetPass in Nintendo 3DS\n\u3000software\n'),
    562: DS_TIP.format(sp='■StreetPass in 3DS software\n'),
    563: 'About Touch Sliding',
    564: ('On the HOME Menu, touch the\nscreen and slide sideways\n(see above) to turn the page\nand show icons hidden to\nthe left and right.\n\n'
          'Other places outside the\nHOME Menu also let you\nslide to turn pages,\nso give it a try!' + SIG),
    565: 'About HOME Menu Settings',
    566: tips7('■Turn Power-Saving Mode\n\u3000ON/OFF\n', '', ''),
    567: tips7('■Turn wireless\n\u3000ON/OFF\n', '', ''),
    568: tips7('■Turn Power-Saving Mode\n\u3000ON/OFF\n', '■Turn wireless ON/OFF\n', '■View the HOME Menu manual\n'),
    569: tips7('■Turn Power-Saving Mode\n\u3000ON/OFF\n', '■Turn wireless ON/OFF\n', '■View the HOME Menu manual\n'),
    576: 'Handy HOME Menu Feature',
    577: ('On the HOME Menu, touch the\nmark in the upper right of\nthe bottom screen (see above)\nto make the software icons\nsmaller or larger.\n\n'
          'Try different sizes to\nfind the HOME Menu that\nsuits you.' + SIG),
    578: 'About the ' + HOME + 'HOME Button',
    579: ('Pressing ' + HOME + 'HOME while playing\na game "suspends" it and\nreturns you to the HOME Menu.\n\n'
          'On the HOME Menu you can\nuse things like "Notifications"\nand "Game Notes" while the\ngame stays suspended.\n\n'
          'To return to the game,\npress ' + HOME + 'HOME again.\n\n'
          'Make good use of the\n' + HOME + 'HOME Button!' + SIG),
    580: 'Software can arrive on its own',
    581: AUTODL.format(intro='This system can automatically\nreceive software via SpotPass.'),
    582: AUTODL.format(intro='The Nintendo 2DS can\nautomatically receive\nsoftware via SpotPass.'),
    585: 'Sharing Screenshots',
    586: ('Screenshots you capture can\nbe shared on social networks\n(SNS).\n\n'
          '■How to share\n\n'
          '\u3000In "HOME Menu Settings" (see\n\u3000above) in the upper left of\n\u3000the bottom screen, choose\n'
          '\u3000"Nintendo 3DS Image Share"\n\u3000and follow the instructions.\n\n'
          '\u3000*Posting requires an\n\u3000\u3000Internet connection and\n\u3000\u3000a login for each SNS.\n\n'
          '\u3000*You can also view captured\n\u3000\u3000images in Nintendo 3DS\n\u3000\u3000Camera under\n\u3000\u3000"View Photos/Videos".' + SIG),
    587: 'Congrats on your first badge!',
    588: ('Use the "Badge Case" to\ndisplay or put away badges\nyou\'ve collected.\n\n'
          'Open the "Badge Case" by:\n\n'
          '■Choosing "Display Badges"\n\u3000in "HOME Menu Settings"\n\u3000(see above) in the upper\n\u3000left of the bottom screen\n'
          '■Touching a displayed badge\n\u3000or pressing ' + A + '\n\n'
          'You can also save a decorated\nHOME Menu with "My HOME Menu"\n(see above) and load it later.\n\n'
          'Try different layouts to make\na HOME Menu you love.' + SIG),
}
