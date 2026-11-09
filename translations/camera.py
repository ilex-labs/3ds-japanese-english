# SPDX-License-Identifier: GPL-3.0-or-later
"""Nintendo 3DS Camera (0004001000020400): msg/JP_Japanese.LZ.

One table per message file, keyed by string number. {{hex}} tokens are
formatting and placeholder codes copied from the original and must stay
as they are."""

MAIN = {  # P.msbt
    0: 'Back',  # back
    1: 'Settings',  # setting
    3: '\ue01e{{0e000200000002000200}}{{0e000300270002000000}}{{0e000200000002000200}}',  # Finder_Pho_00_00
    4: '\ue01e{{0e000200000002000200}}{{0e000300270002000000}}{{0e000200000002000200}}',  # Finder_Pho_00_01
    5: '\ue01e{{0e000200000002000200}}{{0e000300270002000000}}{{0e000200000002000200}}',  # Finder_Pho_00_02
    16: 'frames',  # Finder_Mov_04_00
    17: 'frames',  # Finder_Mov_04_03
    18: 'frames',  # Finder_Mov_04_04
    23: '{{0e0002000100040000000040}}Outer Camera',  # Finder_03
    24: '{{0e0002000100040000000040}}Inner Camera',  # Finder_04
    26: '{{0e0002000100040000000040}}Photo',  # Finder_07
    27: '{{0e0002000100040000000040}}Video',  # Finder_08
    29: 'OK!',  # Finder_Face_03
    30: '{{0e000000020002008c00}}{{0e00000003000400ff3200ff}}OK!{{0e00000003000400454039ff}}{{0e000000020002006400}}',  # Finder_Face_03_01
    31: "Photo failed.\nDon't move until\nthe shutter\nhas clicked.",  # Finder_Face_04
    34: 'Merge Camera',  # Finder_ModeA_Pho_01
    35: 'Sparkle Camera',  # Finder_ModeA_Pho_02
    36: 'Daydream Camera',  # Finder_ModeA_Pho_03
    37: 'Pinhole Camera',  # Finder_ModeA_Pho_04
    38: 'Mystery Camera',  # Finder_ModeA_Pho_06
    39: 'Low-Light Camera',  # Finder_ModeA_Pho_07
    40: 'A normal camera.',  # Finder_ModeA_Pho_EX_00
    41: 'A camera that merges two people. Face each other and capture both faces.',  # Finder_ModeA_Pho_EX_01
    42: 'A camera you decorate by blowing into the mic. Try capturing a face...',  # Finder_ModeA_Pho_EX_02
    43: 'A dreamy camera.',  # Finder_ModeA_Pho_EX_03
    44: 'A camera that keeps the center bright and darkens the edges.',  # Finder_ModeA_Pho_EX_04
    45: "A camera where you never know what photo you'll get.",  # Finder_ModeA_Pho_EX_06
    46: 'A camera that works well in the dark.',  # Finder_ModeA_Pho_EX_07
    48: 'Normal Camera',  # Finder_ModeA_Mov_00
    49: 'Low-Light Camera',  # Finder_ModeA_Mov_01
    50: 'A normal camera.',  # Finder_ModeA_Mov_EX_00
    51: 'A camera that works well in the dark.',  # Finder_ModeA_Mov_EX_01
    53: 'Take Photo',  # Shoot_00
    54: '{{0e00020001000400000040c0}}{{0e000000020002008c00}}\ue004\ue005\ue000{{0e000000020002006400}}{{0e00020001000400000040c0}}{{0e000200000002000200}}: Take a photo',  # Shoot_01
    55: 'Outer Camera',  # Shoot_03
    56: 'Inner Camera',  # Shoot_04
    57: '{{0e000100000002005a00}}View Photos{{0e000100000002006400}}{{0e000100000002004600}}/{{0e000100000002006400}}{{0e000100000002004600}}Videos{{0e000100000002006400}}{{0e000100000002005a00}}{{0e000100000002006400}}',  # Shoot_05
    58: 'Settings',  # Shoot_06
    62: 'Settings',  # Set_Title
    64: 'Save Photos To',  # Set_00
    65: 'Self-Timer Sound',  # Set_01
    66: 'SD Card',  # Set_02
    67: 'System',  # Set_03
    68: 'None',  # Set_04
    69: 'Woof',  # Set_05
    70: 'Meow',  # Set_06
    71: '???',  # Set_07
    72: 'How to Use',  # Set_08
    73: 'Data Management',  # Set_09
    74: 'Color Settings',  # Set_10
    75: 'Show Info',  # Set_11
    76: 'On',  # Set_11_00
    77: 'Off',  # Set_11_01
    79: 'How to Use',  # LctList_00
    80: 'You can read the how-to\ntips shown so far.',  # LctList_01
    82: 'Back',  # LctList_02
    84: 'Data Management',  # Date_00
    85: 'Here you can manage photos,\nvideos and save data.',  # Date_01
    87: '{{0e000100000002005000}}Copy All{{0e000100000002006400}}\n{{0e000100000002004e00}}Photos{{0e000100000002006400}}',  # Date_02
    88: '{{0e000100000002006000}}Delete All{{0e000100000002006400}}',  # Date_03
    89: 'System to SD Card',  # Date_04
    90: 'SD Card to System',  # Date_08
    91: '{{0e000100000002006300}}Reset Save Data{{0e000100000002006400}}',  # Date_05
    92: 'System',  # Date_06
    93: '{{0e000100000002006100}}SD Card{{0e000100000002006400}}',  # Date_07
    99: 'Photos: \nVideos: ',  # Brws_U_01_00
    100: 'Photos: ',  # Brws_U_01_01
    101: 'Videos: ',  # Brws_U_01_02
    102: ' {{0e000300270002000000}}\n {{0e000300270002000100}}',  # Brws_U_02_00
    103: ' {{0e000300270002000000}}',  # Brws_U_02_01
    104: ' {{0e000300270002000000}}',  # Brws_U_02_02
    105: "This photo isn't\nsupported, so it\ncan't be shown.",  # Brws_U_03_00
    106: "This video isn't\nsupported, so it\ncan't be shown.",  # Brws_U_03_01
    107: 'There are no photos\nor videos to show.',  # Brws_U_04
    108: 'Total',  # Brws_U_05
    109: 'Photos: \nVideos: \nDays shot: ',  # Brws_U_06_00
    110: 'Photos: \nDays shot: ',  # Brws_U_06_01
    111: 'Videos: \nDays shot: ',  # Brws_U_06_02
    112: ' {{0e000300270002000100}}\n {{0e000300270002000200}}\n {{0e000300270002000000}}',  # Brws_U_07_00
    113: ' {{0e000300270002000100}}\n {{0e000300270002000000}}',  # Brws_U_07_01
    114: ' {{0e000300270002000100}}\n {{0e000300270002000000}}',  # Brws_U_07_02
    116: 'Slideshow',  # Brws_02
    117: 'Take with Camera',  # Brws_03
    121: 'There are no saved\nphotos or videos.',  # Brws_06
    123: 'Doodle',  # OpePho_00
    124: 'Close',  # OpePho_03
    125: '{{0e000100000002005a00}}Play with Video{{0e000100000002006400}}',  # OpeMov_00
    126: 'Close',  # OpeMov_01
    128: 'Cancel',  # Paint_00
    129: 'Done',  # Paint_01
    130: '{{0e000000020002005a00}}Touch the color you want to use with the stylus.{{0e000000020002006400}}',  # Paint_03
    132: 'Cancel',  # PlayMov_00
    133: 'Save {{0e000100000002004b00}}Frames{{0e000100000002006400}}',  # PlayMov_01
    135: '{{0e0002000100040000004041}}{{0e000000020002008c00}}Random order{{0e000000020002006400}}\n\n{{0e000200010004000000e0c0}}Shows photos.',  # SShow_00_00
    136: '{{0e0002000100040000004041}}{{0e000000020002008c00}}Order taken{{0e000000020002006400}}\n\n{{0e000200010004000000e0c0}}Shows photos.',  # SShow_00_01
    137: '{{0e0002000100040000004041}}{{0e000000020002008c00}}Random order{{0e000000020002006400}}\n\n{{0e000200010004000000e0c0}}Shows videos.',  # SShow_00_02
    138: '{{0e0002000100040000004041}}{{0e000000020002008c00}}Order taken{{0e000000020002006400}}\n\n{{0e000200010004000000e0c0}}Shows videos.',  # SShow_00_03
    139: '{{0e0002000100040000004041}}{{0e000000020002008c00}}Random order{{0e000000020002006400}}\n\n{{0e000200010004000000e0c0}}{{0e000100000002005f00}}Shows photos and videos.{{0e000100000002006400}}',  # SShow_00_04
    140: '{{0e0002000100040000004041}}{{0e000000020002008c00}}Order taken{{0e000000020002006400}}\n\n{{0e000200010004000000e0c0}}{{0e000100000002005f00}}Shows photos and videos.{{0e000100000002006400}}',  # SShow_00_05
    141: 'Theme\n\n{{0e000000020002008c00}}Everything{{0e000000020002006400}}',  # SShow_01_00
    142: 'Theme\n\n{{0e000000020002008c00}}Probably People{{0e000000020002006400}}',  # SShow_01_01
    143: 'Theme\n\n{{0e000000020002008c00}}Probably Men{{0e000000020002006400}}',  # SShow_01_02
    144: 'Theme\n\n{{0e000000020002008c00}}Probably Women{{0e000000020002006400}}',  # SShow_01_03
    145: 'Theme\n\n{{0e000000020002008c00}}Who Are You?{{0e000000020002006400}}',  # SShow_01_04
    146: 'Theme\n\n{{0e000000020002008c00}}Decorated{{0e000000020002006400}}',  # SShow_01_05
    147: 'Theme\n\n{{0e000000020002008c00}}Masterpieces{{0e000000020002006400}}',  # SShow_01_06
    148: 'Theme\n\n{{0e000000020002008c00}}Game Shots{{0e000000020002006400}}',  # SShow_01_07
    149: 'Theme\n\n{{0e000000020002008c00}}Mii{{0e000000020002006400}}',  # SShow_01_08
    150: 'Theme\n\n{{0e000000020002008200}}{{0e0005000000040000009841}}{{0e00030000000000}}{{0e00050001000000}}/{{0e0005000000040000009841}}{{0e00030007000000}}{{0e00050001000000}}/{{0e0005000000040000009841}}{{0e00030008000000}}{{0e00050001000000}}{{0e000000020002006400}}',  # SShow_01_09
    151: 'Theme\n\n{{0e000000020002008200}}{{0e0005000000040000009841}}----{{0e00050001000000}}/{{0e0005000000040000009841}}--{{0e00050001000000}}/{{0e0005000000040000009841}}--{{0e00050001000000}}{{0e000000020002006400}}',  # SShow_01_09_Blnk
    152: 'Effects',  # SShow_02
    153: 'Choose Theme',  # SShow_03
    154: '{{0e000100000002005f00}}Random{{0e000100000002006400}}',  # SShow_04_00
    155: '{{0e000100000002004e00}}In Order{{0e000100000002006400}}',  # SShow_04_01
    159: 'The save data is\ncorrupted.\n\nNew save data will\nbe created.',  # ErrBrkn00
    160: 'OK',  # ErrBrkn_Btn00
    161: 'Creating new\nsave data...',  # ErrBrkn01
    166: 'Photos taken so far:\n{{0e000300270002000000}}',  # FriendCard_Play
    167: 'Photos taken so far:\n{{0e000300270002000000}}',  # FriendCard_Play0
    168: 'Photos taken so far:\n{{0e000300270002000000}}',  # FriendCard_Play1
}

DIALOGS = {  # P_dlg.msbt
    1: '{{0e000000020002007800}}{{0e00000003000400ff3200ff}}Recording{{0e00000003000400454039ff}}{{0e000000020002006400}}',  # RecMovie_00
    2: 'Writing to the SD Card was\ntoo slow, so recording\nstopped.',  # RecMovie_01
    3: 'OK',  # RecMovie_01_Btn0
    4: 'The SD Card ran out\nof space, so recording\nstopped.',  # RecMovie_02
    5: 'OK',  # RecMovie_02_Btn0
    6: 'Shooting failed.',  # RecMovie_04
    7: 'OK',  # RecMovie_04_Btn0
    8: '{{0e00020001000400000040c0}}{{0e000000020002008c00}}\ue004\ue005\ue000{{0e000000020002006400}}{{0e00020001000400000040c0}}{{0e000200000002000200}}: Stop recording',  # RecMovie_03
    9: 'Processing...',  # RecMovie_05
    11: 'Shooting Mode',  # ModeA_Pho_Title
    12: 'Normal Camera',  # ModeA_Pho_00
    13: 'Merge Camera',  # ModeA_Pho_01
    14: 'Sparkle Camera',  # ModeA_Pho_02
    15: 'Daydream Camera',  # ModeA_Pho_03
    16: 'Pinhole Camera',  # ModeA_Pho_04
    17: 'Mystery Camera',  # ModeA_Pho_06
    18: 'Low-Light Camera',  # ModeA_Pho_07
    19: 'Close',  # ModeA_Pho_10
    20: 'Camera Settings',  # ModeA_Pho_11_B
    21: 'Camera Settings',  # ModeA_Pho_11_W
    23: 'Shooting Mode',  # ModeA_Mov_Title
    24: 'Normal Camera',  # ModeA_Mov_00
    25: 'Low-Light Camera',  # ModeA_Mov_01
    27: 'Camera Settings',  # ModeM_Pho_Title
    28: 'Film',  # ModeM_Pho_00
    29: 'Normal',  # ModeM_Pho_00_00
    30: 'B&W',  # ModeM_Pho_00_01
    31: 'Sepia',  # ModeM_Pho_00_02
    32: 'Negative',  # ModeM_Pho_00_03
    33: 'Mystery',  # ModeM_Pho_00_04
    34: '{{0e000100000002006000}}Sharpness{{0e000100000002006400}}',  # ModeM_Pho_01
    35: 'Pattern',  # ModeM_Pho_01_01
    36: '{{0e000000020002005e00}}Contrast{{0e000000020002006400}}',  # ModeM_Pho_02
    37: 'Brightness',  # ModeM_Pho_03
    38: 'Restore',  # ModeM_Pho_04
    39: 'Back',  # ModeM_Pho_05
    41: 'Camera Settings',  # ModeM_Mov_Title
    42: 'Film',  # ModeM_Mov_00
    43: 'Normal',  # ModeM_Mov_00_00
    44: 'B&W',  # ModeM_Mov_00_01
    45: 'Sepia',  # ModeM_Mov_00_02
    46: 'Negative',  # ModeM_Mov_00_03
    47: 'Mystery',  # ModeM_Mov_00_04
    48: '{{0e000100000002006000}}Sharpness{{0e000100000002006400}}',  # ModeM_Mov_01
    49: 'Pattern',  # ModeM_Mov_01_01
    50: '{{0e000000020002005e00}}Contrast{{0e000000020002006400}}',  # ModeM_Mov_02
    51: 'Brightness',  # ModeM_Mov_03
    52: 'Restore',  # ModeM_Mov_04
    53: 'Back',  # ModeM_Mov_05
    55: 'Self-Timer',  # TimS_Title_00
    56: '3-Second Timer',  # TimS_Title_01
    57: '10-Second Timer',  # TimS_Title_02
    58: 'Voice Timer',  # TimS_Title_03
    59: '3 sec',  # TimS_00
    60: '10 sec',  # TimS_01
    61: 'Voice',  # TimS_02
    62: 'Close',  # TimS_03
    63: 'Touch to Start',  # TimS_04
    64: 'Back',  # TimS_05
    65: 'Shoot Again',  # TimS_07
    66: '{{0e00000003000400ff3200ff}}{{0e000000020002009600}}OK{{0e000000020002006400}}\n{{0e00000003000400454039ff}}Say it out loud{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}',  # TimS_09_B
    67: '{{0e000000020002009600}}OK{{0e000000020002006400}}\nSay it out loud',  # TimS_09_W
    69: 'Special Videos',  # Sfx_Title
    70: '{{0e000100000002004600}}Interval{{0e000100000002006400}}',  # Sfx_00
    71: 'Stop Motion',  # Sfx_01
    72: '{{0e000100000002004600}}Best Moments{{0e000100000002006400}}',  # Sfx_02
    73: 'Close',  # Sfx_03
    74: 'Shoot Again',  # Sfx_04
    75: 'Back',  # Sfx_05
    76: 'Interval Shooting',  # Sfx_Int_Title
    77: 'Interval',  # Sfx_Int_00
    78: '0.5 sec',  # Sfx_Int_00_00
    79: '2 sec',  # Sfx_Int_00_01
    80: '5 sec',  # Sfx_Int_00_02
    81: '15 sec',  # Sfx_Int_00_03
    82: '60 sec',  # Sfx_Int_00_04
    83: 'Touch to Start',  # Sfx_Int_01
    84: 'Back',  # Sfx_Int_02
    85: 'Done',  # Sfx_Int_03
    86: '{{0e000300270002000000}}-sec interval shooting',  # Sfx_Int_04
    87: '0.5-sec interval shooting',  # Sfx_Int_07
    88: 'Shooting in...',  # Sfx_Int_05
    89: '{{0e000300290002000000}} sec',  # Sfx_Int_06
    90: '{{0e00000003000400ff3200ff}}{{0e000000020002007800}}Recording{{0e000000020002006400}}{{0e00000003000400454039ff}}',  # Sfx_Int_08
    91: 'Stop Motion',  # Sfx_Stp_Title
    94: 'Back',  # Sfx_Stp_02
    97: 'Shoot',  # Sfx_Stp_05
    98: 'Done',  # Sfx_Stp_06
    99: 'Best Moments',  # Sfx_Mclp_Title
    101: '{{0e00020001000400000040c0}}{{0e000000020002008c00}}\ue004\ue005\ue000{{0e000000020002006400}}{{0e00020001000400000040c0}}{{0e000200000002000200}}: Shoot',  # Sfx_Mclp_00_00
    102: '{{0e00020001000400000040c0}}{{0e000000020002008c00}}\ue004\ue005\ue000{{0e000000020002006400}}{{0e00020001000400000040c0}}{{0e000200000002000200}}: Pause',  # Sfx_Mclp_00_01
    103: '{{0e00020001000400000040c0}}{{0e000000020002008c00}}\ue004\ue005\ue000{{0e000000020002006400}}{{0e00020001000400000040c0}}{{0e000200000002000200}}: Resume',  # Sfx_Mclp_00_02
    105: '{{0e000000020002007800}}{{0e00000003000400ff3200ff}}Recording{{0e00000003000400454039ff}}{{0e000000020002006400}}',  # Sfx_Mclp_01_00
    106: 'Paused',  # Sfx_Mclp_01_01
    108: 'Back',  # Sfx_Mclp_02
    109: 'Done',  # Sfx_Mclp_03
    111: 'This photo will be copied\nfrom the system to the\nSD Card.\n\nIs that OK?',  # Copy_NS_Pho_00
    112: 'Copy',  # Copy_NS_Pho_00_Btn0
    113: 'Cancel',  # Copy_NS_Pho_00_Btn1
    115: 'This photo will be copied\nfrom the SD Card to\nthe system.\n\nIs that OK?',  # Copy_SN_Pho_00
    116: 'Copy',  # Copy_SN_Pho_00_Btn0
    117: 'Cancel',  # Copy_SN_Pho_00_Btn1
    118: "The system's photo\nstorage is full, so it\ncan't be copied.",  # Copy_SN_Pho_02
    119: 'OK',  # Copy_SN_Pho_02_Btn0
    120: "This photo can't be used\nin DSi-compatible\nsoftware.",  # Copy_SN_Pho_03
    121: 'OK',  # Copy_SN_Pho_03_Btn0
    123: 'This photo will be\ndeleted.\n\nIs that OK?',  # Delete_Pho_00
    124: 'Delete',  # Delete_Pho_00_Btn0
    125: 'Cancel',  # Delete_Pho_00_Btn1
    127: 'This video will be\ndeleted.\n\nIs that OK?',  # Delete_Mov_00
    128: 'Delete',  # Delete_Mov_00_Btn0
    129: 'Cancel',  # Delete_Mov_00_Btn1
    131: 'Pencil',  # Paint_Title_01
    132: 'Close',  # Paint_01_00
    133: 'Eraser',  # Paint_Title_02
    134: 'Close',  # Paint_02_00
    135: 'Erase All',  # Paint_02_01
    136: 'Stamps',  # Paint_Title_03
    137: 'Close',  # Paint_03_00
    138: 'Fluffy Pen',  # Paint_Title_04
    139: 'Close',  # Paint_04_00
    141: "Quit doodling?\n\nYour doodle won't\nbe saved.\n\nIs that OK?",  # Paint_Quit_00
    142: 'No',  # Paint_Quit_00_Btn0
    143: 'Yes',  # Paint_Quit_00_Btn1
    145: 'Finish your doodle?\n\nIt will be saved as\na new photo.\n\nIs that OK?',  # Paint_Comp_00
    146: 'No',  # Paint_Comp_00_Btn0
    147: 'Yes',  # Paint_Comp_00_Btn1
    149: "Couldn't play it.",  # PlayVideo_Error
    150: 'OK',  # PlayVideo_Error_Btn0
    152: 'The image shown will be\nsaved as a photo.\n\nIs that OK?',  # FrameSave_00
    153: 'No',  # FrameSave_00_Btn0
    154: 'Yes',  # FrameSave_00_Btn1
    155: 'Saving the image...',  # FrameSave_01
    156: "System Memory's photo\nstorage is full, so\nthe image can't\nbe saved.",  # FrameSave_02
    157: 'OK',  # FrameSave_02_Btn0
    158: "System Memory's photo\nstorage is full, so\nthe image can't\nbe saved.\n\n*Switch photo storage\nto the SD Card?",  # FrameSave_03
    159: 'No',  # FrameSave_03_Btn0
    160: 'Yes',  # FrameSave_03_Btn1
    161: "The SD Card is full of\nphotos and videos, so\nthe image can't\nbe saved.",  # FrameSave_04
    162: 'OK',  # FrameSave_04_Btn0
    163: "The SD Card is full of\nphotos and videos, so\nthe image can't\nbe saved.\n\n*Switch photo storage\nto the system?",  # FrameSave_05
    164: 'No',  # FrameSave_05_Btn0
    165: 'Yes',  # FrameSave_05_Btn1
    166: "There isn't enough free\nspace on the SD Card, so\nthe image\ncan't be saved.",  # FrameSave_06
    167: 'OK',  # FrameSave_06_Btn0
    168: "There isn't enough free\nspace on the SD Card, so\nthe image\ncan't be saved.\n\n*Switch photo storage\nto the system?",  # FrameSave_07
    169: 'No',  # FrameSave_07_Btn0
    170: 'Yes',  # FrameSave_07_Btn1
    172: 'Save Photos To',  # Set_Storage_Title
    173: 'System',  # Set_Storage_00_B
    174: 'System',  # Set_Storage_00_W
    175: 'SD Card',  # Set_Storage_01_B
    176: 'SD Card',  # Set_Storage_01_W
    177: 'Photos left: {{0e0005000000040000007041}}{{0e0003002d0002000000}}',  # Set_Storage_02
    178: 'OK',  # Set_Storage_03
    180: 'Self-Timer Sound',  # Set_Shutter_Title
    181: 'None',  # Set_Shutter_00_B
    182: 'None',  # Set_Shutter_00_W
    183: '???',  # Set_Shutter_01_B
    184: '???',  # Set_Shutter_01_W
    185: 'Meow',  # Set_Shutter_02_B
    186: 'Meow',  # Set_Shutter_02_W
    187: 'Woof',  # Set_Shutter_03_B
    188: 'Woof',  # Set_Shutter_03_W
    189: 'OK',  # Set_Shutter_04
    191: 'Show Info',  # Set_Info_Title
    192: 'On',  # Set_Info_00_B
    193: 'On',  # Set_Info_00_W
    194: 'Off',  # Set_Info_01_B
    195: 'Off',  # Set_Info_01_W
    196: 'Shows extra info on\nthe top screen.',  # Set_Info_02_00
    197: 'Hides the extra info\non the top screen.',  # Set_Info_02_01
    198: 'OK',  # Set_Info_03
    200: "The SD Card can't\nbe recognized.",  # Data_NoSd_00
    201: 'OK',  # Data_NoSd_00_Btn0
    202: 'There are no photos.',  # Data_NoData_00
    203: 'OK',  # Data_NoData_00_Btn0
    204: 'There are no saved\nphotos or videos.',  # Data_NoData_01
    205: 'OK',  # Data_NoData_01_Btn0
    206: "The SD Card is\nwrite-protected.\n\nTurn the power off and\nslide the SD Card's\nlock switch to unlock it.",  # Data_ProhibitedSd_00
    207: 'OK',  # Data_ProhibitedSd_00_Btn0
    208: "The SD Card's management\nfile is read-only, so\nthis can't be done.",  # Data_ReadOnlySd_00
    209: 'OK',  # Data_ReadOnlySd_00_Btn0
    211: 'All photos will be\ncopied.\n\nIs that OK?',  # Data_Copy_00_00
    212: 'All photos will be\ncopied. Is that OK?\n\nThis may take a few\ndozen seconds.',  # Data_Copy_00_01
    213: 'All photos will be\ncopied. Is that OK?\n\nThis may take a\nfew minutes.',  # Data_Copy_00_02
    214: 'All photos will be\ncopied. Is that OK?\n\nThis may take more\nthan 3 minutes.',  # Data_Copy_00_03
    215: 'No',  # Data_Copy_00_Btn0
    216: 'Yes',  # Data_Copy_00_Btn1
    217: 'Not all photos may\nbe copied.\nIs that OK?',  # Data_Copy_01_00
    218: 'Not all photos may\nbe copied. Is that OK?\n\nThis may take a few\ndozen seconds.',  # Data_Copy_01_01
    219: 'Not all photos may\nbe copied. Is that OK?\n\nThis may take a\nfew minutes.',  # Data_Copy_01_02
    220: 'Not all photos may\nbe copied. Is that OK?\n\nThis may take more\nthan 3 minutes.',  # Data_Copy_01_03
    221: 'No',  # Data_Copy_01_Btn0
    222: 'Yes',  # Data_Copy_01_Btn1
    223: "Videos on the SD Card\nwon't be copied to\nthe system.",  # Data_Copy_02
    224: 'OK',  # Data_Copy_02_Btn0
    225: "Copying to the\nSD Card. Don't remove\nthe SD Card.",  # Data_CopyingSd
    226: 'Cancel',  # Data_CopyingSd_Btn0
    227: "Copying to the system.\n\nDon't remove\nthe SD Card.",  # Data_CopyingNand
    228: 'Cancel',  # Data_CopyingNand_Btn0
    229: 'Copying paused.\n\nStop copying here?',  # Data_Copy_Quit_00
    230: 'No',  # Data_Copy_Quit_00_Btn0
    231: 'Yes',  # Data_Copy_Quit_00_Btn1
    232: 'Copying stopped.',  # Data_Copy_Quit_01
    233: 'OK',  # Data_Copy_Quit_01_Btn0
    234: 'Copying complete.',  # Data_Copy_Finish
    235: 'OK',  # Data_Copy_Finish_Btn0
    236: 'Copying failed.',  # Data_Copy_Failure_00
    237: 'OK',  # Data_Copy_Failure_00_Btn0
    238: "Copying complete.\n\nHowever, some data\ncouldn't be copied.",  # Data_Copy_Failure_01
    239: 'OK',  # Data_Copy_Failure_01_Btn0
    240: "There isn't enough free\nspace in the system, so\nit couldn't be copied.",  # Data_Copy_Failure_02
    241: 'OK',  # Data_Copy_Failure_02_Btn0
    242: "There isn't enough free\nspace on the SD Card, so\nit couldn't be copied.",  # Data_Copy_Failure_03
    243: 'OK',  # Data_Copy_Failure_03_Btn0
    244: "The SD Card has too many\nphoto folders, so\nit couldn't be saved.",  # Data_Copy_Failure_04
    245: 'OK',  # Data_Copy_Failure_04_Btn0
    247: "All photos in the system\nwill be deleted. Deleted\nphotos can't be restored.\n\nIs that OK?",  # Data_DeleteNand_00
    248: 'Cancel',  # Data_DeleteNand_00_Btn0
    249: 'Delete',  # Data_DeleteNand_00_Btn1
    250: "All photos and videos on\nthe SD Card will be deleted.\n*Including ones not taken\nwith 3DS Camera. They\ncan't be restored.",  # Data_DeleteSd_00
    251: 'Cancel',  # Data_DeleteSd_00_Btn0
    252: 'Delete',  # Data_DeleteSd_00_Btn1
    253: 'Really delete?',  # Data_Delete_00_00
    254: 'Really delete?\n\nThis may take a few\ndozen seconds.',  # Data_Delete_00_01
    255: 'Really delete?\n\nThis may take a\nfew minutes.',  # Data_Delete_00_02
    256: 'Really delete?\n\nThis may take more\nthan 3 minutes.',  # Data_Delete_00_03
    257: 'Delete',  # Data_Delete00_Btn0
    258: 'Cancel',  # Data_Delete_00_Btn1
    259: 'Deleting...\n\nPlease wait.',  # Data_Deleting
    260: 'Cancel',  # Data_Deleting_Btn0
    261: 'Deleting paused.\n\nStop deleting here?',  # Data_Delete_Quit_00
    262: 'No',  # Data_Delete_Quit_00_Btn0
    263: 'Yes',  # Data_Delete_Quit_00_Btn1
    264: 'Deleting stopped.',  # Data_Delete_Quit_01
    265: 'OK',  # Data_Delete_Quit_01_Btn0
    266: 'Deleted.',  # Data_Delete_Finish
    267: 'OK',  # Data_Delete_Finish_Btn0
    268: 'Delete failed.',  # Data_Delete_Failure_00
    269: 'OK',  # Data_Delete_Failure_00_Btn0
    270: "Some data couldn't\nbe deleted.",  # Data_Delete_Failure_01
    271: 'OK',  # Data_Delete_Failure_01_Btn0
    273: "Reset the save data?\n\n*Photos and videos\nwon't be deleted.",  # Data_DeleteSavedata_02
    274: 'No',  # Data_DeleteSavedata_02_Btn0
    275: 'Yes',  # Data_DeleteSavedata_02_Btn1
    276: "The save data will be\nreset. Once reset,\nit can't be restored.\n\nAre you sure?",  # Data_DeleteSavedata_00
    277: 'Cancel',  # Data_DeleteSavedata_00_Btn0
    278: 'Reset',  # Data_DeleteSavedata_00_Btn1
    279: 'This is the final check.\n\nReally reset?',  # Data_DeleteSavedata_01
    280: 'Reset',  # Data_DeleteSavedata_01_Btn0
    281: 'Cancel',  # Data_DeleteSavedata_01_Btn1
    282: 'Resetting...\nPlease wait.',  # Data_DeletingSavedata
    283: 'Reset complete.',  # Data_DeleteSavedata_Finish
    284: 'OK',  # Data_DeleteSavedata_Finish_Btn0
    286: 'Sample',  # Set_Color_00
    287: 'Color Settings',  # Set_Color_Title
    288: 'Cancel',  # Set_Color_Btn0
    289: 'OK',  # Set_Color_Btn1
    290: 'Reset',  # Set_Color_Btn2
    296: 'There are no photos or\nvideos to show.\n\nThe slideshow\nwill end.',  # SShow_NoData_01
    297: 'OK',  # SShow_NoData_01_Btn0
    299: 'Choose Theme',  # SShow_Theme_Title
    300: 'Everything',  # SShow_Theme_00_00
    301: 'Probably People',  # SShow_Theme_00_01
    302: 'Probably Men',  # SShow_Theme_00_02
    303: 'Probably Women',  # SShow_Theme_00_03
    304: 'Who Are You?',  # SShow_Theme_00_04
    305: 'Decorated',  # SShow_Theme_00_05
    306: 'Masterpieces',  # SShow_Theme_00_06
    307: 'Game Shots',  # SShow_Theme_00_07
    308: 'Mii',  # SShow_Theme_00_08
    309: '○○○○/○○/○○',  # SShow_Theme_00_09
    310: 'OK',  # SShow_Theme_01
    311: 'Close',  # SShow_Theme_02
    312: 'Display Settings',  # SShow_Theme_03
    314: 'Display Settings',  # SShow_Image_Title
    315: 'Photos and Videos',  # SShow_Image_00_00
    316: 'Photos and Videos',  # SShow_Image_00_01
    317: 'Photos',  # SShow_Image_01_00
    318: 'Photos',  # SShow_Image_01_01
    319: 'Videos',  # SShow_Image_02_00
    320: 'Videos',  # SShow_Image_02_01
    321: 'OK',  # SShow_Image_03
    323: 'Effects',  # SShow_Set_Title
    324: 'Music',  # SShow_Set_00
    325: 'Silent',  # SShow_Set_00_00
    326: 'Breeze',  # SShow_Set_00_01
    327: 'Colorful',  # SShow_Set_00_02
    328: 'Street',  # SShow_Set_00_03
    329: 'Doze',  # SShow_Set_00_04
    330: 'Ceremony',  # SShow_Set_00_05
    331: 'Chic',  # SShow_Set_00_06
    332: 'Memories',  # SShow_Set_00_07
    333: 'Comedy',  # SShow_Set_00_08
    334: 'Motion',  # SShow_Set_01
    335: 'Moving',  # SShow_Set_01_00
    336: 'Still',  # SShow_Set_01_01
    337: 'Display Time',  # SShow_Set_02
    338: 'Flip',  # SShow_Set_02_00
    339: '3 sec',  # SShow_Set_02_01
    340: '10 sec',  # SShow_Set_02_02
    341: '1 min',  # SShow_Set_02_03
    342: '3 min',  # SShow_Set_02_04
    343: 'Transition',  # SShow_Set_03
    344: 'Dissolve',  # SShow_Set_03_00
    345: 'Shutter',  # SShow_Set_03_01
    346: 'Soft',  # SShow_Set_03_02
    347: 'Page',  # SShow_Set_03_03
    348: 'Random',  # SShow_Set_03_04
    349: 'OK',  # SShow_Set_05
    351: 'The SD Card was removed.\n\nPlease turn the system\noff before removing\nthe SD Card.',  # RemovedSd
    352: 'OK',  # RemovedSd_Btn0
    353: 'The SD Card was removed.\nUnlock its write\nprotection to use it.\nPlease turn the system\noff before removing\nthe SD Card.',  # RemovedSd_01
    354: 'OK',  # RemovedSd_01_Btn0
    357: 'Photo storage switched\nto the system.\n\nPhotos you take will be\nsaved in the system.',  # SetNand_Pho_00
    358: 'OK',  # SetNand_Pho_00_Btn0
    359: 'Photo storage switched\nto the system.\n\nDoodled photos will be\nsaved in the system.',  # SetNand_Pho_01
    360: 'OK',  # SetNand_Pho_01_Btn0
    361: 'Photo storage switched\nto the system.\n\nRecording videos needs\nan SD Card.',  # SetNand_Mov_00
    362: 'OK',  # SetNand_Mov_00_Btn0
    364: 'Checking the SD Card...',  # CheckSd
    365: 'An SD Card was found.\n\nSwitch photo storage\nto the SD Card?',  # FindSd
    366: 'No',  # FindSd_Btn0
    367: 'Yes',  # FindSd_Btn1
    368: 'An SD Card was\nfound.',  # FindSd_01
    369: 'OK',  # FindSd_01_Btn0
    370: "The SD Card can't\nbe recognized.",  # NotSd
    371: 'OK',  # NotSd_Btn0
    372: "The SD Card is\nwrite-protected.\n\nTurn the power off and\nslide the SD Card's\nlock switch to unlock it.",  # ProhibitedSd
    373: 'OK',  # ProhibitedSd_Btn0
    374: "The SD Card's management\nfile is read-only.",  # ReadOnlySd
    375: 'OK',  # ReadOnlySd_Btn0
    376: 'Photo storage switched\nto the SD Card.\n\nPhotos you take will be\nsaved on the SD Card.',  # SetSd_Pho_00
    377: 'OK',  # SetSd_Pho_00_Btn0
    378: 'Photo storage switched\nto the SD Card.\n\nDoodled photos will be\nsaved on the SD Card.',  # SetSd_Pho_01
    379: 'OK',  # SetSd_Pho_01_Btn0
    381: 'An SD Card was found.\nIts management file\nneeds to be updated.\n*This may take a while.',  # ImageDb_00
    382: 'OK',  # ImageDb_00_Btn0
    383: 'Updating...\n\nPlease wait.',  # ImageDb_01
    384: 'The management file\nwas updated.\n\nSwitch photo storage\nto the SD Card?',  # ImageDb_02
    385: 'No',  # ImageDb_02_Btn0
    386: 'Yes',  # ImageDb_02_Btn1
    387: 'The management file\nneeds to be updated.\n\n*This may take a while.',  # ImageDb_03
    388: 'OK',  # ImageDb_03_Btn0
    389: 'The management file\nwas updated.',  # ImageDb_04
    390: 'OK',  # ImageDb_04_Btn0
    391: "There isn't enough free\nspace on the SD Card, so\nthe management file\ncouldn't be created.",  # MakeImageDb_Failure
    392: 'OK',  # MakeImageDb_Failure_Btn0
    394: 'Something went wrong\nwith the SD Card.',  # FailureSd
    395: 'OK',  # FailureSd_Btn0
    397: "System Memory's photo\nstorage is full, so\nyou can't\ntake photos.",  # Shoot_FullNand_Pho
    398: 'OK',  # Shoot_FullNand_Pho_Btn0
    399: "System Memory's photo\nstorage is full, so\nyou can't\ntake photos.\n\n*Switch photo storage\nto the SD Card?",  # Shoot_FullNand_Pho_01
    400: 'No',  # Shoot_FullNand_Pho_01_Btn0
    401: 'Yes',  # Shoot_FullNand_Pho_01_Btn1
    402: "System Memory's photo\nstorage is full, so\nthe doodle\ncan't be saved.",  # Paint_FullNand_Pho
    403: 'OK',  # Paint_FullNand_Pho_Btn0
    404: "System Memory's photo\nstorage is full, so\nthe doodle\ncan't be saved.\n\n*Switch photo storage\nto the SD Card?",  # Paint_FullNand_Pho_01
    405: 'No',  # Paint_FullNand_Pho_01_Btn0
    406: 'Yes',  # Paint_FullNand_Pho_01_Btn1
    407: "System Memory's photo\nstorage is full, so\nit can't\nbe copied.",  # Data_Copy_FullNand_Pho
    408: 'OK',  # Data_Copy_FullNand_Pho_Btn0
    409: "System Memory's photo\nstorage is full, so\nit can't\nbe copied.",  # Copy_SN_FullNand_Pho
    410: 'OK',  # Copy_SN_FullNand_Pho_Btn0
    411: "System Memory's photo\nstorage is now full.\n\nNo more photos can\nbe saved.",  # FullNand_Pho_00
    412: 'OK',  # FullNand_Pho_00_Btn0
    413: "System Memory's photo\nstorage is now full.\nNo more photos can\nbe saved.\n\n*Switch photo storage\nto the SD Card?",  # FullNand_Pho_01
    414: 'No',  # FullNand_Pho_01_Btn0
    415: 'Yes',  # FullNand_Pho_01_Btn1
    417: "The SD Card is full of\nphotos and videos, so\nyou can't\ntake photos.",  # Shoot_FullSd_Pho
    418: 'OK',  # Shoot_FullSd_Pho_Btn0
    419: "The SD Card is full of\nphotos and videos, so\nyou can't\ntake photos.\n\n*Switch photo storage\nto the system?",  # Shoot_FullSd_Pho_01
    420: 'No',  # Shoot_FullSd_Pho_01_Btn0
    421: 'Yes',  # Shoot_FullSd_Pho_01_Btn1
    422: "The SD Card is full of\nphotos and videos, so\nthe doodle\ncan't be saved.",  # Paint_FullSd_Pho
    423: 'OK',  # Paint_FullSd_Pho_Btn0
    424: "The SD Card is full of\nphotos and videos, so\nthe doodle\ncan't be saved.\n\n*Switch photo storage\nto the system?",  # Paint_FullSd_Pho_01
    425: 'No',  # Paint_FullSd_Pho_01_Btn0
    426: 'Yes',  # Paint_FullSd_Pho_01_Btn1
    427: "The SD Card is full of\nphotos and videos, so\nit can't\nbe copied.",  # Data_Copy_FullSd_Pho
    428: 'OK',  # Data_Copy_FullSd_Pho_Btn0
    429: "The SD Card is full of\nphotos and videos, so\nit can't\nbe copied.",  # Copy_NS_FullSd_Pho
    430: 'OK',  # Copy_NS_FullSd_Pho_Btn0
    431: 'The SD Card is now full of\nphotos and videos.\n\nNo more can be saved.',  # FullSd_Pho_00
    432: 'OK',  # FullSd_Pho_00_Btn0
    433: 'The SD Card is now full of\nphotos and videos.\nNo more can be saved.\n\n*Switch photo storage\nto the system?',  # FullSd_Pho_01
    434: 'No',  # FullSd_Pho_01_Btn0
    435: 'Yes',  # FullSd_Pho_01_Btn1
    437: "There isn't enough free\nspace on the SD Card, so\nyou can't\ntake photos.",  # Shoot_NoSpaceSd
    438: 'OK',  # Shoot_NoSpaceSd_Btn0
    439: "There isn't enough free\nspace on the SD Card, so\nyou can't\ntake photos.\n\n*Switch photo storage\nto the system?",  # Shoot_NoSpaceSd_01
    440: 'No',  # Shoot_NoSpaceSd_01_Btn0
    441: 'Yes',  # Shoot_NoSpaceSd_01_Btn1
    442: "There isn't enough free\nspace on the SD Card, so\nthe doodle\ncan't be saved.",  # Paint_NoSpaceSd
    443: 'OK',  # Paint_NoSpaceSd_Btn0
    444: "There isn't enough free\nspace on the SD Card, so\nthe doodle\ncan't be saved.\n\n*Switch photo storage\nto the system?",  # Paint_NoSpaceSd_01
    445: 'No',  # Paint_NoSpaceSd_01_Btn0
    446: 'Yes',  # Paint_NoSpaceSd_01_Btn1
    447: "There isn't enough free\nspace on the SD Card, so\nit can't\nbe copied.",  # Data_Copy_NoSpaceSd
    448: 'OK',  # Data_Copy_NoSpaceSd_Btn0
    449: "There isn't enough free\nspace on the SD Card, so\nit can't\nbe copied.",  # Copy_NS_NoSpaceSd
    450: 'OK',  # Copy_NS_NoSpaceSd_Btn0
    451: 'The SD Card has run\nout of space.\n\nNo more can be saved.',  # NoSpaceSd_00
    452: 'OK',  # NoSpaceSd_00_Btn0
    453: 'The SD Card has run\nout of space.\nNo more can be saved.\n\n*Switch photo storage\nto the system?',  # NoSpaceSd_01
    454: 'No',  # NoSpaceSd_01_Btn0
    455: 'Yes',  # NoSpaceSd_01_Btn1
    457: "The SD Card has too many\nphoto folders, so\nit couldn't be saved.",  # FullFolder_01_01
    458: 'OK',  # FullFolder_01_01_Btn0
    459: "The SD Card has too many\nphoto folders, so\nit couldn't be saved.\n\n*Switch photo storage\nto the system?",  # FullFolder_01_02
    460: 'No',  # FullFolder_01_02_Btn0
    461: 'Yes',  # FullFolder_01_02_Btn1
    462: "The SD Card has too many\nphoto folders, so\nthe doodle\ncouldn't be saved.",  # FullFolder_02_01
    463: 'OK',  # FullFolder_02_01_Btn0
    464: "The SD Card has too many\nphoto folders, so\nthe doodle\ncouldn't be saved.\n\n*Switch photo storage\nto the system?",  # FullFolder_02_02
    465: 'No',  # FullFolder_02_02_Btn0
    466: 'Yes',  # FullFolder_02_02_Btn1
    467: "The SD Card has too many\nvideo folders, so\nyou can't record.",  # FullFolder_03_01
    468: 'OK',  # FullFolder_03_01_Btn0
    470: 'Getting ready...\nPlease wait.\n\n*This may take a while.',  # Boot_01
    471: "The SD Card can't\nbe recognized.\n\nPhoto storage will switch\nto the system. Photos you\ntake will be saved there.",  # Boot_02
    472: 'OK',  # Boot_02_Btn0
    473: 'Photo storage will switch\nto the system. Photos you\ntake will be saved there.',  # Boot_03
    474: 'OK',  # Boot_03_Btn0
    475: "The SD Card can't\nbe recognized.",  # Boot_04
    476: 'OK',  # Boot_04_Btn0
}

GUIDE = {  # P_tips.msbt
    1: '/ {{0e000300270002000000}}',  # Guide_D_00_00
    3: 'OK',  # Guide_D_O_Btn0
    4: 'Cancel',  # Guide_D_CN_Btn0
    5: 'Next',  # Guide_D_CN_Btn1
    6: 'Next',  # Guide_D_N_Btn0
    7: 'Back',  # Guide_D_BN_Btn0
    8: 'Next',  # Guide_D_BN_Btn1
    9: 'Back',  # Guide_D_BO_Btn0
    10: 'OK',  # Guide_D_BO_Btn1
    12: '???',  # T_001_S
    13: '{{0e0003002a0002000000}} Stay at Least 30 cm Away',  # T_001
    14: '{{0e0003002a0002000000}} 3D Focus When Shooting',  # T_002
    15: '{{0e0003002a0002000000}} Welcome to 3DS Camera!',  # T_003
    16: '{{0e0003002a0002000000}} Showing the Level',  # T_004
    17: '{{0e0003002a0002000000}} Outer and Inner Cameras',  # T_005
    18: '{{0e0003002a0002000000}} 3D Focus When Viewing',  # T_006
    19: '{{0e0003002a0002000000}} Grouping Photos and Videos',  # T_007
    21: '{{0e0003002a0002000000}} Watching a Slideshow',  # T_009
    22: '{{0e0003002a0002000000}} Rereading the Tips',  # T_010
    23: '{{0e0003002a0002000000}} How to Quit',  # T_011
    24: '{{0e0003002a0002000000}} The Red Lever',  # T_012
    25: '{{0e0003002a0002000000}} Viewing Photos and Videos in 3D',  # T_013
    26: '{{0e0003002a0002000000}} Photos in Other Software',  # T_014
    27: '{{0e0003002a0002000000}} Doodle: Fluffy Pen',  # T_015
    28: '{{0e0003002a0002000000}} Settings: Color Settings',  # T_016
    29: '{{0e0003002a0002000000}} Settings: Self-Timer Sound',  # T_017
    30: '{{0e0003002a0002000000}} Using the Level',  # T_018
    31: '{{0e0003002a0002000000}} Self-Timer',  # T_019
    32: '{{0e0003002a0002000000}} Merge Camera',  # T_020
    33: '{{0e0003002a0002000000}} Sparkle Camera',  # T_021
    34: '{{0e0003002a0002000000}} Daydream Camera',  # T_022
    35: '{{0e0003002a0002000000}} Pinhole Camera',  # T_023
    37: '{{0e0003002a0002000000}} Mystery Camera',  # T_025
    38: '{{0e0003002a0002000000}} Low-Light Camera',  # T_026
    39: '{{0e0003002a0002000000}} Camera Settings',  # T_027
    40: '{{0e0003002a0002000000}} Settings: Save Photos To',  # T_028
    41: '{{0e0003002a0002000000}} 3D Depth Slider',  # T_029
    42: '{{0e0003002a0002000000}} The 3D Mark',  # T_030
    43: '{{0e0003002a0002000000}} Camera Settings: Film',  # T_031
    44: '{{0e0003002a0002000000}} Camera Settings: Sharpness',  # T_032
    45: '{{0e0003002a0002000000}} Camera Settings: Contrast',  # T_033
    46: '{{0e0003002a0002000000}} Camera Settings: Brightness',  # T_034
    47: '{{0e0003002a0002000000}} 3D Tips: Stay in Frame',  # T_035
    48: '{{0e0003002a0002000000}} 3D Tips: Vertical Lines',  # T_036
    49: '{{0e0003002a0002000000}} 3D Tips: Haze',  # T_037
    50: '{{0e0003002a0002000000}} 3D Tips: Clutter',  # T_038
    51: '{{0e0003002a0002000000}} 3D Tips: See-Through',  # T_039
    52: '{{0e0003002a0002000000}} 3D Tips: Near and Far',  # T_040
    53: '{{0e0003002a0002000000}} The Photo and Video Menu',  # T_041
    54: '{{0e0003002a0002000000}} Slideshow: Effects',  # T_042
    55: '{{0e0003002a0002000000}} Inserting and Removing SD Cards',  # T_043
    56: '{{0e0003002a0002000000}} A Capable Parakeet',  # T_044
    57: '{{0e0003002a0002000000}} Tip: Shutter Buttons',  # T_045
    58: '{{0e0003002a0002000000}} Number of Photos Shown',  # T_046
    59: '{{0e0003002a0002000000}} Camera Settings and Merge Camera',  # T_047
    60: '{{0e0003002a0002000000}} More on Merge Camera',  # T_048
    61: '{{0e0003002a0002000000}} More on Sparkle Camera',  # T_049
    63: '{{0e0003002a0002000000}} Tip: Switch Shoot and View',  # T_051
    64: '{{0e0003002a0002000000}} Improve Your Skills',  # T_052
    65: '{{0e0003002a0002000000}} Photo Class: Camera Shake',  # T_053
    66: '{{0e0003002a0002000000}} Photo Class: Avoiding Shake',  # T_054
    67: '{{0e0003002a0002000000}} Photo Class: Balance',  # T_055
    68: '{{0e0003002a0002000000}} Photo Class: Gaze and Composition',  # T_056
    69: '{{0e0003002a0002000000}} Photo Class: Change Your Eye Level',  # T_057
    70: '{{0e0003002a0002000000}} Slideshow: Themes',  # T_058
    71: '{{0e0003002a0002000000}} Photo Class: Backgrounds',  # T_059
    72: '{{0e0003002a0002000000}} Photo Class: Angles',  # T_060
    73: '{{0e0003002a0002000000}} Photo Class: Natural Shots',  # T_061
    74: '{{0e0003002a0002000000}} Photo Class: Shoot a Lot',  # T_062
    75: '{{0e0003002a0002000000}} Sepia × Sparkle',  # T_063
    76: '{{0e0003002a0002000000}} Photo Class: Backlight',  # T_064
    77: '{{0e0003002a0002000000}} What to Shoot: Walks',  # T_065
    78: '{{0e0003002a0002000000}} What to Shoot: Flowers',  # T_066
    79: '{{0e0003002a0002000000}} What to Shoot: Animals',  # T_067
    80: '{{0e0003002a0002000000}} What to Shoot: Meals',  # T_068
    81: '{{0e0003002a0002000000}} What to Shoot: The Sky',  # T_069
    82: '{{0e0003002a0002000000}} What to Shoot: Things You Love',  # T_070
    83: '{{0e0003002a0002000000}} What to Shoot: After the Rain',  # T_071
    87: '{{0e0003002a0002000000}} Take a Break',  # T_075
    95: '{{0e0003002a0002000000}} B&W × Merge',  # T_083
    96: '{{0e0003002a0002000000}} Brightness × Daydream',  # T_084
    97: '{{0e0003002a0002000000}} Contrast × Pinhole',  # T_085
    98: '{{0e0003002a0002000000}} 3D Autofocus',  # T_086
    99: '{{0e0003002a0002000000}} Write-Protected SD Cards',  # T_087
    100: '{{0e0003002a0002000000}} What to Shoot: People',  # T_088
    101: "{{0e0003002a0002000000}} Parakeet Tales: What's a Camera?",  # T_089
    102: '{{0e0003002a0002000000}} Parakeet Tales: Why a Room?',  # T_090
    103: '{{0e0003002a0002000000}} Parakeet Tales: A Smaller Room',  # T_091
    104: '{{0e0003002a0002000000}} Parakeet Tales: The Birth of Photos',  # T_092
    105: "{{0e0003002a0002000000}} Parakeet Tales: Grandpa's Portrait",  # T_093
    106: '{{0e0003002a0002000000}} Black and White Frames',  # T_094
    107: '{{0e0003002a0002000000}} JPG and MPO',  # T_095
    109: '{{0e0003002a0002000000}} Where Videos Are Saved',  # T_097
    110: '{{0e0003002a0002000000}} Watching Videos',  # T_098
    111: '{{0e0003002a0002000000}} AVI Files',  # T_099
    112: '{{0e0003002a0002000000}} Special Videos',  # T_100
    113: '{{0e0003002a0002000000}} Best Moments',  # T_101
    114: '{{0e0003002a0002000000}} Interval Shooting',  # T_102
    115: '{{0e0003002a0002000000}} Stop Motion',  # T_103
    116: '{{0e0003002a0002000000}} Play with Video',  # T_104
    117: '{{0e0003002a0002000000}} Save Frames',  # T_105
    118: '{{0e0003002a0002000000}} Switching Photo and Video',  # T_106
    119: '{{0e0003002a0002000000}} The Visible Area of Photos',  # T_107
    120: '{{0e0003002a0002000000}} Stop Motion × B&W',  # T_108
    121: '{{0e0003002a0002000000}} What to Shoot: Growing Plants',  # T_109
    122: '{{0e0003002a0002000000}} What to Shoot: Moving Clouds',  # T_110
    123: '{{0e0003002a0002000000}} What to Shoot: Crowds',  # T_111
    124: '{{0e0003002a0002000000}} What to Shoot: Transformations',  # T_112
    125: '{{0e0003002a0002000000}} What to Shoot: Teleporting',  # T_113
    126: '{{0e0003002a0002000000}} What to Shoot: Dancing Dolls',  # T_114
    127: '{{0e0003002a0002000000}} What to Shoot: Building Things',  # T_115
    128: '{{0e0003002a0002000000}} Tip: Automatic Stop Motion',  # T_116
    129: '{{0e0003002a0002000000}} Tip: Frame by Frame',  # T_117
    130: '{{0e0003002a0002000000}} 3D Tips: Videos',  # T_118
    131: '{{0e0003002a0002000000}} Tip: Afterimages',  # T_119
    132: '{{0e0003002a0002000000}} Photo Class: Blown Highlights',  # T_120
    133: '{{0e0003002a0002000000}} Slideshow Display Settings',  # T_121
    134: '{{0e0003002a0002000000}} "From the Northern Nest"',  # T_122
    135: '{{0e0003002a0002000000}} How About Special Videos?',  # T_123
    136: '{{0e0003002a0002000000}} Photos for DSi Software',  # T_124
    138: 'Are your toys and\nstuffed animals coming\nout well in 3D?',  # D_001_0
    139: "{{0e00040001001600140050005f004700750069006400310030005f005500}}3DS Camera can't take\ngood shots when you're\ntoo close to the subject.",  # D_001_1
    140: '{{0e00040001001600140050005f004700750069006400310030005f005500}}If you touch your\nfinger to the tip\nof your nose,',  # D_001_2
    141: "{{0e00040001001600140050005f004700750069006400310030005f005500}}your finger looks doubled\nor blurry, and you\ncan't see it well, right?",  # D_001_3
    142: '{{0e00040001001600140050005f004700750069006400300031005f005500}}{{0e00000003000400ff3200ff}}The key is to stay\n{{0e00000003000400454039ff}}at least 30 cm away.',  # D_001_4
    144: 'Ahem.\nExcuse me a moment.',  # D_002_0
    145: '3D autofocus usually\nadjusts the focus\nautomatically, but',  # D_002_1
    146: '{{0e00040001001600140050005f004700750069006400300033005f005500}}you can also adjust the\n{{0e00000003000400ff3200ff}}3D focus{{0e00000003000400454039ff}} yourself.',  # D_002_2
    147: '{{0e00040001001600140050005f004700750069006400300034005f005500}}{{0e00000003000400ff3200ff}}Move the {{0e00000003000400454039ff}}● left and right\nto line up the\ndoubled image.',  # D_002_3
    148: '{{0e00040001001600140050005f004700750069006400310032005f005500}}To go back to\n3D autofocus, press\nthe {{0e00000003000400ff3200ff}}\ue002 Button{{0e00000003000400454039ff}} or put\nthe arrows away.',  # D_002_4
    149: 'Sorry to interrupt.',  # D_002_5
    151: 'Welcome to\nNintendo 3DS Camera!',  # D_003_0
    152: 'With this software, you\ncan take 2D and even\n3D photos and videos.',  # D_003_1
    153: '{{0e00040001001600140050005f004700750069006400300035005f005500}}To take 3D photos\nor videos, turn up\nthe {{0e00000003000400ff3200ff}}3D depth slider{{0e00000003000400454039ff}}.',  # D_003_2
    154: "{{0e00040001001600140050005f004700750069006400300031005f005500}}Stay {{0e00000003000400ff3200ff}}at least\n30 cm{{0e00000003000400454039ff}} away from\nwhat you're shooting.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}",  # D_003_3
    155: "{{0e00040001001600140050005f004700750069006400300032005f005500}}If you'd like to know\nmore about 3DS Camera,\ntry touching me.",  # D_003_4
    157: 'Welcome to\nNintendo 3DS Camera!',  # D_003_0_flw
    158: 'With this software, you\ncan take 2D and even\n3D photos and videos.',  # D_003_1_flw
    159: 'This system can only\nshow 2D, but with\nan SD Card,',  # D_003_2_flw
    160: 'you can take your data to\na device that shows 3D,\nlike a Nintendo 3DS,\nand enjoy it in 3D.',  # D_003_3_flw
    161: "Let's start shooting.\n...But first, a word!",  # D_003_4_flw
    162: "{{0e00040001001600140050005f004700750069006400300031005f005500}}Stay {{0e00000003000400ff3200ff}}at least\n30 cm{{0e00000003000400454039ff}} away from\nwhat you're shooting.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}",  # D_003_5_flw
    163: "{{0e00040001001600140050005f004700750069006400300032005f005500}}Like this, if you'd like\nto know more about\n3DS Camera, try\ntouching me.",  # D_003_6_flw
    165: '{{0e00000003000400ff3200ff}}Press {{0e00000003000400ff3200ff}}\ue07a{{0e00000003000400454039ff}} to show the\n{{0e00000003000400454039ff}}level on the top screen.',  # D_004_0
    166: 'Press it again\nto hide it.',  # D_004_1
    167: 'You can also change\nwhat the {{0e00000003000400ff3200ff}}red{{0e00000003000400454039ff}} horizon\nline uses as level.',  # D_004_2
    168: 'Put the system on the\nslope you want to use,\nand with the level showing,\nhold {{0e00000003000400ff3200ff}}\ue079{{0e00000003000400454039ff}}.',  # D_004_3
    169: 'To go back, put it on\na level desk and\nhold {{0e00000003000400ff3200ff}}\ue079{{0e00000003000400454039ff}} again.',  # D_004_4
    171: '{{0e00040001001600140050005f004700750069006400310031005f005500}}The inner camera takes\n{{0e00000003000400ff3200ff}}2D{{0e00000003000400454039ff}} photos and videos.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}',  # D_005_0
    172: '{{0e00040001001600140050005f004700750069006400300036005f005500}}The outer camera takes\n{{0e00000003000400ff3200ff}}3D{{0e00000003000400454039ff}} and {{0e00000003000400ff3200ff}}2D{{0e00000003000400454039ff}} photos\nand videos.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}',  # D_005_1
    173: '{{0e00040001001600140050005f004700750069006400300036005f005500}}To take a {{0e00000003000400ff3200ff}}3D photo{{0e00000003000400454039ff}}\nof yourself, use the\nouter camera with\nthe self-timer!',  # D_005_2
    175: "If a friend looks at\nyour photos or videos\nand says they're hard\nto see in 3D,",  # D_006_0
    176: '{{0e00040001001600140050005f004700750069006400300037005f005500}}{{0e00000003000400ff3200ff}}have them move the\n{{0e00000003000400454039ff}}Circle Pad to adjust\nthe 3D focus.',  # D_006_1
    177: '{{0e00040001001600140050005f004700750069006400300037005f005500}}Line up the doubled\nimage... It should be\nmuch easier to see.',  # D_006_2
    179: 'When photos and\nvideos start to\npile up,',  # D_007_0
    180: '{{0e00040001001600140050005f004700750069006400310033005f005500}}touch a "date folder" to\ngroup everything taken\non that day.',  # D_007_1
    181: "{{0e00040001001600140050005f004700750069006400310034005f005500}}To see what's in a group,\ntouch it again to\nexpand it.",  # D_007_2
    182: "{{0e00040001001600140050005f004700750069006400310034005f005500}}By the way, I've grouped\nand hidden yesterday's\ndate photos.\nIt's a secret.",  # D_007_3
    189: 'In "Slideshow," you\ncan enjoy the photos\nand videos you\'ve taken.',  # D_009_0
    190: "When the system's on a\ndesk or you're watching\nfrom further away,\n2D is best.",  # D_009_1
    191: '{{0e00040001001600140050005f004700750069006400300035005f005500}}To switch to 2D,\nturn down the\n{{0e00000003000400ff3200ff}}3D depth slider{{0e00000003000400454039ff}}.\n(Remember?)',  # D_009_2
    193: 'In "Slideshow," you\ncan enjoy the photos\nand videos you\'ve taken.',  # D_009_0_flw
    194: 'Put the system on a desk\nand take your time\nlooking at photos,',  # D_009_1_flw
    195: 'and lovely memories\nwill come back to you.',  # D_009_2_flw
    197: "The how-to tips and hints\nI've shown you",  # D_010_0
    198: 'can be reread anytime\nfrom "How to Use"\nin "Settings."',  # D_010_1
    200: 'Oops!\nI forgot to mention...',  # D_011_0
    201: '{{0e00040001001600140050005f004700750069006400300038005f005500}}To return to the\nHOME Menu, press\n{{0e00000003000400ff3200ff}}\ue073 HOME{{0e00000003000400454039ff}}.',  # D_011_1
    203: 'Have you touched that\nintriguing {{0e00000003000400ff3200ff}}red lever{{0e00000003000400454039ff}}\nin the bottom right?',  # D_012_0
    204: 'Touch it and three\nfunction buttons\nappear.',  # D_012_1
    205: 'You can change the\n"Shooting Mode,"',  # D_012_2
    206: 'use the "Self-Timer"\nfor photos,',  # D_012_4
    207: 'and use "Special Videos"\nfor videos.',  # D_012_5
    208: 'Touch the lever again\nto put the function\nbuttons away.',  # D_012_3
    210: 'You thought you were\nshooting in 3D, but the\n3D depth slider was\nstill down...',  # D_013_0
    211: "{{0e00040001001600140050005f004700750069006400300035005f005500}}Don't worry! When you\nview photos and videos,\nyou can switch with the\n3D depth slider.",  # D_013_1
    212: '{{0e00040001001600140050005f004700750069006400300035005f005500}}Of course, photos and\nvideos taken with the\ninner camera stay 2D.\nUse the outer camera for 3D.',  # D_013_2
    214: 'Are your shots\ncoming out well?',  # D_014_0
    215: 'Photos in 3DS Camera\nmight show up in\nother games.',  # D_014_1
    216: "Let's take lots of\nfun photos together!",  # D_014_2
    218: 'The "Fluffy Pen"\nin "Doodle"',  # D_015_0
    219: 'lets you puff up or\nsink in any part\nof a photo.',  # D_015_1
    220: 'To flatten it back,\nuse the fluffy eraser.',  # D_015_2
    222: 'In "Color Settings,"\nyou can change the\nscreen\'s {{0e00000003000400ff3200ff}}theme color{{0e00000003000400454039ff}}.',  # D_016_0
    223: 'If choosing a color\nis a hassle, flick\nthe cursor and leave\nit to luck.',  # D_016_1
    224: 'Touch "Reset" to go\nback to the original\ncolor.',  # D_016_2
    226: 'Use "Woof" or "Meow" in\n"Self-Timer Sound,"',  # D_017_0
    227: 'and your pet might\nturn around at just\nthe right moment.',  # D_017_1
    228: 'Babies and sweethearts\nmight give you a\ngreat smile too!',  # D_017_2
    230: 'To shoot trees or\nbuildings straight,\npress {{0e00000003000400ff3200ff}}\ue07a{{0e00000003000400454039ff}} to show\nthe level.',  # D_018_0
    231: 'The {{0e00000003000400ff3200ff}}red line{{0e00000003000400454039ff}} that moves\nas you tilt the system...\nis roughly level with\nthe ground.',  # D_018_1
    232: "The lines that don't move\nmark the center\nof the screen.",  # D_018_2
    233: 'Use them to check\nyour balance.',  # D_018_3
    235: 'Want to be in the\nphoto with everyone?',  # D_019_0
    236: 'Then use the\n"Self-Timer."',  # D_019_1
    237: '3DS Camera will take\nthe photo for you\nautomatically.',  # D_019_2
    238: 'Touch "Voice," and you\ncan also take it by\nsaying "{{0e00000003000400ff3200ff}}OK!{{0e00000003000400454039ff}}"',  # D_019_3
    239: 'Say it clearly\nand cheerfully!',  # D_019_4
    241: '"Merge Camera" takes\nwonderfully weird\nface photos.',  # D_020_0
    242: '"I know someone like that!"\n"Perms suit you."\n"...Who is this?"',  # D_020_1
    243: 'Last night my cousins\nand I had a blast!',  # D_020_2
    245: '"Sparkle Camera" makes\ndecorating photos\neasy.',  # D_021_0
    246: 'Blow on it or show\nyour face on screen,\nand all kinds of\nsparkles appear.',  # D_021_1
    247: 'Wait for the moment...\nSnap!',  # D_021_2
    248: 'You can choose\n"Sparkle Camera" from\n"Shooting Mode."',  # D_021_3
    250: 'To make beautiful people\neven more beautiful,\ntry the\n"Daydream Camera."',  # D_022_0
    251: 'Your photos come out\nsoft and gentle.',  # D_022_1
    252: 'Food looks warm\nand delicious too.',  # D_022_2
    254: 'Get a nostalgic\nlook with the\n"Pinhole Camera."',  # D_023_0
    255: 'Before saying goodbye\nto that toy, why not\ntake a photo of it?',  # D_023_1
    260: 'With the "Mystery Camera,"\nyou never know what\nyou\'ll get.',  # D_025_0
    261: 'You get all sorts of\nphotos, so you might\ndiscover something new.',  # D_025_1
    262: 'Rumor has it things from\nanother dimension\nshow up...',  # D_025_2
    264: 'For night views or\ndim rooms, use the\n"Low-Light Camera."',  # D_026_0
    265: 'It takes a little\nlonger to shoot so it\ncan gather enough light,',  # D_026_1
    266: 'so tuck in your elbows\nand hold steady to\navoid camera shake.',  # D_026_2
    268: 'Why not set up your\nown original camera\nto your liking?',  # D_027_0
    269: 'In "Camera Settings,"\nyou can freely change\nfour settings.',  # D_027_1
    270: '"Restore" brings back the\noriginal settings, so\nfeel free to\nexperiment.',  # D_027_2
    272: 'Photos taken with\n3DS Camera',  # D_028_0
    273: 'can be saved in\n{{0e00000003000400ff3200ff}}System Memory{{0e00000003000400454039ff}}\nor on the {{0e00000003000400ff3200ff}}SD Card{{0e00000003000400454039ff}}.',  # D_028_1
    274: 'System Memory can hold\nup to {{0e00000003000400ff3200ff}}about 380{{0e00000003000400454039ff}}\nphotos.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}',  # D_028_2
    275: 'An SD Card can hold\nup to {{0e00000003000400ff3200ff}}about 3,000{{0e00000003000400454039ff}}\nphotos and videos\ncombined.',  # D_028_3
    276: 'Choose where to save\nthem in "Settings,"\nunder "Save Photos To."',  # D_028_4
    278: "Huh? I shot it with the\nouter camera, but it\ndoesn't look 3D...",  # D_029_0
    279: '{{0e00040001001600140050005f004700750069006400300035005f005500}}Then check the\n{{0e00000003000400ff3200ff}}3D depth slider{{0e00000003000400454039ff}}!\nIs it turned down?',  # D_029_1
    280: "{{0e00040001001600140050005f004700750069006400300035005f005500}}If it still doesn't\nshow in 3D when\nturned up,",  # D_029_2
    281: '{{0e00040001001600140050005f004700750069006400300035005f005500}}3D may be blocked by\nParental Controls.\n(Ask a grown-up.)',  # D_029_3
    283: '{{0e00040001001600140050005f004700750069006400300039005f005500}}When 3D can be shown,\nthe {{0e00000003000400ff3200ff}}3D mark{{0e00000003000400454039ff}} appears.',  # D_030_0
    284: "{{0e00040001001600140050005f004700750069006400300039005f005500}}It's {{0e00000003000400ff3200ff}}white{{0e00000003000400454039ff}} when showing 3D\nand {{0e00000003000400ff3200ff}}gray{{0e00000003000400454039ff}} when\nshowing 2D.",  # D_030_1
    286: "{{0e00040001001600140050005f004700750069006400300039005f005500}}When you can shoot in 3D,\nthe {{0e00000003000400ff3200ff}}3D mark{{0e00000003000400454039ff}} appears.\nWhat you shoot while\nit's showing",  # D_030_0_flw
    287: 'can be seen in 3D\nwhen played on a\ndevice that shows 3D.',  # D_030_1_flw
    289: '"Camera Settings"\n~ Film ~',  # D_031_0
    290: 'Change the "Film" in\n"Camera Settings" to change\nthe mood of photos\nand videos.',  # D_031_1
    291: 'Shoot in "B&W" and it\nlooks like a scene from\nan old movie!',  # D_031_2
    293: '"Camera Settings"\n~ Sharpness ~',  # D_032_0
    294: '"Sharpness" changes\nhow soft photos and\nvideos look.',  # D_032_1
    295: 'Slide left for a\nsofter image.',  # D_032_2
    296: 'Slide right for a\ncrisper image.',  # D_032_3
    297: 'For smooth-looking skin,\nslide it left.',  # D_032_4
    299: '"Camera Settings"\n~ Contrast ~',  # D_033_0
    300: '"Contrast" changes how\nvivid the colors are.',  # D_033_1
    301: 'Slide left for\ngentle colors.',  # D_033_2
    302: 'Slide right for\nvivid colors.',  # D_033_3
    303: 'For lively festivals,\nvivid colors are\nthe way to go.',  # D_033_4
    305: '"Camera Settings"\n~ Brightness ~',  # D_034_0
    306: '"Brightness" sets how\nbright photos and\nvideos are.',  # D_034_1
    307: 'Slide left to make\nthem darker,',  # D_034_2
    308: 'and slide right to\nmake them brighter.',  # D_034_3
    309: 'Master the camera settings\nand you might get exactly\nthe shot you want.',  # D_034_4
    311: 'Try to keep your subject\nfrom {{0e00000003000400ff3200ff}}going off the edge{{0e00000003000400454039ff}}\nof the screen, and it\nwill look better in 3D.',  # D_035_0
    313: 'Including {{0e00000003000400ff3200ff}}vertical{{0e00000003000400454039ff}} lines\nlike pillars or doors\nmakes 3D easier to see.',  # D_036_0
    315: '{{0e00000003000400ff3200ff}}Hazy{{0e00000003000400454039ff}} things like smoke\nor steam work in\n3D photos too.',  # D_037_0
    316: 'When lifting a pot lid,\nwatch out for\nthe hot steam!',  # D_037_1
    318: 'Small or {{0e00000003000400ff3200ff}}cluttered{{0e00000003000400454039ff}}\nthings are great\nfor 3D photos.',  # D_038_0
    319: 'Is your room tidy?',  # D_038_1
    320: "If it's messy...\nit's a great room\nfor 3D photos.",  # D_038_2
    321: 'But tidy it up anyway!',  # D_038_3
    323: '{{0e00000003000400ff3200ff}}See-through{{0e00000003000400454039ff}} things like\nfences or glass make\ninteresting 3D photos too.',  # D_039_0
    325: 'A hallway with depth,\na tree up front and a\nbuilding behind,\na fist thrust forward...',  # D_040_0
    326: '{{0e00000003000400ff3200ff}}Shoot with things {{0e00000003000400ff3200ff}}far{{0e00000003000400454039ff}} and\nthings {{0e00000003000400454039ff}}near in the\nframe for great 3D.',  # D_040_1
    328: "{{0e00000003000400ff3200ff}}Touch{{0e00000003000400454039ff}} a photo or video\nyou've taken to bring\nup a small menu.",  # D_041_0
    329: 'You can "Doodle" on\nphotos or\n"Play with Video."',  # D_041_1
    330: 'You can also delete\nphotos and videos\none at a time.',  # D_041_2
    332: 'Why not look at photos\nand videos with music\nthat fits the mood?',  # D_042_0
    333: 'In "Slideshow," you can\nchoose the music\nthat plays.',  # D_042_1
    334: 'You can also set how\nlong photos show and\nhow they change.',  # D_042_2
    336: 'Before removing the\nSD Card, {{0e00000003000400ff3200ff}}turn your\nNintendo 3DS off{{0e00000003000400454039ff}}.',  # D_043_0
    337: '{{0e00000003000400ff3200ff}}Open the {{0e00000003000400454039ff}}slot cover and\npush the SD Card in\nuntil it clicks...',  # D_043_1
    338: 'then pull out the\npart that pops out.',  # D_043_2
    339: 'When inserting it, check\nwhich side is up. The\nshiny gold contacts\nface {{0e00000003000400ff3200ff}}toward you{{0e00000003000400454039ff}}.',  # D_043_3
    341: "Actually...\nI'm a pretty capable\nparakeet.",  # D_044_0
    342: 'I read the room and talk\nabout what fits\nthe moment.',  # D_044_1
    343: "When you're shooting\nor when you're viewing,",  # D_044_2
    344: 'touch me at\neach moment.',  # D_044_3
    346: 'When taking photos, you\ncan shoot with the\n{{0e00000003000400ff3200ff}}\ue004\ue005\ue000 Buttons{{0e00000003000400454039ff}} while\nchoosing a camera in\n"Shooting Mode."',  # D_045_0
    348: 'Change how many photos\nand videos show on the\nTouch Screen with the\n{{0e00000003000400ff3200ff}}+{{0e00000003000400454039ff}} and {{0e00000003000400ff3200ff}}-{{0e00000003000400454039ff}} magnifying glasses.',  # D_046_0
    350: 'Actually, I work behind\nthe scenes in\n"Merge Camera," but',  # D_047_0
    351: "if I can't find\nthe faces, I can't\nmerge them.",  # D_047_1
    352: 'In dark places, or with\n"Negative" or "Mystery"\nchosen in\n"Camera Settings,"',  # D_047_2
    353: 'finding faces gets\nreally hard.',  # D_047_3
    354: "Sorry if it\ndoesn't work.",  # D_047_4
    356: '"Merge Camera" can\nactually merge with\nthings that aren\'t people.',  # D_048_0
    357: 'Merge with idol posters\nor mannequins!!',  # D_048_1
    359: 'In "Sparkle Camera,"\ntilting the system\nchanges how the\nsparkles move.',  # D_049_0
    364: 'Shooting and viewing\nphotos and videos...\nYou can switch with\nthe {{0e00000003000400ff3200ff}}\ue003 Button{{0e00000003000400454039ff}}.',  # D_051_0
    366: "Once you've taken photos\nor videos, take your\ntime looking at them.",  # D_052_0
    367: 'Looking back is important\nfor improving your skills.',  # D_052_1
    368: 'You might find\na new goal too.',  # D_052_2
    370: 'Do your photos or videos\never come out blurry?',  # D_053_0
    371: "When your hands move\nwhile shooting and photos\nor videos come out blurry,\nthat's {{0e00000003000400ff3200ff}}camera shake{{0e00000003000400454039ff}}.",  # D_053_1
    372: 'Dark places especially\ncause {{0e00000003000400ff3200ff}}camera shake{{0e00000003000400454039ff}}, so',  # D_053_2
    373: '{{0e00040001001600140050005f004700750069006400310035005f005500}}hold the camera steady\nor set it down\nto prevent it.',  # D_053_3
    375: 'Does the camera move\na little when you press\nthe shutter button?',  # D_054_0
    376: 'When taking photos\nin dark places where\nshake is likely, the\n"Self-Timer" can help.',  # D_054_1
    377: 'Once the "Self-Timer"\nis set, hold the\nsystem steady.',  # D_054_2
    378: "You don't have to press\nthe shutter button, so\nthere's less shake.",  # D_054_3
    380: 'Put your subject in the\ncenter of the screen\nfor a solid,\nsteady photo.',  # D_055_0
    381: 'Put your subject a little\noff center for\na cooler shot.',  # D_055_1
    382: "{{0e00000003000400ff3200ff}}Press {{0e00000003000400454039ff}}\ue07a to show the level\nand you'll see the\ncenter of the screen.",  # D_055_2
    383: 'Show off your sense of\nstyle with balance.\nStylish!',  # D_055_3
    385: "When shooting people,\nwhere they're looking\nis key.",  # D_056_0
    386: '{{0e00040001001600140050005f004700750069006400310038005f005500}}For example, put someone\nfacing right on the\nright side of the screen...\nIt looks cramped.',  # D_056_1
    387: '{{0e00040001001600140050005f004700750069006400310039005f005500}}Put them on the left,\nand the balance feels\nbetter and calmer.',  # D_056_2
    388: "{{0e00040001001600140050005f004700750069006400310039005f005500}}For someone facing left,\nit's the opposite.\nThis kind of balance\nin the frame...",  # D_056_3
    389: '{{0e00040001001600140050005f004700750069006400310039005f005500}}{{0e00000003000400ff3200ff}}is called\n{{0e00000003000400454039ff}}composition!',  # D_056_4
    391: 'Shooting kids or pets\nfrom a low eye level\nis fun too.',  # D_057_0
    393: 'In "Slideshow," you\ncan choose a theme.',  # D_058_0
    394: "I'll choose photos and\nvideos to fit the\ntheme you pick.",  # D_058_1
    395: "If what I pick doesn't\nfit the theme...\nI'm sorry.",  # D_058_2
    396: 'Hee hee.',  # D_058_3
    398: 'To make your subject\nstand out, pay attention\nto the background too.',  # D_059_0
    399: 'A simple background, like\na softly colored wall,\nmakes the star stand out.',  # D_059_1
    401: "Cool and cute.\nThere's a knack to\nshooting people.\nFor example...",  # D_060_0
    402: 'To make them look cool\nlike a model, shoot\nfrom below,\nlooking up.',  # D_060_1
    403: 'For a cute, wide-eyed\nlook, have them look\nup and shoot from above.',  # D_060_2
    404: 'The mood changes\ncompletely with the\nangle.',  # D_060_3
    406: 'Posed faces are nice,\nbut how about a shot\nlooking away sometimes?',  # D_061_0
    407: 'A natural expression\nmight make a\nlivelier photo.',  # D_061_1
    409: 'Even professional\nphotographers choose\ntheir best shot from\nlots of photos.',  # D_062_0
    410: 'To get good photos,\njust shoot\nlots of them!',  # D_062_1
    411: 'Delete the so-so ones!\nThe fun ones often\nhappen by chance.',  # D_062_2
    412: 'Not sure when to shoot?\nJust press the\nshutter button!',  # D_062_3
    414: 'Try combining\n"Camera Settings" and\n"Shooting Mode."',  # D_063_0
    415: 'For example, combine\n"Sepia" with\n"Sparkle Camera"...',  # D_063_1
    416: 'and the usual sparkles\nlook even more\nmagical.',  # D_063_2
    418: "When the camera is\nfacing the light,\nthat's called\n{{0e00000003000400ff3200ff}}backlight{{0e00000003000400454039ff}}.",  # D_064_0
    419: '{{0e00000003000400ff3200ff}}If you shoot with\n{{0e00000003000400454039ff}}backlight, your subject\ncomes out dark, but',  # D_064_1
    420: 'you can shoot with {{0e00000003000400ff3200ff}}backlight{{0e00000003000400454039ff}}\non purpose to make\na silhouette photo.',  # D_064_2
    422: 'Not sure what to shoot?\nWhy not take a\nleisurely walk?',  # D_065_0
    423: "Let's go find something\nyou want to shoot.",  # D_065_1
    425: 'How about shooting\nflowers and plants?',  # D_066_0
    426: "Shoot them every day\nand you'll have a\nrecord of their growth.",  # D_066_1
    428: "Why not shoot a\nneighbor's dog or\npigeons in the park?",  # D_067_0
    429: "Doodle what the dog's\nthinking... You could\nmake a little story.",  # D_067_1
    430: '"...Where did I\nbury that bone?"',  # D_067_2
    432: "Why not shoot\ntoday's meal?",  # D_068_0
    433: 'Shoot it every day,\nand it could be\na diet diary?',  # D_068_1
    435: 'Why not shoot\nthe sky?',  # D_069_0
    436: 'Even the same sky has\na different look\nevery day.',  # D_069_1
    437: 'A blue sky like the sea,\ndrifting fluffy clouds,\na passing plane...',  # D_069_2
    438: "(But don't shoot\nthe sun.)",  # D_069_3
    440: 'Why not shoot\nthe things you love?',  # D_070_0
    441: 'People, things, places\nyou love...\n\nShoot them with feeling.',  # D_070_1
    443: 'Right after rain is\na great time to shoot.',  # D_071_0
    444: 'You get different photos\nthan on a sunny day.',  # D_071_1
    445: 'How about shooting the\nscenery reflected\nin a puddle?',  # D_071_2
    459: 'Ahh, a moment to relax.\nWhy not take a break?',  # D_075_0
    484: 'Combine "B&W" in\n"Camera Settings"',  # D_083_0
    485: 'with "Merge Camera"\nin "Shooting Mode"...',  # D_083_1
    486: 'and you get a photo like\na great person from\na textbook!\n(But who is this?)',  # D_083_2
    488: '"Camera Settings" can\nalso strengthen the\neffect of a\n"Shooting Mode."',  # D_084_0
    489: 'Choose "Daydream Camera"\nand slide "Brightness"\nto the right...',  # D_084_1
    490: 'and you get a glowing,\nvery happy-looking\nphoto.',  # D_084_2
    492: 'My favorite combination\nof "Camera Settings"\nand "Pinhole Camera"',  # D_085_0
    493: 'is "Contrast."\nSlide it all the\nway right',  # D_085_1
    494: 'for a toy-camera\nlook!',  # D_085_2
    496: '3D autofocus is actually\nme working behind\nthe scenes, but',  # D_086_0
    497: "in dark places I can't\ntell where to focus...",  # D_086_1
    498: "If the top-screen image\nsways left and right and\nwon't look 3D,",  # D_086_2
    499: 'try adjusting the\n3D focus yourself.',  # D_086_3
    500: 'Touch the red lever,\nand the adjustment\nbuttons appear.',  # D_086_4
    501: 'You can do it!',  # D_086_5
    503: 'Hm?',  # D_087_0
    504: '{{0e00040001001600140050005f004700750069006400320030005f005500}}The SD Card is\nwrite-protected.',  # D_087_1
    505: "{{0e00040001001600140050005f004700750069006400320030005f005500}}3DS Camera can't use\na write-protected\nSD Card, so",  # D_087_2
    506: '{{0e00040001001600140050005f004700750069006400320031005f005500}}turn the power off and\nslide the {{0e00000003000400ff3200ff}}lock switch{{0e00000003000400454039ff}}\nup as shown above.',  # D_087_3
    507: '{{0e00040001001600140050005f004700750069006400320031005f005500}}Thank you very much.\n(bows)',  # D_087_4
    509: 'Why not take photos\nof family or friends?',  # D_088_0
    510: 'Will they be surprised\nwhen you show them?',  # D_088_1
    512: 'By the way,',  # D_089_0
    513: '{{0e00000003000400ff3200ff}}{{0e00000003000400ff3200ff}}camera{{0e00000003000400454039ff}} means {{0e00000003000400454039ff}}room\nin Italian.\nAhem!',  # D_089_1
    514: 'Huh?\nWhy, you ask...?',  # D_089_2
    515: '...',  # D_089_3
    516: "I'll look it up\nby next time!",  # D_089_4
    518: 'I looked it up!\nWhy {{0e00000003000400ff3200ff}}camera{{0e00000003000400454039ff}} means {{0e00000003000400ff3200ff}}room{{0e00000003000400454039ff}}...',  # D_090_0
    519: 'On a sunny day, go into\na {{0e00000003000400ff3200ff}}pitch-dark room{{0e00000003000400454039ff}}\nand make a tiny hole\nin the wall,',  # D_090_1
    520: 'and get this!\nThe view outside shows\nup on the opposite wall!',  # D_090_2
    521: '{{0e00000003000400ff3200ff}}A {{0e00000003000400ff3200ff}}camera{{0e00000003000400454039ff}} is this\npitch-dark {{0e00000003000400454039ff}}room!',  # D_090_3
    522: "Huh?\nIt's too big\nto carry...?",  # D_090_4
    523: '...',  # D_090_5
    524: "I'll look it up\nby next time!",  # D_090_6
    526: 'I looked it up!',  # D_091_0
    527: 'Great people long ago\nmade cameras about\nthe size of a bag.',  # D_091_1
    528: '{{0e00000003000400ff3200ff}}They say {{0e00000003000400ff3200ff}}lenses{{0e00000003000400454039ff}} and {{0e00000003000400454039ff}}mirrors\nare important!',  # D_091_2
    529: "Huh?\nIt's too small\nto get inside...?",  # D_091_3
    530: '...',  # D_091_4
    531: "I'll look it up\nby next time!",  # D_091_5
    533: 'Inside a dark box with\na lens, the scenery\naround it is projected...',  # D_092_0
    534: 'and the way to take\nthat out is a\n{{0e00000003000400ff3200ff}}photo{{0e00000003000400454039ff}}!',  # D_092_1
    535: "That's the power\nof science!",  # D_092_2
    536: 'No more questions!',  # D_092_3
    537: "(Science... what's that?)",  # D_092_4
    539: 'Long, long ago, when my\nancestor was taking\na nap,',  # D_093_0
    540: 'a human with a box with\na lens appeared and drew\na picture that looked\njust like him.',  # D_093_1
    541: 'They say there were\nno photos back then.',  # D_093_2
    542: 'What a strange story.',  # D_093_3
    544: 'Photos with black frames\nare saved in\n{{0e00000003000400ff3200ff}}System Memory{{0e00000003000400454039ff}},',  # D_094_0
    545: 'and photos with white\nframes are saved on\nthe {{0e00000003000400ff3200ff}}SD Card{{0e00000003000400454039ff}}.',  # D_094_1
    546: 'You can start calling me\nProfessor Know-It-All\nanytime now.',  # D_094_2
    548: 'Photos saved on\nthe SD Card',  # D_095_0
    549: 'are in a folder\ncalled {{0e00000003000400ff3200ff}}DCIM{{0e00000003000400454039ff}}\non the SD Card.',  # D_095_1
    550: 'Files named\nHNI_XXXX{{0e00000003000400ff3200ff}}.JPG{{0e00000003000400454039ff}}\nare {{0e00000003000400ff3200ff}}2D photo{{0e00000003000400454039ff}} data,',  # D_095_2
    551: 'and files named\nHNI_XXXX{{0e00000003000400ff3200ff}}.MPO{{0e00000003000400454039ff}}\nare {{0e00000003000400ff3200ff}}3D photo{{0e00000003000400454039ff}} data.',  # D_095_3
    552: 'The other day a friend\naccidentally deleted\nsome MPO files,',  # D_095_4
    553: "and was sad that the\nphotos didn't look\n3D anymore.",  # D_095_5
    554: "I'll just have to be\na model and cheer\nthem up!",  # D_095_6
    561: 'Videos taken with\n3DS Camera are saved\non the {{0e00000003000400ff3200ff}}SD Card{{0e00000003000400454039ff}}.',  # D_097_0
    562: '"Save Photos To" in\n"Settings" can\'t change\nthis, so keep it in mind.',  # D_097_1
    564: "{{0e00040001001600140050005f004700750069006400320034005f005500}}Videos have a frame\nthat's a little different\nfrom photos.",  # D_098_0
    565: '{{0e00040001001600140050005f004700750069006400320034005f005500}}Touch one, and it plays\non the top screen,',  # D_098_1
    566: '{{0e00040001001600140050005f004700750069006400320034005f005500}}so you can quickly\nremember what the\nvideo was.',  # D_098_2
    568: 'Videos saved on\nthe SD Card',  # D_099_0
    569: 'are in a folder\ncalled {{0e00000003000400ff3200ff}}DCIM{{0e00000003000400454039ff}}\non the SD Card.',  # D_099_1
    570: 'Files named\nHNI_XXXX{{0e00000003000400ff3200ff}}.{{0e00000003000400454039ff}}{{0e00000003000400ff3200ff}}AVI{{0e00000003000400454039ff}}\nare {{0e00000003000400ff3200ff}}video{{0e00000003000400454039ff}} data.',  # D_099_2
    571: "Please don't play 3D\nvideos on devices that\ndon't support 3D playback.",  # D_099_3
    573: 'With "Special Videos,"\nyou can shoot\nsomewhat unusual videos.',  # D_100_0
    574: '"Interval Shooting,"\n"Stop Motion" and\n"Best Moments"',  # D_100_1
    575: 'each let you easily\nmake a different\nkind of video.',  # D_100_2
    576: 'Oh, and "Special Videos"\ndon\'t record sound.',  # D_100_3
    578: '"Best Moments" lets\nyou use pause',  # D_101_0
    579: 'to make a video of\njust the scenes\nyou want.',  # D_101_1
    580: 'Try making a lovely\nvideo of just the\nbest moments.',  # D_101_2
    582: '"Interval Shooting" takes\na photo at set intervals\nand strings them\ninto a video.',  # D_102_0
    583: 'You get a video like\ntime on fast-forward,',  # D_102_1
    584: 'so try shooting things\nthat usually move slowly.\nYou might discover\nsomething new.',  # D_102_2
    586: 'With "Stop Motion," you\ncan shoot simple\nanimations.',  # D_103_0
    587: 'For example, use\na pen lying nearby...',  # D_103_1
    588: 'move it a little at a\ntime and "Shoot."',  # D_103_2
    589: 'The finished video is\na little jerky with a\nunique feel, but\nI love it.',  # D_103_3
    591: 'In "Play with Video," you\ncan do more than watch.\nYou can play it backward,',  # D_104_0
    592: 'and change the speed\nand pitch.',  # D_104_1
    593: 'Left and right\nchanges the speed,',  # D_104_2
    594: 'and up and down\nchanges the pitch.',  # D_104_3
    595: 'You can change\neach one separately.',  # D_104_4
    597: '"Save Frames" in\n"Play with Video" lets\nyou cut out a single\nframe of a video.',  # D_105_0
    598: 'When paused, the\ntop-screen image is\nsaved as a photo.',  # D_105_1
    599: "With this, you won't\nmiss the decisive\nmoment.",  # D_105_2
    601: 'You may already\nknow this, but\n3DS Camera takes\nphotos and videos.',  # D_106_0
    602: '{{0e00040001001600140050005f004700750069006400320032005f005500}}To shoot a video,\ntouch the {{0e00000003000400ff3200ff}}\ue076{{0e00000003000400454039ff}} button\non the screen.',  # D_106_1
    603: '{{0e00040001001600140050005f004700750069006400320033005f005500}}When you want to take\nphotos, touch the\n{{0e00000003000400ff3200ff}}\ue01e{{0e00000003000400454039ff}} button on the\nscreen to switch.',  # D_106_2
    605: 'Actually, photos taken\nwith 3DS Camera save a\nwider area than you see\non the screen.',  # D_107_0
    606: 'To see all of it, move\nthe {{0e00000003000400ff3200ff}}Circle Pad{{0e00000003000400454039ff}} down.',  # D_107_1
    607: 'To go back, move\nthe {{0e00000003000400ff3200ff}}Circle Pad{{0e00000003000400454039ff}} up.',  # D_107_2
    609: 'You can combine\n"Special Videos" with\n"Camera Settings" too.',  # D_108_0
    610: 'For example, combine\n"Stop Motion" with\n"B&W"...',  # D_108_1
    611: 'and it looks just\nlike a silent movie.',  # D_108_2
    612: "Actually, I'm\ngood at mime too!",  # D_108_3
    614: 'Why not watch sprouts\ncome up or flowers\nbloom?',  # D_109_0
    615: 'In "Interval Shooting,"\nset the interval to\n{{0e00000003000400ff3200ff}}60 seconds{{0e00000003000400454039ff}},',  # D_109_1
    616: 'and you can watch slow\ngrowth like plants\non fast-forward.',  # D_109_2
    617: 'You can record for up\nto {{0e00000003000400ff3200ff}}about 8 days{{0e00000003000400454039ff}}.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}',  # D_109_3
    619: 'Why not shoot slowly\ndrifting clouds with\n"Interval Shooting"?',  # D_110_0
    620: 'Set the interval to\n{{0e00000003000400ff3200ff}}5 seconds{{0e00000003000400454039ff}} to see\nthe clouds drift by.',  # D_110_1
    621: 'A longer interval makes\nthem move faster, which\nis even more dramatic!',  # D_110_2
    623: 'I looked down on a\nbusy intersection',  # D_111_0
    624: 'and shot it with\n"Interval Shooting"\nat {{0e00000003000400ff3200ff}}2 seconds{{0e00000003000400454039ff}}.',  # D_111_1
    625: 'Watching the people\nand cars rushing\naround,',  # D_111_2
    626: 'I somehow felt like\na giant.',  # D_111_3
    628: 'Have you tried\n"Best Moments"?',  # D_112_0
    629: 'My cousin and I made\na transformation\nvideo together.',  # D_112_1
    630: "Just swap places while\nit's paused. Easy!",  # D_112_2
    631: 'Trans-form!',  # D_112_3
    633: "I'll secretly teach you\nhow to teleport.",  # D_113_0
    634: 'First, put down a cup\nand start shooting with\n"Best Moments."',  # D_113_1
    635: 'Shoot a little, pause,\nmove the cup, and\nresume shooting...',  # D_113_2
    636: 'Ta-da!',  # D_113_3
    637: '...It was a magic trick,\nand yes, there was\na trick to it.',  # D_113_4
    639: "Let's make your favorite\ndoll dance.",  # D_114_0
    640: 'With "Stop Motion," just\nchange its pose a little\neach shot, and you\'re done.',  # D_114_1
    641: "It's exciting to imagine\nhow it'll move when\nit's finished.",  # D_114_2
    643: "Building models is\nfun, isn't it?",  # D_115_0
    644: 'Why not record it all\nwith "Interval Shooting"\nor "Stop Motion"?',  # D_115_1
    645: "The excitement of\nbuilding it comes back,\nand it's even more moving.",  # D_115_2
    647: 'Do you think "Stop Motion"\nis fun but a hassle?',  # D_116_0
    648: 'Using "Interval Shooting"\nmakes it a little easier.',  # D_116_1
    649: 'Your hands are free,\nso shooting might\ngo faster.',  # D_116_2
    650: 'Once you get used to it,\nset the interval to\n2 seconds for speed shooting!',  # D_116_3
    652: 'In "Play with Video,"\nhave you ever been\ncurious about something\nyou only glimpsed?',  # D_117_0
    653: 'Pause, then use the\n{{0e00000003000400ff3200ff}}\ue004 Button{{0e00000003000400454039ff}} to go back\none frame at a time.{{0e00000003000400ff3200ff}}{{0e00000003000400ff3200ff}}',  # D_117_1
    654: "The {{0e00000003000400ff3200ff}}\ue005 Button{{0e00000003000400454039ff}} goes forward\none frame, so it's fine\nif you go back too far.{{0e00000003000400ff3200ff}}{{0e00000003000400ff3200ff}}",  # D_117_2
    656: 'Videos with a lot of\nmovement may not look\n3D or can make you\nfeel sick.',  # D_118_0
    657: 'Move slowly when\nshooting videos.',  # D_118_1
    659: 'When shooting\n"Special Videos," do you\nsee something like\nan afterimage?',  # D_119_0
    660: 'In "Interval Shooting"\nand "Stop Motion,"\nthe previous frame',  # D_119_1
    661: 'and in "Best Moments,"\nthe image from when\nyou paused show\nfaintly.',  # D_119_2
    662: 'Use it as a guide for\nyour next shot.',  # D_119_3
    664: 'Have you ever shot\nthe sky and the clouds\ncame out flat white?',  # D_120_0
    665: "When lit areas are so\nbright they turn white,\nthat's called\n{{0e00000003000400ff3200ff}}blown highlights{{0e00000003000400454039ff}}.",  # D_120_1
    666: 'When shooting somewhere\nbright, slide "Brightness"\nin "Camera Settings"\nto the left,',  # D_120_2
    667: 'and even the shadows\nwill show clearly.',  # D_120_3
    669: 'To see only photos in\na row in the slideshow,',  # D_121_0
    670: 'choose the combination\nyou want in "Display\nSettings" under\n"Choose Theme."',  # D_121_1
    672: 'Thank you for reading\nall my explanations.\n(bows)',  # D_122_0
    673: 'A song to say\nthanks...',  # D_122_1
    674: '"From the Northern Nest"',  # D_122_2
    675: "...Sorry.\nI'll save the song\nfor next time.",  # D_122_3
    676: 'From now on, keep taking\nlots of photos and\nvideos and having fun.',  # D_122_4
    678: 'Are you using\n"Special Videos"?',  # D_123_0
    679: 'They let you shoot\nvideos unlike usual,\nso I recommend them.',  # D_123_1
    680: 'If you can\'t find\n"Special Videos," touch\nthe {{0e00000003000400ff3200ff}}red lever{{0e00000003000400454039ff}}.',  # D_123_2
    682: 'Some DSi-compatible\nsoftware uses photos\nsaved in the system.',  # D_124_0
    683: "But some photos, like\ndoodled ones, can't\nbe used.",  # D_124_1
}
