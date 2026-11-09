# SPDX-License-Identifier: GPL-3.0-or-later
"""Nintendo 3DS Sound (0004001000020500): msg/JP_Japanese.LZ.

One table per message file, keyed by string number. {{hex}} tokens are
formatting and placeholder codes copied from the original and must stay
as they are."""

MAIN = {  # S.msbt
    1: 'Nintendo 3DS Sound',  # C_T_00
    3: 'Settings',  # C_T_02
    4: 'Favorites',  # C_T_03
    6: 'System Memory',  # C_T_05
    7: 'SD Card',  # C_T_06
    8: 'StreetPass',  # C_T_07
    11: 'How to Use',  # C_T_10
    12: 'Data Management',  # C_T_11
    13: 'Recent StreetPass Log',  # C_T_12
    14: 'Top 10 Matches',  # C_T_13
    15: 'StreetPass Hit Songs',  # C_T_14
    16: 'StreetPass Top Artists',  # C_T_15
    23: 'Close',  # C_B_01
    24: 'Back',  # C_B_02
    25: 'Settings',  # C_B_03
    26: '{{0e000100000002005000}}StreetPass{{0e000100000002006400}}',  # C_B_04
    28: 'Open',  # P_B_00
    29: 'Start',  # P_B_02
    30: '{{0e000100000002005000}}Favorites{{0e000100000002006400}}',  # P_B_03
    31: 'Remove',  # P_B_05
    34: '{{0e000100000002005000}}Remove All{{0e000100000002006400}}',  # P_B_09
    36: 'Record & Play with the Mic',  # P_BR_00
    38: '/SD Card',  # P_BR_02
    39: 'Shuffle Picks',  # P_BR_03
    40: 'Resume',  # P_BR_04
    41: '/Extra Data',  # P_BR_05
    44: 'Shuffle Everything',  # E_00
    45: 'Top 10 Played',  # E_01
    47: "Today's Pick",  # E_03
    48: '{{0e0003002e0002000000}} Special',  # E_04
    49: '{{0e0003002e0002000000}} Special',  # E_05
    50: 'Shuffle all songs',  # E_I_00
    51: 'Your 10 most\nplayed songs',  # E_I_01
    53: "The parakeet's\npick of the day",  # E_I_03
    55: 'A collection for songs\nthat caught your ear',  # E_I_05
    56: "The parakeet's\nwhimsical collection",  # E_I_06
    57: '1st',  # E_I_TOP10_01
    58: '2nd',  # E_I_TOP10_02
    59: '3rd',  # E_I_TOP10_03
    60: '4th',  # E_I_TOP10_04
    61: '5th',  # E_I_TOP10_05
    62: '6th',  # E_I_TOP10_06
    63: '7th',  # E_I_TOP10_07
    64: '8th',  # E_I_TOP10_08
    65: '9th',  # E_I_TOP10_09
    66: '10th',  # E_I_TOP10_10
    68: 'Top 10',  # F_00
    69: 'Practice',  # F_01
    70: 'StreetPass',  # F_02
    71: 'Secret',  # F_03
    73: 'Favorites {{0e00030000000000}}/{{0e00030007000000}}/{{0e00030008000000}}{{0e0003002e0002000000}}{{0e0003002e0002000100}}',  # F_N_00
    78: 'There are no images\nto show right now.',  # V_SS_NoPhoto
    80: 'Play',  # R_B_00
    81: 'Record',  # R_B_01
    82: 'Delete',  # R_B_02
    83: 'Overwrite',  # R_B_05
    84: 'Copy',  # R_B_06
    85: 'Move',  # R_B_07
    88: 'Audio Output',  # S_00
    89: 'Mono',  # S_B_00_0
    90: 'Stereo',  # S_B_00_1
    91: 'Surround',  # S_B_00_2
    92: 'Touch Sounds',  # S_01
    93: 'On',  # S_B_01_0
    94: 'Off',  # S_B_01_1
    95: 'Color Settings',  # S_B_03
    96: 'Data Management',  # S_B_04
    97: 'How to Use',  # S_B_05
    98: 'You can read the how-to\ntips shown so far.',  # S_I_05
    103: '{{0e000100000002006300}}Reset Save Data{{0e000100000002006400}}',  # D_B_00
    104: 'Delete Sounds on This Page',  # D_B_01
    105: 'Delete All Sounds',  # D_B_02
    107: 'StreetPass\nMatchmaker',  # CEC_TOP_B_00
    108: 'StreetPass\nHit Chart',  # CEC_TOP_B_01
    109: 'StreetPass',  # CEC_TOP_B_02
    110: 'On',  # CEC_TOP_B_03_0
    111: 'Off',  # CEC_TOP_B_03_1
    112: '{{0e00030026000000}} Selection',  # CEC_TOP_00
    113: 'Put songs in your\n"StreetPass" favorites.',  # CEC_TOP_10
    114: 'Without song info,\nStreetPass can\'t be used.\n\nPut songs in your\n"StreetPass" favorites.',  # CEC_TOP_15
    116: "Everyone's Sound Selection\n",  # CEC_MsgDesc
    118: 'Top 10 Matches',  # CEC_CNT_B_00
    119: 'Recent StreetPass Log',  # CEC_CNT_B_01
    120: 'StreetPass Hit Songs',  # CEC_CNT_B_02
    121: 'StreetPass Top Artists',  # CEC_CNT_B_03
    122: 'Scroll with \ue07d or \ue077',  # CEC_CNT_B_04
    123: 'Save as Photo',  # CEC_CNT_B_05
    124: '{{0e000100000002005000}}Reset{{0e000100000002006400}}',  # CEC_CNT_B_06
    125: 'No StreetPass\nrecords yet.',  # CEC_CNT_10
    126: "You haven't passed anyone\nwith similar taste yet.",  # CEC_CNT_15
    127: 'No hit chart\ninfo yet.',  # CEC_CNT_20
    128: '{{0e000300270002000000}} songs nominated!\nKeep on StreetPassing.',  # CEC_CNT_21
    129: '1 song nominated!\nKeep on StreetPassing.',  # CEC_CNT_23
    130: '{{0e000300270002000000}} artists nominated!\nKeep on StreetPassing.',  # CEC_CNT_22
    131: '1 artist nominated!\nKeep on StreetPassing.',  # CEC_CNT_24
    134: 'Music you both like',  # CEC_CNT_32
    135: '{{0e000300280002000000}}s',  # CEC_CNT_33
    136: '{{0e0005000000040000004041}}{{0e00030000000000}}{{0e000200000002000100}}/{{0e000200000002000100}}{{0e00030007000000}}{{0e000200000002000100}}/{{0e000200000002000100}}{{0e00030008000000}} around {{0e00030009000000}}{{0e00050001000000}}:00',  # CEC_CNT_34
    140: '{{0e0003002e0002000000}}\u3000and more',  # CEC_CNT_38
    141: 'No songs to show',  # CEC_CNT_39
    142: 'Period {{0e0005000000040000004041}}{{0e00030000000000}}{{0e000200000002000100}}/{{0e000200000002000100}}{{0e00030007000000}}{{0e000200000002000100}}/{{0e000200000002000100}}{{0e00030008000000}}{{0e00050001000000}} - {{0e0005000000040000004041}}{{0e00030013000000}}{{0e000200000002000100}}/{{0e000200000002000100}}{{0e0003001a000000}}{{0e000200000002000100}}/{{0e000200000002000100}}{{0e0003001b000000}}',  # CEC_CNT_40
    146: 'Compiled by {{0e00030026000000}}',  # CEC_CNT_43
    147: 'Participants: {{0e0003002b0002000000}}',  # CEC_CNT_44
    148: '{{0e0003002c0002000000}}\npoints',  # CEC_CNT_45
    152: 'You can change the title.',  # SWKB_U
    153: 'Cancel',  # SWKB_Btn00
    154: 'OK',  # SWKB_Btn01
    156: 'OK',  # ErrBrkn_Btn00
    157: 'The save data is\ncorrupted.\n\nNew save data will\nbe created.',  # ErrBrkn00
    158: 'Creating new\nsave data...',  # ErrBrkn01
    160: 'Times music played so far:\n{{0e000300270002000000}}',  # FriendCard_Play
    161: 'Times music played so far:\n{{0e000300270002000000}}',  # FriendCard_Play0
    162: 'Times music played so far:\n{{0e000300270002000000}}',  # FriendCard_Play1
    164: "Mii Maker's save data\nwas corrupted, so it\nhas been reset.",  # CFL_Recover_000
    165: 'OK',  # CFL_B_Recover_000
}

DIALOGS = {  # S_dlg.msbt
    2: "The SD Card can't\nbe recognized.",  # SD_Invalid_00
    3: 'OK',  # SD_Invalid_B00
    4: "The SD Card is\nwrite-protected.\n\nTurn the power off and\nslide the SD Card's\nlock switch to unlock it.",  # SD_Protected
    5: 'OK',  # SD_Protected_B00
    6: 'The SD Card was removed.\n\nPlease turn the system\noff before removing\nthe SD Card.',  # SD_Remove
    7: 'OK',  # SD_Remove_B00
    8: "There isn't enough free\nspace on the SD Card,\nso favorites can't be saved.",  # SD_Full_P_00
    9: 'OK',  # SD_Full_P_B00
    10: "There isn't enough free\nspace on the SD Card,\nso sounds can't be recorded.",  # SD_Full_R_00
    11: 'OK',  # SD_Full_R_B00
    12: "There isn't enough free\nspace on the SD Card,\nso the sound can't be overwritten.",  # SD_Full_R_01
    13: 'OK',  # SD_Full_R_B01
    14: "There isn't enough free\nspace on the SD Card,\nso sounds can't be moved.",  # SD_Full_R_02
    15: 'OK',  # SD_Full_R_B02
    16: "There isn't enough free\nspace on the SD Card,\nso sounds can't be copied.",  # SD_Full_R_03
    17: 'OK',  # SD_Full_R_B03
    18: "There isn't enough free\nspace on the SD Card,\nso the photo can't be saved.",  # SD_Full_CEC_00
    19: 'OK',  # SD_Full_CEC_B00
    21: "Couldn't play it.",  # C_ErrPlay
    22: 'OK',  # C_B_ErrPlay
    23: 'Checking the SD Card...',  # P_Bro_000
    25: '{{0e000100000002005a00}}Radio{{0e000100000002006400}}',  # P_B_Fx_00_0
    26: '{{0e000100000002005a00}}Radio{{0e000100000002006400}}',  # P_B_Fx_00_1
    27: '{{0e000100000002005a00}}Karaoke{{0e000100000002006400}}',  # P_B_Fx_10_0
    28: '{{0e000100000002005a00}}Karaoke{{0e000100000002006400}}',  # P_B_Fx_10_1
    29: '{{0e000100000002005a00}}Echo{{0e000100000002006400}}',  # P_B_Fx_20_0
    30: '{{0e000100000002005a00}}Echo{{0e000100000002006400}}',  # P_B_Fx_20_1
    31: '{{0e000100000002005a00}}8-bit{{0e000100000002006400}}',  # P_B_Fx_30_0
    32: '{{0e000100000002005a00}}8-bit{{0e000100000002006400}}',  # P_B_Fx_30_1
    34: '{{0e000100000002005a00}}Add to which favorites?{{0e000100000002006400}}',  # P_Add_000
    35: 'Cancel',  # P_B_Add_000
    36: 'Add',  # P_B_Add_001
    37: 'New',  # P_B_Add_002
    38: 'Added to\n"{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}".',  # P_Add_010
    39: 'OK',  # P_B_Add_010
    40: "Couldn't update\nfavorites.",  # P_Add_020
    41: 'OK',  # P_B_Add_020
    42: 'All songs in\n"{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}"\nwill be added.\n\nIs that OK?',  # P_Add_030
    43: 'Yes',  # P_B_Add_030
    44: 'No',  # P_B_Add_031
    45: 'Not every song can\nbe added. Continue?',  # P_Add_040
    46: 'Yes',  # P_B_Add_040
    47: 'No',  # P_B_Add_041
    48: 'Adding to\nfavorites...',  # P_Add_050
    49: 'The same song is\nalready there.\n\nThe same song can\'t be\nadded to "StreetPass" twice.',  # P_Add_080
    50: 'OK',  # P_B_Add_080
    51: 'There are no songs\nthat can be added\nto favorites.',  # P_Add_090
    52: 'OK',  # P_B_Add_090
    53: 'Use this title\nand icon?',  # P_New_000
    54: 'Change Title',  # P_B_New_000
    55: 'Change Icon',  # P_B_New_001
    56: 'Cancel',  # P_B_New_002
    57: 'OK',  # P_B_New_003
    58: 'Which icon?',  # P_New_010
    60: 'Cancel',  # P_B_New_011
    61: 'OK',  # P_B_New_012
    62: 'Favorites with the same\ntitle already exist.\n\nSave anyway?',  # P_New_050
    63: 'Yes',  # P_B_New_050
    64: 'No',  # P_B_New_051
    66: 'All songs will be removed\nfrom "{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}".\n\nIs that OK?',  # P_Rmv_000
    67: 'Yes',  # P_B_Rmv_000
    68: 'No',  # P_B_Rmv_001
    72: "Couldn't update\nfavorites.",  # P_Rmv_020
    73: 'OK',  # P_B_Rmv_020
    74: 'All songs were\nremoved from\n"{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}".',  # P_Rmv_030
    75: 'OK',  # P_B_Rmv_030
    76: 'Removing from\nfavorites...',  # P_Rmv_050
    77: 'The selected songs will\nbe removed from\n"{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}".\n\nIs that OK?',  # P_Rmv_100
    78: 'Yes',  # P_B_Rmv_100
    79: 'No',  # P_B_Rmv_101
    82: 'StreetPass can\'t be used\nwhile "StreetPass"\nhas no songs.',  # P_Rmv_120
    83: 'OK',  # P_B_Rmv_120
    84: 'All songs will be\nremoved and\n"{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}"\nwill be deleted.\n\nIs that OK?',  # P_Del_000
    85: 'Yes',  # P_B_Del_000
    86: 'No',  # P_B_Del_001
    89: '"{{0e000100000002005c00}}{{0e0003002e0002000000}}{{0e000100000002006400}}"\nwas deleted.',  # P_Del_020
    90: 'OK',  # P_B_Del_020
    91: "Some music data\ncan't be found\non the SD Card.\n\nRemove it from\nfavorites?",  # P_DeadLink_000
    92: 'Yes',  # P_B_DeadLink_000
    93: 'No',  # P_B_DeadLink_001
    94: "Some music data\ncan't be found\non the SD Card.\n\nRemove it from\nfavorites?",  # P_DeadLink_010
    95: 'Yes',  # P_B_DeadLink_010
    96: 'No',  # P_B_DeadLink_011
    109: 'A problem was found\nwith sounds in\nSystem Memory.\n\nRepairing them...',  # R_Recover_00
    110: 'The sounds were\nrepaired.',  # R_Recover_10
    111: 'OK',  # R_B_Recover_10
    112: "Couldn't repair\nthe sounds.",  # R_Recover_90
    113: 'OK',  # R_B_Recover_90
    115: '{{0e000100000002005a00}}Parakeet{{0e000100000002006400}}',  # R_B_Fx_00_0
    116: '{{0e000100000002005a00}}Parakeet{{0e000100000002006400}}',  # R_B_Fx_00_1
    117: '{{0e000100000002005a00}}Robot{{0e000100000002006400}}',  # R_B_Fx_01_0
    118: '{{0e000100000002005a00}}Robot{{0e000100000002006400}}',  # R_B_Fx_01_1
    119: '{{0e000100000002005a00}}Helium{{0e000100000002006400}}',  # R_B_Fx_02_0
    120: '{{0e000100000002005a00}}Helium{{0e000100000002006400}}',  # R_B_Fx_02_1
    121: '{{0e000100000002005a00}}Fan{{0e000100000002006400}}',  # R_B_Fx_10_0
    122: '{{0e000100000002005a00}}Fan{{0e000100000002006400}}',  # R_B_Fx_10_1
    123: '{{0e000100000002005a00}}Tunnel{{0e000100000002006400}}',  # R_B_Fx_11_0
    124: '{{0e000100000002005a00}}Tunnel{{0e000100000002006400}}',  # R_B_Fx_11_1
    125: '{{0e000100000002005a00}}Walkie-Talkie{{0e000100000002006400}}',  # R_B_Fx_12_0
    126: '{{0e000100000002005a00}}Walkie-Talkie{{0e000100000002006400}}',  # R_B_Fx_12_1
    127: '{{0e000100000002005a00}}Low Harmony{{0e000100000002006400}}',  # R_B_Fx_20_0
    128: '{{0e000100000002005a00}}Low Harmony{{0e000100000002006400}}',  # R_B_Fx_20_1
    129: '{{0e000100000002005a00}}High Harmony{{0e000100000002006400}}',  # R_B_Fx_21_0
    130: '{{0e000100000002005a00}}High Harmony{{0e000100000002006400}}',  # R_B_Fx_21_1
    131: '{{0e000100000002005a00}}Trio Harmony{{0e000100000002006400}}',  # R_B_Fx_22_0
    132: '{{0e000100000002005a00}}Trio Harmony{{0e000100000002006400}}',  # R_B_Fx_22_1
    133: '{{0e000100000002005a00}}Trumpet{{0e000100000002006400}}',  # R_B_Fx_30_0
    134: '{{0e000100000002005a00}}Trumpet{{0e000100000002006400}}',  # R_B_Fx_30_1
    135: '{{0e000100000002005a00}}Whistle{{0e000100000002006400}}',  # R_B_Fx_31_0
    136: '{{0e000100000002005a00}}Whistle{{0e000100000002006400}}',  # R_B_Fx_31_1
    137: '{{0e000100000002005a00}}Buzzer{{0e000100000002006400}}',  # R_B_Fx_32_0
    138: '{{0e000100000002005a00}}Buzzer{{0e000100000002006400}}',  # R_B_Fx_32_1
    140: 'Starting to record.',  # R_Rec_000
    141: 'Cancel',  # R_B_Rec_000
    142: 'Recording...',  # R_Rec_010
    143: '{{0e000100000002006000}}Recorded!\nYou can play with this sound.{{0e000100000002006400}}',  # R_Rec_020
    144: 'OK',  # R_B_Rec_020
    145: 'Cancel',  # R_B_Rec_021
    146: 'Saving the\nsound...',  # R_Rec_030
    147: "Couldn't save\nthe sound.",  # R_Rec_090
    148: 'OK',  # R_B_Rec_090
    150: 'Delete this sound?',  # R_Del_000
    151: 'Yes',  # R_B_Del_000
    152: 'No',  # R_B_Del_001
    153: 'Deleting the\nsound...',  # R_Del_020
    154: "Couldn't delete\nthe sound.",  # R_Del_010
    155: 'OK',  # R_B_Del_010
    159: 'Check the sound.',  # R_Sav_010
    160: 'Cancel',  # R_B_Sav_010
    161: 'This sound will overwrite\nthe original, which will be\ndeleted. Is that OK?',  # R_Sav_020
    162: 'OK',  # R_B_Sav_020
    163: 'Cancel',  # R_B_Sav_021
    164: 'Saving the\nsound...',  # R_Sav_030
    165: "Couldn't save\nthe sound.",  # R_Sav_090
    166: 'OK',  # R_B_Sav_090
    168: 'All sounds on this\npage will be moved.\n\nIs that OK?',  # R_VoiceMov_000
    169: 'Yes',  # R_VoiceMov_B000
    170: 'No',  # R_VoiceMov_B001
    171: 'Moving sounds...',  # R_VoiceMov_010
    172: 'Sounds moved.',  # R_VoiceMov_020
    173: 'OK',  # R_VoiceMov_B020
    174: "Couldn't move\nthe sounds.",  # R_VoiceMov_090
    175: 'OK',  # R_VoiceMov_B090
    176: 'All sounds on this\npage will be copied.\n\nIs that OK?',  # R_VoiceCpy_000
    177: 'Yes',  # R_VoiceCpy_B000
    178: 'No',  # R_VoiceCpy_B001
    179: 'Copying sounds...',  # R_VoiceCpy_010
    180: 'Sounds copied.',  # R_VoiceCpy_020
    181: 'OK',  # R_VoiceCpy_B020
    182: "Couldn't copy\nthe sounds.",  # R_VoiceCpy_090
    183: 'OK',  # R_VoiceCpy_B090
    185: 'Sample',  # Set_Col_000
    186: 'Color Settings',  # Set_Col_001
    187: 'Cancel',  # Set_B_Col_00
    188: 'OK',  # Set_B_Col_01
    189: 'Reset',  # Set_B_Col_02
    191: 'Choose Surround, Stereo\nor Mono for headphones\nand speakers.',  # Set_I_Out_00
    192: 'Audio Output',  # Set_Out_000
    193: 'Surround',  # Set_B_Out_00_0
    194: 'Surround',  # Set_B_Out_00_1
    195: 'Stereo',  # Set_B_Out_10_0
    196: 'Stereo',  # Set_B_Out_10_1
    197: 'Mono',  # Set_B_Out_20_0
    198: 'Mono',  # Set_B_Out_20_1
    199: 'OK',  # Set_B_Out_30
    201: 'Choose whether buttons make\na touch sound when playing\nmusic from the SD Card.',  # Set_I_SE_00
    202: 'Touch Sounds',  # Set_SE_000
    203: 'Off',  # Set_B_SE_00_0
    204: 'Off',  # Set_B_SE_00_1
    205: 'On',  # Set_B_SE_10_0
    206: 'On',  # Set_B_SE_10_1
    207: 'OK',  # Set_B_SE_20
    208: "Buttons won't make\ntouch sounds.",  # Set_SE_010
    209: 'Buttons will make\ntouch sounds.',  # Set_SE_020
    211: "Reset the save data?\n\n*Music and sounds\nwon't be deleted.",  # DM_SavDt_Init_001
    212: 'Yes',  # DM_SavDt_Init_B002
    213: 'No',  # DM_SavDt_Init_B003
    214: "The save data will be\nreset. Once reset,\nit can't be restored.\n\nAre you sure?",  # DM_SavDt_Init_000
    215: 'Cancel',  # DM_SavDt_Init_B000
    216: 'Reset',  # DM_SavDt_Init_B001
    217: 'This is the final check.\n\nReally reset?',  # DM_SavDt_Init_010
    218: 'Reset',  # DM_SavDt_Init_B010
    219: 'Cancel',  # DM_SavDt_Init_B011
    220: 'Resetting...\nPlease wait.',  # DM_SavDt_Init_020
    221: 'Reset complete.',  # DM_SavDt_Init_030
    222: 'OK',  # DM_SavDt_Init_B030
    223: "The SD Card is\nwrite-protected.\n\nFavorites on the SD Card\nwon't be reset.",  # DM_SavDt_Init_080
    224: 'OK',  # DM_SavDt_Init_B080
    225: 'Reset failed.',  # DM_SavDt_Init_090
    226: 'OK',  # DM_SavDt_Init_B090
    228: "All sounds in System\nMemory and on the SD Card\nwill be deleted. Deleted\nsounds can't be restored.\n\nIs that OK?",  # DM_Voice_Del_000
    229: 'Cancel',  # DM_Voice_Del_B000
    230: 'Delete',  # DM_Voice_Del_B001
    231: "All sounds shown on\nthe top screen will be\ndeleted. Deleted sounds\ncan't be restored.\n\nIs that OK?",  # DM_Voice_Del_010
    232: 'Cancel',  # DM_Voice_Del_B010
    233: 'Delete',  # DM_Voice_Del_B011
    234: 'Really delete?',  # DM_Voice_Del_020
    235: 'Delete',  # DM_Voice_Del_B020
    236: 'Cancel',  # DM_Voice_Del_B021
    237: 'Deleting...',  # DM_Voice_Del_030
    238: 'Deleted.',  # DM_Voice_Del_040
    239: 'OK',  # DM_Voice_Del_B040
    240: 'Delete failed.',  # DM_Voice_Del_090
    241: 'OK',  # DM_Voice_Del_B090
    243: 'Saving data received\nvia StreetPass...',  # CEC_Get_000
    244: "Couldn't save data\nreceived via StreetPass.",  # CEC_Get_110
    245: 'OK',  # CEC_B_Get_110
    246: 'You have {{0e000300290002000000}} StreetPass\nresults. Save them?',  # CEC_Get_200
    247: 'No',  # CEC_B_Get_200
    248: 'Yes',  # CEC_B_Get_201
    250: 'StreetPass Settings',  # CEC_Con_000
    251: 'Off',  # CEC_B_Con_000_0
    252: 'Off',  # CEC_B_Con_000_1
    253: 'On',  # CEC_B_Con_010_0
    254: 'On',  # CEC_B_Con_010_1
    255: 'StreetPass will be\nturned off.',  # CEC_Con_010
    256: 'StreetPass will be\nturned on.',  # CEC_Con_020
    257: 'OK',  # CEC_B_Con_020
    262: 'Turn on StreetPass?\n\n*StreetPass for 3DS Sound\nwill be registered\non the system.',  # CEC_Con_110
    263: 'No',  # CEC_B_Con_110
    264: 'Yes',  # CEC_B_Con_111
    265: 'Preparing\nStreetPass...',  # CEC_Con_120
    266: 'StreetPass is on.',  # CEC_Con_130
    267: 'OK',  # CEC_B_Con_130
    268: '{{0e000100000002005a00}}StreetPass is full.\n\nIn System Settings, go to\nStreetPass Management and\nturn off StreetPass for\nanother software title.{{0e000100000002006400}}',  # CEC_Con_200
    269: 'OK',  # CEC_B_Con_200
    270: "StreetPass with other\nusers can't be used\ndue to Parental Controls.",  # CEC_Con_210
    271: 'OK',  # CEC_B_Con_210
    272: 'To use StreetPass, you must\naccept the latest User\nAgreement.',  # CEC_Con_230
    273: 'OK',  # CEC_B_Con_230
    276: "Couldn't turn on\nStreetPass.\n\nFor details, check\nStreetPass Management\nin System Settings.",  # CEC_Con_250
    277: 'OK',  # CEC_B_Con_250
    278: "Couldn't turn on\nStreetPass.",  # CEC_Con_260
    279: 'OK',  # CEC_B_Con_260
    280: 'To use StreetPass,\nput songs in your\n"StreetPass" favorites.',  # CEC_Con_270
    281: 'OK',  # CEC_B_Con_270
    282: 'Turn off StreetPass\nfor 3DS Sound?',  # CEC_Con_300
    283: 'No',  # CEC_B_Con_300
    284: 'Yes',  # CEC_B_Con_301
    285: 'You have data received\nvia StreetPass.\n\nSave it?',  # CEC_Con_310
    286: 'No',  # CEC_B_Con_310
    287: 'Yes',  # CEC_B_Con_311
    288: 'Stopping StreetPass...',  # CEC_Con_320
    289: 'StreetPass is off.',  # CEC_Con_330
    290: 'OK',  # CEC_B_Con_330
    291: "Couldn't stop\nStreetPass.\n\nFor details, check\nStreetPass Management\nin System Settings.",  # CEC_Con_400
    292: 'OK',  # CEC_B_Con_400
    294: 'Your Matchmaker records\nwill be deleted.\n\nIs that OK?',  # CEC_Com_000
    295: 'No',  # CEC_B_Com_000
    296: 'Yes',  # CEC_B_Com_010
    297: 'Matchmaker records\ndeleted.',  # CEC_Com_100
    298: 'OK',  # CEC_B_Com_100
    300: 'StreetPass Hit Chart\nrecords will be deleted.\n\nIs that OK?',  # CEC_Hit_000
    301: 'No',  # CEC_B_Hit_000
    302: 'Yes',  # CEC_B_Hit_010
    303: 'StreetPass Hit Chart\nrecords deleted.',  # CEC_Hit_100
    304: 'OK',  # CEC_B_Hit_100
    306: 'Photo saved.\n\nYou can view saved\nphotos in Nintendo\n3DS Camera.',  # CEC_Cam_000
    307: 'OK',  # CEC_B_Cam_000
    310: "Couldn't save.",  # CEC_Cam_100
    311: 'OK',  # CEC_B_Cam_100
    312: 'Saving photo...',  # CEC_Cam_200
    314: 'You seem to have {{0e000300270002000000}}\nStreetPass results.\n\nTouch "StreetPass"\nto check them.',  # CEC_Notice_000
    315: 'OK',  # CEC_B_Notice_000
    316: 'Did StreetPass get\nturned off?\n\nTouch "StreetPass"\nto check.',  # CEC_Notice_050
    317: 'OK',  # CEC_B_Notice_050
    318: 'StreetPass was\ninterrupted.\n\nTo start again, turn\n"StreetPass" on.',  # CEC_Notice_100
    319: 'OK',  # CEC_B_Notice_100
    321: 'Preparing...',  # CEC_Migration_000
    322: "StreetPass for 3DS Sound\nwill be updated.\n\n*Data you've received\nwill be saved.",  # CEC_Migration_010
    323: 'OK',  # CEC_B_Migration_010
    324: 'StreetPass for 3DS Sound\nwill be updated.',  # CEC_Migration_011
    325: 'OK',  # CEC_B_Migration_011
    326: 'Updating StreetPass\nfor 3DS Sound...',  # CEC_Migration_020
    327: 'Updating StreetPass\nfor 3DS Sound...',  # CEC_Migration_021
    328: "Couldn't save data\nreceived via StreetPass.",  # CEC_Migration_025
    329: 'OK',  # CEC_B_Migration_025
    330: 'Preparing\nStreetPass...',  # CEC_Migration_030
    331: "Couldn't turn on\nStreetPass.",  # CEC_Migration_035
    332: 'OK',  # CEC_B_Migration_035
    333: 'StreetPass for 3DS Sound\nhas been updated.',  # CEC_Migration_040
    334: 'OK',  # CEC_B_Migration_040
}

GUIDE = {  # S_tips.msbt
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
    13: '{{0e0003002a0002000000}} Welcome to 3DS Sound!',  # T_001
    14: '{{0e0003002a0002000000}} Hello, Music!',  # T_002
    15: '{{0e0003002a0002000000}} Inserting and Removing SD Cards',  # T_003
    16: '{{0e0003002a0002000000}} Record Toward the Speech Bubble',  # T_004
    17: '{{0e0003002a0002000000}} Overwriting Sounds',  # T_005
    18: '{{0e0003002a0002000000}} Your Music Is Safe',  # T_006
    19: '{{0e0003002a0002000000}} Rereading the Tips',  # T_007
    20: '{{0e0003002a0002000000}} How to Quit',  # T_008
    23: '{{0e0003002a0002000000}} What Is StreetPass?',  # T_011
    25: '{{0e0003002a0002000000}} Starting StreetPass',  # T_013
    27: '{{0e0003002a0002000000}} StreetPass at Concerts',  # T_015
    28: '{{0e0003002a0002000000}} StreetPass Hit Chart',  # T_016
    29: '{{0e0003002a0002000000}} StreetPass Matchmaker',  # T_017
    30: '{{0e0003002a0002000000}} The Blue Parakeet',  # T_018
    31: '{{0e0003002a0002000000}} The Copycat Parakeet',  # T_019
    33: '{{0e0003002a0002000000}} Adding Favorites: Basics',  # T_021
    34: '{{0e0003002a0002000000}} Favorites: Top 10',  # T_022
    36: '{{0e0003002a0002000000}} Favorites: Secret',  # T_024
    37: '{{0e0003002a0002000000}} Favorites: StreetPass',  # T_025
    38: '{{0e0003002a0002000000}} Making New Favorites',  # T_026
    39: '{{0e0003002a0002000000}} Removing from Favorites',  # T_027
    40: '{{0e0003002a0002000000}} Deleting Favorites',  # T_028
    41: '{{0e0003002a0002000000}} Adding Favorites: Shortcuts',  # T_029
    42: '{{0e0003002a0002000000}} Adding Favorites: Advanced',  # T_030
    43: '{{0e0003002a0002000000}} Shuffle Picks',  # T_031
    44: '{{0e0003002a0002000000}} Shuffle Everything',  # T_032
    45: '{{0e0003002a0002000000}} Top 10 Played',  # T_033
    47: '{{0e0003002a0002000000}} LR Percussion',  # T_035
    48: '{{0e0003002a0002000000}} LR Percussion: Off',  # T_036
    49: '{{0e0003002a0002000000}} LR Percussion: Coins',  # T_037
    50: '{{0e0003002a0002000000}} LR Percussion: Animals',  # T_038
    51: '{{0e0003002a0002000000}} Pressing \ue004\ue005',  # T_039
    52: '{{0e0003002a0002000000}} Play a Folder',  # T_040
    53: '{{0e0003002a0002000000}} Repeat a Folder',  # T_041
    54: '{{0e0003002a0002000000}} Repeat One Song',  # T_042
    55: '{{0e0003002a0002000000}} Repeat a Section',  # T_043
    56: '{{0e0003002a0002000000}} Shuffle Play',  # T_044
    57: '{{0e0003002a0002000000}} Changing the Visualizer',  # T_045
    59: '{{0e0003002a0002000000}} Change the Sound: Radio',  # T_047
    60: '{{0e0003002a0002000000}} Change the Sound: Karaoke',  # T_048
    63: '{{0e0003002a0002000000}} Changing Pitch and Speed',  # T_051
    64: '{{0e0003002a0002000000}} Find a Key You Can Sing',  # T_052
    65: '{{0e0003002a0002000000}} Language Practice',  # T_053
    73: '{{0e0003002a0002000000}} Playing with Voices',  # T_061
    74: '{{0e0003002a0002000000}} Voice: Parakeet',  # T_062
    75: '{{0e0003002a0002000000}} Voice: Robot',  # T_063
    76: '{{0e0003002a0002000000}} Voice: Helium',  # T_064
    77: '{{0e0003002a0002000000}} Voice: Fan',  # T_065
    78: '{{0e0003002a0002000000}} Voice: Tunnel',  # T_066
    79: '{{0e0003002a0002000000}} Voice: Walkie-Talkie',  # T_067
    80: '{{0e0003002a0002000000}} Voice: High Harmony',  # T_068
    81: '{{0e0003002a0002000000}} Voice: Trio Harmony',  # T_069
    82: '{{0e0003002a0002000000}} Voice: Low Harmony',  # T_070
    87: "{{0e0003002a0002000000}} Changing Your Voice's Pitch",  # T_075
    90: '{{0e0003002a0002000000}} Tip: Auto Recording',  # T_078
    91: '{{0e0003002a0002000000}} Clipping Part of a Sound',  # T_079
    92: '{{0e0003002a0002000000}} Secret Words: Oyuobosa',  # T_080
    93: '{{0e0003002a0002000000}} Secret Words: Uotedemo',  # T_081
    94: '{{0e0003002a0002000000}} Secret Words: The Method',  # T_082
    95: '{{0e0003002a0002000000}} Secret Words: The Easy Way',  # T_083
    96: '{{0e0003002a0002000000}} Secret Words: Vowel Hint',  # T_084
    99: '{{0e0003002a0002000000}} What to Record: Messages',  # T_087
    100: '{{0e0003002a0002000000}} What to Record: Group Messages',  # T_088
    101: '{{0e0003002a0002000000}} Settings: Touch Sounds',  # T_089
    102: '{{0e0003002a0002000000}} Settings: Audio Output',  # T_090
    103: '{{0e0003002a0002000000}} Resume',  # T_091
    104: '{{0e0003002a0002000000}} Take a Break',  # T_092
    105: '{{0e0003002a0002000000}} Tip: \ue000 Button',  # T_093
    106: '{{0e0003002a0002000000}} Tip: \ue001 Button',  # T_094
    107: '{{0e0003002a0002000000}} Tip: \ue002 and \ue003 Buttons',  # T_095
    108: '{{0e0003002a0002000000}} Tip: \ue07e',  # T_096
    109: '{{0e0003002a0002000000}} Tip: \ue07d',  # T_097
    110: '{{0e0003002a0002000000}} Tip: \ue006',  # T_098
    112: '{{0e0003002a0002000000}} What to Record: Idea Notes',  # T_100
    114: '{{0e0003002a0002000000}} Listening with Earphones',  # T_102
    115: '{{0e0003002a0002000000}} Color-Coding Sounds',  # T_103
    116: '{{0e0003002a0002000000}} The Visualizer',  # T_104
    117: '{{0e0003002a0002000000}} Moving and Copying Sounds',  # T_105
    119: '{{0e0003002a0002000000}} Sounds to Another Page',  # T_107
    120: '{{0e0003002a0002000000}} Parakeet Tales: Walks',  # T_108
    121: '{{0e0003002a0002000000}} Parakeet Tales: Karaoke',  # T_109
    122: '{{0e0003002a0002000000}} Keepy-Uppy',  # T_110
    123: '{{0e0003002a0002000000}} Parakeet Tales: Your Own Voice',  # T_111
    124: '{{0e0003002a0002000000}} Black Pages and White Pages',  # T_112
    126: '{{0e0003002a0002000000}} Deleting Sounds in Bulk',  # T_114
    127: '{{0e0003002a0002000000}} Parakeet Tales: Ahhhh',  # T_115
    128: '{{0e0003002a0002000000}} Secret Words: A Code?',  # T_116
    129: '{{0e0003002a0002000000}} 3D Depth',  # T_117
    130: '{{0e0003002a0002000000}} Settings: Color Settings',  # T_118
    131: "{{0e0003002a0002000000}} The Parakeets' Live Show",  # T_119
    132: '{{0e0003002a0002000000}} Write-Protected SD Cards',  # T_120
    134: 'Welcome to\nNintendo 3DS Sound!',  # D_001_0
    135: 'With this software,\nyou can play music\nand record your voice\nto have fun with it.',  # D_001_1
    136: '{{0e00040001001600140053005f004700750069006400300033005f005500}}You can adjust the\nvolume with the\n{{0e00000003000400ff3200ff}}volume slider{{0e00000003000400454039ff}}.',  # D_001_2
    138: 'Thank you for putting\nmusic on the SD Card.',  # D_002_0
    139: 'If someone else did it\nfor you, be sure to\nsay "thank you."',  # D_002_1
    140: "{{0e00040001001600140053005f004700750069006400300032005f005500}}If you'd like to know more\nabout 3DS Sound,\n{{0e00000003000400454039ff}}touch me{{0e00000003000400454039ff}}.",  # D_002_2
    142: 'Before removing the SD Card,\n{{0e00000003000400ff3200ff}}turn the power off{{0e00000003000400454039ff}}.',  # D_003_0
    143: 'Then open the\n{{0e00000003000400ff3200ff}}slot cover{{0e00000003000400454039ff}} and push\nthe SD Card in until\nit clicks.',  # D_003_1
    144: 'Then pull out the\npart that pops out.',  # D_003_2
    145: "When inserting an SD Card,\nmake sure it's the\nright way around.",  # D_003_3
    146: 'Insert it with the shiny\ngold contacts facing\n{{0e00000003000400ff3200ff}}toward you{{0e00000003000400454039ff}}.',  # D_003_4
    148: 'If you record and\nyour voice sounds\ntoo quiet...',  # D_004_0
    149: '{{0e00040001001600140053005f004700750069006400300034005f005500}}try speaking toward\nthe speech bubble.',  # D_004_1
    150: '{{0e00040001001600140053005f004700750069006400300034005f005500}}The microphone is\nnear the Touch Screen.',  # D_004_2
    152: "Once you've played\naround with a sound,",  # D_005_0
    153: 'you can save it with\n"Overwrite."',  # D_005_1
    154: 'Change it again and again\nwith "Overwrite," and you\nmight make an even\nfunnier sound.',  # D_005_2
    155: 'If you want to keep\nthe original sound,',  # D_005_3
    156: 'don\'t forget to\n"Copy" it first.',  # D_005_4
    158: 'In 3DS Sound you can\nadd all kinds of\neffects to music, but',  # D_006_0
    159: 'the music on the SD Card\nitself is never changed.',  # D_006_1
    160: 'So feel free to play around.',  # D_006_2
    162: "The how-to tips and hints\nI've shown you",  # D_007_0
    163: 'can be {{0e00000003000400454039ff}}reread anytime\nfrom "How to Use"\nin "Settings."{{0e00000003000400454039ff}}',  # D_007_1
    165: 'Oh, I forgot\nto mention...',  # D_008_0
    166: '{{0e00040001001600140053005f004700750069006400300031005f005500}}To return to the\nHOME Menu, press\n{{0e00000003000400ff3200ff}}\ue073 HOME{{0e00000003000400454039ff}}.',  # D_008_1
    178: 'Do you know\nabout StreetPass?',  # D_011_0
    179: 'With StreetPass\nin 3DS Sound,',  # D_011_1
    180: 'you swap song info\nto check how well\nyou match up,',  # D_011_2
    181: 'and find out what\nmusic is popular\naround you.',  # D_011_3
    182: 'First, to get ready,\nput five songs that\nare very "you"',  # D_011_4
    183: 'into your "StreetPass"\nfavorites.',  # D_011_5
    191: 'To start StreetPass,',  # D_013_0
    192: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310039005f005500}}touch "StreetPass"{{0e00000003000400454039ff}}',  # D_013_1
    193: 'and turn StreetPass\non.',  # D_013_2
    194: "{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300036005f005500}}{{0e00000003000400454039ff}}Oh, and don't forget\nto slide the {{0e00000003000400ff3200ff}}wireless\nswitch{{0e00000003000400454039ff}} to turn\nwireless on.",  # D_013_3
    195: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300036005f005500}}{{0e00000003000400454039ff}}Why not head out\nsomewhere with\nyour music?',  # D_013_4
    201: 'When my big sister\nwent to see\n"The Parakeet Band" live,',  # D_015_0
    202: 'the Hit Chart went\nwild.',  # D_015_1
    203: 'Of course, everyone\nhad "The Parakeet Band"\nsongs in "StreetPass," but',  # D_015_2
    204: 'when real fans get\ntogether, even hidden\ngems make the\nHit Chart.',  # D_015_3
    205: "By the way, my sister's\nfan club member\nnumber is 002.\n\nAmazing!",  # D_015_4
    207: 'The "StreetPass\nHit Chart"',  # D_016_0
    208: 'collects song info\nfrom "StreetPass"\nfavorites to make\na hit chart.',  # D_016_1
    209: 'The people you pass\nvary from town to town.',  # D_016_2
    210: 'What songs and artists\nare popular around you?',  # D_016_3
    212: 'The "StreetPass\nMatchmaker"',  # D_017_0
    213: 'swaps song info from\n"StreetPass" favorites\nto rate how well you match\nwith people you pass.',  # D_017_1
    214: 'They say there are\n100 people out there\nwith exactly your\ntaste in music.',  # D_017_2
    215: '...Sorry,\nI made that up.',  # D_017_3
    217: 'Have you ever seen\na blue parakeet?',  # D_018_0
    218: "He's a good guy who\nbrings great news.",  # D_018_1
    219: 'If you see him,\ngive him a touch.',  # D_018_2
    220: "I'm such a good\nfriend.",  # D_018_3
    222: 'Parakeets are\nfamous for mimicking.',  # D_019_0
    223: "I sometimes mimic things\nI hear or sounds\nyou've saved, so",  # D_019_1
    224: "be careful not to say\nanything you wouldn't\nwant others to hear.",  # D_019_2
    230: '{{0e00040001001600140053005f004700750069006400310035005f005500}}Choose some music\nand touch\n{{0e00000003000400454039ff}}"Favorites"{{0e00000003000400454039ff}}',  # D_021_0
    231: '{{0e00040001001600140053005f004700750069006400310035005f005500}}to add it to\nyour favorites.',  # D_021_1
    233: "You can kind of tell\nwhat someone's like\nfrom their music, right?",  # D_022_0
    234: 'Show each other your\n"Top 10" favorites and\nyou might discover\na surprising side.',  # D_022_1
    235: 'I\'d love to show you\nmy hand-picked\n"Top 10," but',  # D_022_2
    236: "somehow... it's a\nlittle embarrassing.",  # D_022_3
    242: "If there are songs you'd\nrather keep private,",  # D_024_0
    243: 'put them in the\n"Secret" favorites.',  # D_024_1
    244: 'A song called\n"Hidden Song" would\nshow up as "H□□□□□."',  # D_024_2
    245: "But you'd tell me,\nwouldn't you?\n\n...What, no?",  # D_024_3
    247: 'You may already\nknow this, but\nStreetPass',  # D_025_0
    248: 'swaps info about\nthe music in your\n"StreetPass" favorites.',  # D_025_1
    249: 'Show off, play it cool,\nor just be honest...',  # D_025_2
    250: "it's up to you.",  # D_025_3
    252: 'Why not make your\nown favorites?',  # D_026_0
    253: 'Pick some music you\nlike, then touch "New"\nin "Favorites."',  # D_026_1
    254: 'You can change the\ntitle and icon to\nwhatever you like.',  # D_026_2
    255: 'I collect upbeat songs\nunder the title\n"Feel-Good Songs."',  # D_026_3
    256: "I always listen to\nthem when I'm down.",  # D_026_4
    258: 'Even if you remove\nmusic from favorites,',  # D_027_0
    259: "the music data on the\nSD Card isn't lost.",  # D_027_1
    260: "Don't worry.",  # D_027_2
    262: "Oh, are you stuck\nbecause you don't know\n{{0e00000003000400ff3200ff}}how to delete{{0e00000003000400454039ff}}\nfavorites?",  # D_028_0
    263: 'Sorry!\nI forgot to tell you.',  # D_028_1
    264: 'Open the favorites and\nremove all the songs,',  # D_028_2
    265: 'and the favorites\nitself will be\ndeleted too.',  # D_028_3
    266: "Even if favorites are\ndeleted, the music on\nthe SD Card isn't lost.",  # D_028_4
    267: "Don't worry.",  # D_028_5
    269: 'Choose a folder and\ntouch "Favorites"',  # D_029_0
    270: 'to add {{0e00000003000400454039ff}}all{{0e00000003000400454039ff}} the music\nin it to your\nfavorites.',  # D_029_1
    272: 'How about making\nfavorites this way\nfor a change?',  # D_030_0
    273: 'Choose a theme in\n"Shuffle Picks" and\ntouch "Favorites"',  # D_030_1
    274: 'to make favorites\nfrom my picks\njust as they are.',  # D_030_2
    276: 'When you listen with\n"Shuffle Picks,"',  # D_031_0
    277: "I'll choose the songs\nfor you.",  # D_031_1
    278: "When you're\nlistening to music,",  # D_031_2
    279: "I'm actually\nlistening along.",  # D_031_3
    280: 'The more you listen,\nthe better my picks\nmight get.',  # D_031_4
    282: 'If you want to leave\neverything to me,',  # D_032_0
    283: 'touch "Shuffle Everything"\nin "Shuffle Picks."',  # D_032_1
    284: "I'll shuffle every\nsong you have\nand play them for you.",  # D_032_2
    286: 'Which songs do you\nlisten to most?',  # D_033_0
    287: 'Try "Top 10 Played"\nin "Shuffle Picks."',  # D_033_1
    288: 'Were the 10 songs\nwhat you expected?\nOr a bit surprising?',  # D_033_2
    289: 'Why not put these\nsongs in your\n"Top 10" favorites?',  # D_033_3
    295: 'LR Percussion.\n\nPress the {{0e00000003000400ff3200ff}}\ue004 Button{{0e00000003000400454039ff}} or {{0e00000003000400ff3200ff}}\ue005\nButton{{0e00000003000400454039ff}} to play\nall kinds of\ninstrument sounds.{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_035_0
    296: "Play along with the\nmusic and you'll feel\nlike you're performing!",  # D_035_1
    297: '{{0e00040001001600140053005f004700750069006400310036005f005500}}Touch the icon to\nchange the instrument.',  # D_035_2
    299: 'While changing LR\nPercussion instruments,',  # D_036_0
    300: 'you may find one\nthat makes no sound.',  # D_036_1
    301: "When you're listening\nwith it in a bag, LR\nPercussion sounds won't\nbother you.",  # D_036_2
    302: 'What a handy\ninstrument.',  # D_036_3
    304: 'LR Percussion.\n\nWhen I hear that\ncoin sound,',  # D_037_0
    305: "I just can't stop\nplaying it.",  # D_037_1
    307: 'LR Percussion.\n\nMeow meow, woof woof!\nPlay them in time\nwith the rhythm and',  # D_038_0
    308: 'you might make friends\nwith cats and dogs.',  # D_038_1
    309: 'But...\ncats scare me.',  # D_038_2
    311: 'LR Percussion.\n\nWith some instruments,\nhow you press the buttons',  # D_039_0
    312: 'can change the sound.',  # D_039_1
    313: '{{0e00000003000400ff3200ff}}Try {{0e00000003000400ff3200ff}}holding{{0e00000003000400454039ff}} or\n{{0e00000003000400ff3200ff}}pressing both{{0e00000003000400454039ff}} with\nall kinds of\ninstruments.{{0e00000003000400454039ff}}',  # D_039_2
    315: '{{0e00040001001600140053005f004700750069006400320030005f005500}}This play mode plays\nthe songs in a folder\n{{0e00000003000400ff3200ff}}in order{{0e00000003000400454039ff}} and then\n{{0e00000003000400454039ff}}stops{{0e00000003000400454039ff}}.',  # D_040_0
    316: '{{0e00040001001600140053005f004700750069006400320030005f005500}}I listen to about\n30 minutes of songs\nin one go',  # D_040_1
    317: '{{0e00040001001600140053005f004700750069006400320030005f005500}}while working up a sweat\nwith my daily\nParakeet Workout.',  # D_040_2
    318: "{{0e00040001001600140053005f004700750069006400320030005f005500}}It's like a timer.",  # D_040_3
    320: '{{0e00040001001600140053005f004700750069006400300039005f005500}}This play mode\n{{0e00000003000400ff3200ff}}repeats{{0e00000003000400454039ff}} the songs\nin a folder.{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_041_0
    321: "{{0e00040001001600140053005f004700750069006400300039005f005500}}It's perfect for me,\nbecause I play songs\non heavy rotation.",  # D_041_1
    322: '{{0e00040001001600140053005f004700750069006400300039005f005500}}Do you like playing\nsongs on repeat?\n\nOr do you',  # D_041_2
    323: '{{0e00040001001600140053005f004700750069006400300039005f005500}}prefer to savor\nthe afterglow?',  # D_041_3
    325: '{{0e00040001001600140053005f004700750069006400310030005f005500}}This play mode\n{{0e00000003000400ff3200ff}}repeats one song{{0e00000003000400454039ff}}.{{0e00000003000400ff3200ff}}{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_042_0
    326: '{{0e00040001001600140053005f004700750069006400310030005f005500}}Why not use it to learn\na new song by\nlistening closely?',  # D_042_1
    327: '{{0e00040001001600140053005f004700750069006400310030005f005500}}At karaoke, I always\nkeep up with the\nnewest songs.',  # D_042_2
    329: '{{0e00040001001600140053005f004700750069006400310031005f005500}}This play mode',  # D_043_0
    330: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300038005f005500}}repeats the section\nbetween the {{0e00000003000400ff3200ff}}A{{0e00000003000400454039ff}} and {{0e00000003000400ff3200ff}}B{{0e00000003000400454039ff}}\nmarkers, which\nyou can slide.{{0e00000003000400454039ff}}',  # D_043_1
    331: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300038005f005500}}{{0e00000003000400454039ff}}Listen to tricky\nphrases again and again\nto boost your language\nskills.',  # D_043_2
    332: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300038005f005500}}{{0e00000003000400454039ff}}I\'m studying Cat\nso cats won\'t\npick on me.\n\n"Meow-meow-meow~"',  # D_043_3
    334: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310032005f005500}}{{0e00000003000400454039ff}}This play mode\n{{0e00000003000400ff3200ff}}shuffles{{0e00000003000400454039ff}} the songs\nin a folder and\nrepeats them.',  # D_044_0
    335: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310032005f005500}}{{0e00000003000400454039ff}}When the order changes,\neven familiar songs\nsound fresh again.',  # D_044_1
    336: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310032005f005500}}{{0e00000003000400454039ff}}By the way, sometimes\nwhen I guess the next song,\nI get it right.',  # D_044_2
    337: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310032005f005500}}{{0e00000003000400454039ff}}Could I be psychic?',  # D_044_3
    339: 'Why not change the\n"Visualizer" to\nmatch the music?',  # D_045_0
    340: 'Touch the round\nswitch with\nthe string',  # D_045_1
    341: 'and enjoy the\nvisuals you like.',  # D_045_2
    346: '{{0e00040001001600140053005f004700750069006400310034005f005500}}Touch this icon\nand turn "Radio" on\nwhile listening',  # D_047_0
    347: "Doesn't the retro\nsound make you\nfeel nostalgic?",  # D_047_1
    348: 'It reminds me of my\nstudent days, when\nradio music\nkept me going.',  # D_047_2
    349: 'Those were the days...\nI want to go back.',  # D_047_3
    351: '{{0e00040001001600140053005f004700750069006400310034005f005500}}Touch this icon\nand turn "Karaoke" on\nwhile listening',  # D_048_0
    352: 'and the vocals get\nquieter, which is\nhandy for karaoke practice.',  # D_048_1
    362: '{{0e00040001001600140053005f004700750069006400310033005f005500}}Touch this icon',  # D_051_0
    363: '{{0e00040001001600140053005f004700750069006400310033005f005500}}to listen with the\npitch and speed\nchanged.',  # D_051_1
    364: 'Up and down changes\nthe pitch,',  # D_051_2
    365: 'and left and right\nchanges the speed.',  # D_051_3
    366: 'You can change\neach one separately.',  # D_051_4
    368: 'There are songs that\nare too high to sing.',  # D_052_0
    369: 'For those, try\nchanging the pitch.',  # D_052_1
    370: 'Use \ue07d to adjust\none semitone at a time.',  # D_052_2
    371: 'I used to stick to the\noriginal key, but since\nfinding a key that suits me\nI can sing more songs.',  # D_052_3
    372: 'Easy to sing is best.',  # D_052_4
    374: 'If you get used to fast\nspeech in listening tests,',  # D_053_0
    375: 'normal speed feels\neasier to understand.',  # D_053_1
    376: 'You can set the speed\nup to twice as fast,',  # D_053_2
    377: 'and down to half\nspeed.',  # D_053_3
    378: 'When I study Cat,\nI listen at 1.5x\nspeed to train\nmy ears.',  # D_053_4
    411: 'To play with voices,',  # D_061_1
    412: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310034005f005500}}{{0e00000003000400454039ff}}touch this icon.',  # D_061_2
    413: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300037005f005500}}{{0e00000003000400454039ff}}{{0e00000003000400ff3200ff}}Keep touching{{0e00000003000400454039ff}} it to\nchange the effect\neven more.{{0e00000003000400ff3200ff}}{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_061_3
    415: 'Turn "Parakeet" on\nand listen to\na sound...',  # D_062_0
    416: 'It sounds just like me.\n"Friends! More friends!"',  # D_062_1
    418: 'Turn "Robot" on\nand listen to\na sound...',  # D_063_0
    419: 'It sounds mechanical.\n"Are-you-cold?"\n\nThe voice may be cold,\nbut the heart is warm.',  # D_063_1
    421: 'Turn "Helium" on\nand listen to\na sound...',  # D_064_0
    422: 'Your voice goes high,\nlike a tiny bug.\n"A parakeet! Run!"',  # D_064_1
    424: 'Turn "Fan" on\nand listen to\na sound...',  # D_065_0
    425: 'Anyone can be an alien.',  # D_065_1
    426: 'And of course you have\nto say...\n"We... come... in peace!"',  # D_065_2
    428: 'Turn "Tunnel" on\nand listen to\na sound...',  # D_066_0
    429: 'It echoes like you\'re\nin a hot spring.\n"Ahh, this is nice~"',  # D_066_1
    431: 'Turn "Walkie-Talkie" on\nand listen to\na sound...',  # D_067_0
    432: 'It sounds like a voice\nsent over the radio.\n"Do you read me?"',  # D_067_1
    434: 'Turn "High Harmony" on\nand listen to\na sound...',  # D_068_0
    435: 'You feel like a fairy.\n"Welcome to the forest."',  # D_068_1
    437: 'Turn "Trio Harmony" on\nand listen to\na sound...',  # D_069_0
    438: 'One voice makes\na trio.',  # D_069_1
    439: 'Two voices make\na sextet.',  # D_069_2
    440: "And ten voices!...\nOh, that's enough?\nExcuse me.",  # D_069_3
    442: 'Turn "Low Harmony" on\nand listen to\na sound...',  # D_070_0
    443: 'You sound like a genie.\n"Your wish is my command."',  # D_070_1
    459: 'By changing the\npitch of a voice,',  # D_075_0
    460: "you can make a woman's\nvoice sound like a man's,\nand a man's like a woman's.",  # D_075_1
    461: 'Will your voice sound\ncool? Or cute?',  # D_075_2
    472: 'When recording,\nspeak loudly toward\nthe speech bubble',  # D_078_0
    473: 'and recording starts\nautomatically.',  # D_078_1
    475: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310031005f005500}}{{0e00000003000400454039ff}}This play mode',  # D_079_0
    476: '{{0e00000003000400ff3200ff}}{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400300038005f005500}}plays only the section\nbetween the {{0e00000003000400ff3200ff}}A{{0e00000003000400454039ff}} and {{0e00000003000400ff3200ff}}B{{0e00000003000400454039ff}}\nmarkers, which\nyou can slide.{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_079_1
    477: 'Then "Overwrite" to\n{{0e00000003000400ff3200ff}}clip and save it{{0e00000003000400454039ff}}.',  # D_079_2
    479: 'I figured out the\nmystery of "Oyuobosa."',  # D_080_0
    480: "Get this! It's a\nsecret message for\nmaking friends.",  # D_080_1
    481: 'Try playing\n"Oyuobosa" backward.',  # D_080_2
    482: 'My answer is "YES,"\nof course!',  # D_080_3
    484: "When something good\nhappens, here's a\nsecret word for you:",  # D_081_0
    485: '"Uotedemo"',  # D_081_1
    486: 'The trick is to record\nit fairly quietly at first.',  # D_081_2
    487: 'What does it sound\nlike backward?',  # D_081_3
    489: "For those who know\nJapanese romaji, here's\nmore on making\nsecret words.",  # D_082_0
    490: 'Let\'s try making\n"arigatou"\n(thank you).',  # D_082_1
    491: 'First, write it in\nromaji.\n\n"arigatou"\n↓\n"ARIGATOU"',  # D_082_2
    492: 'Then reverse it.\n\n"ARIGATOU"\n↓\n"UOTAGIRA"',  # D_082_3
    493: 'Read it out, and it\'s\n"u-o-ta-gi-ra."',  # D_082_4
    494: 'That\'s the secret word\nfor saying\n"thank you."',  # D_082_5
    495: 'Record "uotagira"\nand play it\nbackward.',  # D_082_6
    496: 'Does it sound like\n"arigatou"?',  # D_082_7
    498: "Here's how to make\nsecret words you can\nhear in reverse.",  # D_083_0
    499: "It's easy.\nJust record what you\nwant to say and\nplay it backward.",  # D_083_1
    500: 'For example, record\n"oishii" (tasty)\nand play it backward',  # D_083_2
    501: 'and it sounds like\n"iishio."',  # D_083_3
    502: 'This "iishio" is the\nsecret word for\nsaying "oishii."',  # D_083_4
    503: 'Record "iishio"\nand play it\nbackward.',  # D_083_5
    504: 'It should sound\nlike "oishii."',  # D_083_6
    505: 'Backward twice is\nback to normal...',  # D_083_7
    506: "Obvious when you\nthink about it, but\nit's the easiest way.",  # D_083_8
    508: 'A tip for choosing\nsecret words:',  # D_084_0
    509: 'pick words that start\nwith a vowel sound\n(a, i, u, e or o).',  # D_084_1
    510: '"Asobou yo"\n"Omedetou"\n"Oishii"\n"Arigatou"',  # D_084_2
    511: "They're easier to say\nwhen reversed.",  # D_084_3
    520: 'A recorded message\nfor Dad when he\ncomes home late.\n"Thanks for all\nyour hard work!"',  # D_087_0
    522: 'Why not make a group\nvoice message for a\ngraduation or wedding?',  # D_088_0
    524: 'If touch sounds bother\nyou while listening,',  # D_089_0
    525: 'you can turn them off\nin "Settings."',  # D_089_1
    527: 'In 3DS Sound, you can\neasily change the\naudio output.',  # D_090_0
    528: 'In "Settings," under\n"Audio Output,"',  # D_090_1
    529: 'choose "Surround,"\n"Stereo" or "Mono."',  # D_090_2
    530: '"Stereo" is like hearing\nthe performance from\nthe front,',  # D_090_3
    531: 'and "Surround" is like\nbeing surrounded\nby sound.',  # D_090_4
    533: 'Touch "Resume"',  # D_091_0
    534: 'to pick up from where\nyou left off last time.',  # D_091_1
    536: 'Ahh, a moment to relax.\nWhy not take a break?',  # D_092_0
    538: '{{0e00000003000400ff3200ff}}Press the {{0e00000003000400454039ff}}\ue000 Button{{0e00000003000400454039ff}} to\nconfirm a selection\nand more,{{0e00000003000400454039ff}}',  # D_093_0
    539: '{{0e00000003000400454039ff}}and also to play\nand pause.{{0e00000003000400454039ff}}',  # D_093_1
    541: '{{0e00000003000400ff3200ff}}Press the {{0e00000003000400454039ff}}\ue001 Button{{0e00000003000400454039ff}} to\ngo back, close, cancel\nand more,{{0e00000003000400454039ff}}',  # D_094_0
    542: 'and also to reset\nthe pitch and speed.{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_094_1
    544: '{{0e00000003000400ff3200ff}}Press the {{0e00000003000400ff3200ff}}\ue002 Button{{0e00000003000400454039ff}} or\n{{0e00000003000400454039ff}}\ue003 Button to change\nthe LR Percussion\ninstrument.',  # D_095_0
    546: '{{0e00000003000400ff3200ff}}Press {{0e00000003000400ff3200ff}}\ue07b{{0e00000003000400454039ff}} to skip to the\nprevious song, and {{0e00000003000400454039ff}}\ue07c{{0e00000003000400454039ff}}\nto skip to the next.{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_096_0
    548: '{{0e00000003000400ff3200ff}}Press {{0e00000003000400ff3200ff}}\ue079{{0e00000003000400454039ff}} or {{0e00000003000400454039ff}}\ue07a to\nswitch the\n"Visualizer."',  # D_097_0
    550: 'While a sound is\nplaying, use {{0e00000003000400ff3200ff}}\ue006{{0e00000003000400454039ff}} to\nselect another sound.',  # D_098_0
    556: 'When a great melody\npops into your head,\nrecord it before\nyou forget!',  # D_100_0
    564: 'With earphones or\nheadphones,',  # D_102_0
    565: 'you can listen to music\neven with the system\nclosed.',  # D_102_1
    566: "It's handy for\nlistening on the go.",  # D_102_2
    567: "But if it's always\nclosed, we don't see\neach other much.\nI'd get lonely.",  # D_102_3
    569: 'When you save a sound,\nyou can {{0e00000003000400454039ff}}choose\na color{{0e00000003000400454039ff}}.',  # D_103_0
    570: 'Touch the color you\nlike on the colorful\nOK button.',  # D_103_1
    571: 'Red for my own voice,\ngreen for friends.',  # D_103_2
    572: 'I color-code by\nwho recorded it.',  # D_103_3
    573: 'And orange is...',  # D_103_4
    575: 'The top-screen visuals\nthat change with\nthe music',  # D_104_0
    576: 'are called the\n"Visualizer."',  # D_104_1
    577: 'What a cool name.',  # D_104_2
    579: 'Touch a sound\nand slide it',  # D_105_0
    580: 'to swap its place.',  # D_105_1
    581: 'Touch "Copy"',  # D_105_2
    582: 'to switch to copying.',  # D_105_3
    583: 'Touch the sound you\nwant to copy and\nslide it.',  # D_105_4
    590: 'To take a sound\nto another page,',  # D_107_0
    591: 'touch the sound\nyou want to take',  # D_107_1
    592: 'and drag it onto the\npage-switch button.',  # D_107_2
    594: 'I often sing while\nI go for walks, but',  # D_108_0
    595: 'if I stop singing when\nsomeone walks past,',  # D_108_1
    596: "I'd hate them to think\nI'm embarrassed, so",  # D_108_2
    597: 'I end up singing\neven louder.',  # D_108_3
    598: "I'm sure I'm not\nthe only one.",  # D_108_4
    600: 'I love solo\nkaraoke.',  # D_109_0
    601: "I can sing and dance\nwithout worrying who's\nwatching,",  # D_109_1
    602: "and sing songs I'm too\nunpracticed to sing in\nfront of people over\nand over.",  # D_109_2
    603: 'But choosing songs\nwastes time, so',  # D_109_3
    604: 'I make a list of\nsongs I want to sing\nbeforehand.',  # D_109_4
    605: 'With solo karaoke,\nthe game starts\nbefore you sing.',  # D_109_5
    607: 'The "Visualizer"\nKeepy-Uppy',  # D_110_0
    608: 'can actually be\ncontrolled with the\n{{0e00000003000400ff3200ff}}Circle Pad{{0e00000003000400454039ff}}.',  # D_110_1
    609: 'See how many times\nyou can keep the ball\nup without dropping it.',  # D_110_2
    610: 'Olé!',  # D_110_3
    612: "Doesn't your recorded\nvoice sound like\nsomeone else?",  # D_111_0
    613: 'Besides the voice\nthat travels through\nthe air,',  # D_111_1
    614: 'you also hear your voice\nfrom the inside, traveling\nthrough your head.',  # D_111_2
    615: 'A recording only\ncaptures the voice\nin the air, so',  # D_111_3
    616: 'it sounds different\nfrom what you expect.',  # D_111_4
    617: 'The voice I hear\nas mine is much\nlovelier!',  # D_111_5
    619: 'Each page (one screen)\ncan hold\n{{0e00000003000400454039ff}}18{{0e00000003000400454039ff}} sounds.',  # D_112_0
    620: 'Sounds on black pages\nare saved in\n{{0e00000003000400ff3200ff}}System Memory{{0e00000003000400454039ff}},',  # D_112_1
    621: 'and sounds on white\npages are saved on\nthe {{0e00000003000400ff3200ff}}SD Card{{0e00000003000400454039ff}}.',  # D_112_2
    627: 'To delete sounds\nin bulk,',  # D_114_0
    628: 'touch "Data Management"\nin "Settings."',  # D_114_1
    629: 'You can delete one\npage at a time or\nall pages.',  # D_114_2
    631: 'When driving on\na bumpy road,',  # D_115_0
    632: 'don\'t you want to go\n"Ahhhhhhhhhh"?',  # D_115_1
    633: "Your voice wobbles,\nand it's fun.",  # D_115_2
    634: '...Is it just me??',  # D_115_3
    636: 'Do you know what\n"Oyuobosa" means?',  # D_116_0
    637: 'Apparently it makes\nsense if you record it\nand listen.',  # D_116_1
    638: "But I haven't a clue.\nIs it some kind of code?",  # D_116_2
    640: 'To adjust the 3D effect\nof the "Visualizer,"',  # D_117_0
    641: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400310038005f005500}}{{0e00000003000400454039ff}}{{0e00000003000400ff3200ff}}move the {{0e00000003000400454039ff}}3D depth\nslider up and down.',  # D_117_1
    643: 'In "Color Settings,"\nyou can change the\nscreen\'s {{0e00000003000400ff3200ff}}theme color{{0e00000003000400454039ff}}.',  # D_118_0
    644: 'If choosing a color\nis a hassle, flick\nthe cursor and leave\nit to luck.',  # D_118_1
    645: 'Touch "Reset" to go\nback to the original\ncolor.',  # D_118_2
    647: 'Somewhere today,\na parakeet duo\nputs on a live show.',  # D_119_0
    648: 'Singing? Acting? Comedy?\nThey say the two are\nmulti-talented,',  # D_119_1
    649: 'but nobody has\never seen it.',  # D_119_2
    650: "They're always\npracticing in secret.",  # D_119_3
    652: 'Hm?',  # D_120_0
    653: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400320031005f005500}}{{0e00000003000400454039ff}}The SD Card is\nwrite-protected.',  # D_120_1
    654: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400320031005f005500}}{{0e00000003000400454039ff}}With a write-protected\nSD Card, 3DS Sound\ncan only play music, so',  # D_120_2
    655: '{{0e00040001001600140053005f004700750069006400320032005f005500}}turn the power off and\nslide the {{0e00000003000400ff3200ff}}lock switch{{0e00000003000400454039ff}}\nup as shown above.{{0e00000003000400454039ff}}{{0e00000003000400454039ff}}',  # D_120_3
    656: '{{0e00000003000400454039ff}}{{0e00040001001600140053005f004700750069006400320032005f005500}}{{0e00000003000400454039ff}}Thank you very much.\n(bows)',  # D_120_4
}
