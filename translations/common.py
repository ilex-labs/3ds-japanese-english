# SPDX-License-Identifier: GPL-3.0-or-later
"""Shared tokens used by the translation tables.

Strings are written in a "display" form: plain text, with Nintendo's MSBT
control codes kept as {{hex}} tokens copied verbatim from the original
files. The build checks that every translated string keeps exactly the
same control codes, button icons and %-placeholders as the original.
"""

# Button / icon glyphs (private-use characters in the 3DS system font)
A = '\ue000'
B = '\ue001'
X = '\ue002'
Y = '\ue003'
L = '\ue004'
R = '\ue005'
QUIT = '\ue071'     # "close software" icon
HOME = '\ue073'     # HOME button icon
STEPS = '\ue074'    # pedometer icon
COIN = '\ue075'     # Play Coin icon
POWER = '\ue078'    # POWER button icon
UP = '\ue079'       # D-pad up
DOWN = '\ue07a'     # D-pad down
UPDOWN = '\ue07c'   # D-pad up/down

# Formatting codes copied verbatim from the original files
GAP = '{{0e000100000002001400}}\n\u3000{{0f0001000000}}\n'      # small blank spacer line
NOTE = '{{0e000100000002005500}}{{0e000000030004003c3c3cff}}'   # small gray text start
NOTE_END = '{{0e00000003000400000000ff}}{{0f0001000000}}'
SMALL = '{{0e000100000002005500}}'                             # small text start (no color)
SIZE_END = '{{0f0001000000}}'


def SIZE(pct, text):
    """Wrap text in a font-size code (percent of normal).

    Only use this in the HOME Menu. System Settings renders labels with
    added size codes as blank, so the build rejects it there.
    """
    return '{{0e00010000000200%02x00}}' % pct + text + '{{0f0001000000}}'
