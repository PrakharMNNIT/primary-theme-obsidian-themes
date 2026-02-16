#!/usr/bin/env python3
"""
Generate 4 color palette variants for Primary Obsidian Theme.
Each palette replaces ONLY the color primitive HSL/RGB values,
keeping all variable names, structure, and non-color code identical.
"""

import re
import os
import shutil

PALETTES_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'scss', '10_foundations', 'palettes')
ORIGINAL = os.path.join(PALETTES_DIR, '_classic-original.scss')

# ─────────────────────────────────────────────
# PALETTE DEFINITIONS
# Each palette defines replacements for color primitives only
# Format: { 'search_pattern': 'replacement_value' }
# ─────────────────────────────────────────────

PALETTES = {
    # ───── Blossom Neo ─────
    # Neobrutalist kawaii: pink/teal/amber with flat colored shadows
    # Fonts: Poppins + Fira Code
    'blossom-neo': {
        'name': 'Blossom Neo',
        'light': {
            # Grayscale: warm pink-tinted (hue ~330-340)
            # bg rgb(246,230,238)=hsl(330,47%,93%), fg rgb(91,91,91)=hsl(0,0%,36%)
            'color-l-gray-10':  'hsla(330, 40%, 97%, 1)',
            'color-l-gray-20':  'hsla(330, 38%, 95%, 1)',
            'color-l-gray-30':  'hsla(330, 30%, 92%, 1)',
            'color-l-gray-40':  'hsla(330, 24%, 89%, 1)',
            'color-l-gray-50':  'hsla(330, 18%, 86%, 1)',
            'color-l-gray-60':  'hsla(330, 14%, 80%, 1)',
            'color-l-gray-70':  'hsla(330, 8%, 68%, 1)',
            'color-l-gray-80':  'hsla(330, 5%, 56%, 1)',
            'color-l-gray-90':  'hsla(330, 3%, 46%, 1)',
            'color-l-gray-100': 'hsla(330, 3%, 38%, 1)',
            'color-l-gray-110': 'hsla(330, 3%, 34%, 1)',
            'color-l-gray-120': 'hsla(330, 4%, 28%, 1)',
            'color-l-gray-130': 'hsla(330, 5%, 22%, 1)',
            'color-l-gray-140': 'hsla(330, 6%, 16%, 1)',
            'color-l-alpha-gray': 'hsla(330, 8%, 68%, 0.15)',
            # Red → Coral (destructive: rgb(249,111,112))
            'color-l-red-10':  'hsla(0, 88%, 76%, 1)',
            'color-l-red-20':  'hsla(0, 92%, 71%, 1)',
            'color-l-red-30':  'hsla(356, 72%, 58%, 1)',
            'color-l-red-40':  'hsla(352, 65%, 45%, 1)',
            'color-l-alpha-red': 'hsla(0, 85%, 70%, 0.2)',
            # Orange → Warm Amber (accent: rgb(251,226,167))
            'color-l-orange-10': 'hsla(30, 80%, 68%, 1)',
            'color-l-orange-20': 'hsla(28, 85%, 60%, 1)',
            'color-l-orange-30': 'hsla(25, 78%, 52%, 1)',
            'color-l-orange-40': 'hsla(22, 82%, 40%, 1)',
            'color-l-alpha-orange': 'hsla(28, 90%, 60%, 0.2)',
            # Yellow → Cream/Gold (card: rgb(253,237,201))
            'color-l-yellow-10': 'hsla(42, 88%, 82%, 1)',
            'color-l-yellow-20': 'hsla(40, 85%, 72%, 1)',
            'color-l-yellow-30': 'hsla(38, 78%, 58%, 1)',
            'color-l-yellow-40': 'hsla(36, 82%, 44%, 1)',
            'color-l-alpha-yellow': 'hsla(42, 93%, 82%, 0.25)',
            # Green → Teal (secondary: rgb(138,207,209))
            'color-l-green-10': 'hsla(182, 42%, 72%, 1)',
            'color-l-green-20': 'hsla(182, 48%, 62%, 1)',
            'color-l-green-30': 'hsla(182, 45%, 50%, 1)',
            'color-l-green-40': 'hsla(182, 52%, 38%, 1)',
            'color-l-alpha-green': 'hsla(182, 40%, 68%, 0.2)',
            # Blue → Muted Teal-Blue (muted: rgb(178,225,235))
            'color-l-blue-10':  'hsla(191, 48%, 78%, 1)',
            'color-l-blue-20':  'hsla(191, 52%, 65%, 1)',
            'color-l-blue-30':  'hsla(191, 48%, 50%, 1)',
            'color-l-blue-40':  'hsla(191, 55%, 36%, 1)',
            'color-l-alpha-blue': 'hsla(191, 50%, 65%, 0.2)',
            # Purple → Hot Pink/Magenta (primary: rgb(208,79,153))
            'color-l-purple-10': 'hsla(326, 52%, 72%, 1)',
            'color-l-purple-20': 'hsla(326, 55%, 62%, 1)',
            'color-l-purple-30': 'hsla(326, 55%, 52%, 1)',
            'color-l-purple-40': 'hsla(326, 58%, 40%, 1)',
            'color-l-alpha-purple': 'hsla(326, 55%, 56%, 0.2)',
            # Accent
            'accent-h-light': '326',
            'accent-s-light': '55%',
            'accent-l-light': '56%',
            # Special colors
            'color-gray-rgb-light':   '195, 185, 190',
            'color-gray-light':       'hsla(330, 8%, 75%, 1)',
            'color-red-rgb-light':    '249, 111, 112',
            'color-red-light':        'hsla(0, 92%, 71%, 1)',
            'color-orange-rgb-light': '240, 170, 100',
            'color-orange-light':     'hsla(30, 82%, 60%, 1)',
            'color-yellow-rgb-light': '251, 226, 167',
            'color-yellow-light':     'hsla(42, 93%, 82%, 1)',
            'color-green-rgb-light':  '138, 207, 209',
            'color-green-light':      'hsla(182, 42%, 68%, 1)',
            'color-cyan-rgb-light':   '132, 210, 226',
            'color-cyan-light':       'hsla(191, 55%, 70%, 1)',
            'color-blue-rgb-light':   '120, 185, 210',
            'color-blue-light':       'hsla(197, 50%, 65%, 1)',
            'color-purple-rgb-light': '208, 79, 153',
            'color-purple-light':     'hsla(326, 55%, 56%, 1)',
            'color-pink-rgb-light':   '243, 160, 202',
            'color-pink-light':       'hsla(330, 78%, 79%, 1)',
        },
        'dark': {
            # Grayscale: deep teal-navy (bg: rgb(18,36,46)=hsl(201,44%,13%))
            'color-d-gray-10':  'hsla(334, 35%, 92%, 1)',
            'color-d-gray-20':  'hsla(334, 28%, 80%, 1)',
            'color-d-gray-30':  'hsla(346, 20%, 70%, 1)',
            'color-d-gray-40':  'hsla(346, 14%, 55%, 1)',
            'color-d-gray-50':  'hsla(200, 12%, 42%, 1)',
            'color-d-gray-60':  'hsla(201, 18%, 30%, 1)',
            'color-d-gray-70':  'hsla(201, 24%, 24%, 1)',
            'color-d-gray-80':  'hsla(201, 30%, 18%, 1)',
            'color-d-gray-90':  'hsla(201, 36%, 15%, 1)',
            'color-d-gray-100': 'hsla(201, 40%, 13%, 1)',
            'color-d-gray-110': 'hsla(201, 42%, 12%, 1)',
            'color-d-gray-120': 'hsla(201, 44%, 11%, 1)',
            'color-d-gray-130': 'hsla(201, 46%, 9%, 1)',
            'color-d-gray-140': 'hsla(201, 48%, 7%, 1)',
            'color-d-alpha-gray': 'hsla(200, 12%, 42%, 0.2)',
            # Red → Pink-Rose (destructive: rgb(227,94,164))
            'color-d-red-10':  'hsla(328, 75%, 75%, 1)',
            'color-d-red-20':  'hsla(328, 70%, 68%, 1)',
            'color-d-red-30':  'hsla(328, 65%, 60%, 1)',
            'color-d-red-40':  'hsla(328, 58%, 50%, 1)',
            'color-d-alpha-red': 'hsla(328, 70%, 65%, 0.2)',
            # Orange → Warm Amber
            'color-d-orange-10': 'hsla(30, 78%, 62%, 1)',
            'color-d-orange-20': 'hsla(28, 75%, 54%, 1)',
            'color-d-orange-30': 'hsla(25, 70%, 48%, 1)',
            'color-d-orange-40': 'hsla(22, 68%, 40%, 1)',
            'color-d-alpha-orange': 'hsla(28, 78%, 55%, 0.2)',
            # Yellow → Warm Gold (primary in dark: rgb(251,226,167))
            'color-d-yellow-10': 'hsla(42, 90%, 82%, 1)',
            'color-d-yellow-20': 'hsla(40, 85%, 72%, 1)',
            'color-d-yellow-30': 'hsla(38, 78%, 62%, 1)',
            'color-d-yellow-40': 'hsla(36, 72%, 52%, 1)',
            'color-d-alpha-yellow': 'hsla(42, 93%, 82%, 0.2)',
            # Green → Teal (ring: rgb(80,175,182))
            'color-d-green-10': 'hsla(184, 48%, 58%, 1)',
            'color-d-green-20': 'hsla(184, 45%, 48%, 1)',
            'color-d-green-30': 'hsla(184, 50%, 38%, 1)',
            'color-d-green-40': 'hsla(184, 55%, 30%, 1)',
            'color-d-alpha-green': 'hsla(184, 45%, 48%, 0.2)',
            # Blue → Deep Teal
            'color-d-blue-10':  'hsla(191, 50%, 58%, 1)',
            'color-d-blue-20':  'hsla(191, 48%, 48%, 1)',
            'color-d-blue-30':  'hsla(191, 52%, 38%, 1)',
            'color-d-blue-40':  'hsla(191, 55%, 30%, 1)',
            'color-d-alpha-blue': 'hsla(191, 50%, 48%, 0.2)',
            # Purple → Soft Rose (secondary: rgb(228,162,177))
            'color-d-purple-10': 'hsla(346, 52%, 78%, 1)',
            'color-d-purple-20': 'hsla(346, 48%, 68%, 1)',
            'color-d-purple-30': 'hsla(346, 42%, 58%, 1)',
            'color-d-purple-40': 'hsla(346, 38%, 48%, 1)',
            'color-d-alpha-purple': 'hsla(346, 50%, 68%, 0.2)',
            # Accent (inverted: amber in dark)
            'accent-h-dark': '42',
            'accent-s-dark': '85%',
            'accent-l-dark': '72%',
            # Special colors (dark)
            'color-gray-rgb-dark':   '160, 145, 152',
            'color-gray-dark':       'rgb(160, 145, 152)',
            'color-red-rgb-dark':    '227, 94, 164',
            'color-red-dark':        'rgb(200, 90, 145)',
            'color-orange-rgb-dark': '225, 155, 95',
            'color-orange-dark':     'rgb(200, 140, 80)',
            'color-yellow-rgb-dark': '251, 226, 167',
            'color-yellow-dark':     'rgb(235, 210, 155)',
            'color-green-rgb-dark':  '80, 175, 182',
            'color-green-dark':      'rgb(70, 165, 172)',
            'color-cyan-rgb-dark':   '100, 185, 195',
            'color-cyan-dark':       'rgb(85, 175, 185)',
            'color-blue-rgb-dark':   '90, 160, 185',
            'color-blue-dark':       'rgb(75, 148, 172)',
            'color-purple-rgb-dark': '228, 162, 177',
            'color-purple-dark':     'rgb(210, 148, 165)',
            'color-pink-rgb-dark':   '249, 168, 212',
            'color-pink-dark':       'rgb(230, 155, 195)',
        }
    },
    # ───── A: Slate Ocean ─────
    'slate-ocean': {
        'name': 'Slate Ocean',
        'light': {
            # Grayscale: cool slate-blue base (hue ~210-215)
            'color-l-gray-10':  'hsla(210, 30%, 98%, 1)',
            'color-l-gray-20':  'hsla(212, 28%, 96%, 1)',
            'color-l-gray-30':  'hsla(213, 25%, 92%, 1)',
            'color-l-gray-40':  'hsla(214, 22%, 89%, 1)',
            'color-l-gray-50':  'hsla(214, 20%, 86%, 1)',
            'color-l-gray-60':  'hsla(215, 18%, 79%, 1)',
            'color-l-gray-70':  'hsla(215, 15%, 65%, 1)',
            'color-l-gray-80':  'hsla(216, 13%, 55%, 1)',
            'color-l-gray-90':  'hsla(217, 14%, 45%, 1)',
            'color-l-gray-100': 'hsla(218, 18%, 36%, 1)',
            'color-l-gray-110': 'hsla(219, 20%, 32%, 1)',
            'color-l-gray-120': 'hsla(220, 22%, 26%, 1)',
            'color-l-gray-130': 'hsla(222, 30%, 20%, 1)',
            'color-l-gray-140': 'hsla(224, 40%, 14%, 1)',
            'color-l-alpha-gray': 'hsla(215, 15%, 65%, 0.15)',
            # Red → Rose
            'color-l-red-10':  'hsla(347, 55%, 62%, 1)',
            'color-l-red-20':  'hsla(347, 68%, 52%, 1)',
            'color-l-red-30':  'hsla(347, 62%, 44%, 1)',
            'color-l-red-40':  'hsla(347, 72%, 32%, 1)',
            'color-l-alpha-red': 'hsla(347, 80%, 60%, 0.18)',
            # Orange → Warm Amber
            'color-l-orange-10': 'hsla(28, 65%, 60%, 1)',
            'color-l-orange-20': 'hsla(25, 75%, 54%, 1)',
            'color-l-orange-30': 'hsla(22, 70%, 46%, 1)',
            'color-l-orange-40': 'hsla(20, 85%, 34%, 1)',
            'color-l-alpha-orange': 'hsla(25, 90%, 50%, 0.18)',
            # Yellow → Amber
            'color-l-yellow-10': 'hsla(38, 68%, 64%, 1)',
            'color-l-yellow-20': 'hsla(36, 80%, 52%, 1)',
            'color-l-yellow-30': 'hsla(34, 78%, 44%, 1)',
            'color-l-yellow-40': 'hsla(32, 90%, 34%, 1)',
            'color-l-alpha-yellow': 'hsla(36, 90%, 50%, 0.18)',
            # Green → Emerald
            'color-l-green-10': 'hsla(160, 35%, 60%, 1)',
            'color-l-green-20': 'hsla(162, 50%, 44%, 1)',
            'color-l-green-30': 'hsla(164, 55%, 36%, 1)',
            'color-l-green-40': 'hsla(166, 65%, 26%, 1)',
            'color-l-alpha-green': 'hsla(162, 60%, 42%, 0.18)',
            # Blue → Cyan/Teal
            'color-l-blue-10':  'hsla(192, 45%, 54%, 1)',
            'color-l-blue-20':  'hsla(195, 62%, 44%, 1)',
            'color-l-blue-30':  'hsla(198, 60%, 35%, 1)',
            'color-l-blue-40':  'hsla(200, 80%, 24%, 1)',
            'color-l-alpha-blue': 'hsla(195, 60%, 44%, 0.18)',
            # Purple → Indigo/Lavender
            'color-l-purple-10': 'hsla(250, 45%, 72%, 1)',
            'color-l-purple-20': 'hsla(248, 40%, 58%, 1)',
            'color-l-purple-30': 'hsla(246, 42%, 44%, 1)',
            'color-l-purple-40': 'hsla(244, 55%, 32%, 1)',
            'color-l-alpha-purple': 'hsla(248, 70%, 62%, 0.18)',
            # Accent
            'accent-h-light': '215',
            'accent-s-light': '20%',
            'accent-l-light': '45%',
            # Special colors
            'color-gray-rgb-light':   '165, 172, 182',
            'color-gray-light':       'hsla(215, 10%, 68%, 1)',
            'color-red-rgb-light':    '210, 80, 95',
            'color-red-light':        'hsla(347, 55%, 50%, 1)',
            'color-orange-rgb-light': '220, 130, 65',
            'color-orange-light':     'hsla(25, 65%, 50%, 1)',
            'color-yellow-rgb-light': '230, 185, 55',
            'color-yellow-light':     'hsla(36, 82%, 44%, 1)',
            'color-green-rgb-light':  '75, 178, 130',
            'color-green-light':      'hsla(162, 42%, 46%, 1)',
            'color-cyan-rgb-light':   '85, 175, 195',
            'color-cyan-light':       'hsla(195, 45%, 48%, 1)',
            'color-blue-rgb-light':   '80, 155, 195',
            'color-blue-light':       'hsla(200, 55%, 44%, 1)',
            'color-purple-rgb-light': '125, 110, 190',
            'color-purple-light':     'hsla(248, 38%, 58%, 1)',
            'color-pink-rgb-light':   '200, 105, 125',
            'color-pink-light':       'hsla(347, 42%, 58%, 1)',
        },
        'dark': {
            # Grayscale: deep midnight (hue ~220-230)
            'color-d-gray-10':  'hsla(210, 25%, 85%, 1)',
            'color-d-gray-20':  'hsla(212, 20%, 74%, 1)',
            'color-d-gray-30':  'hsla(214, 16%, 65%, 1)',
            'color-d-gray-40':  'hsla(216, 14%, 52%, 1)',
            'color-d-gray-50':  'hsla(218, 14%, 42%, 1)',
            'color-d-gray-60':  'hsla(220, 16%, 28%, 1)',
            'color-d-gray-70':  'hsla(222, 18%, 22%, 1)',
            'color-d-gray-80':  'hsla(224, 20%, 17%, 1)',
            'color-d-gray-90':  'hsla(226, 22%, 15%, 1)',
            'color-d-gray-100': 'hsla(228, 24%, 13%, 1)',
            'color-d-gray-110': 'hsla(229, 26%, 12%, 1)',
            'color-d-gray-120': 'hsla(230, 28%, 11%, 1)',
            'color-d-gray-130': 'hsla(232, 32%, 9%, 1)',
            'color-d-gray-140': 'hsla(234, 38%, 7%, 1)',
            'color-d-alpha-gray': 'hsla(218, 14%, 42%, 0.2)',
            # Red → Soft Rose
            'color-d-red-10':  'hsla(350, 85%, 72%, 1)',
            'color-d-red-20':  'hsla(348, 82%, 66%, 1)',
            'color-d-red-30':  'hsla(347, 78%, 60%, 1)',
            'color-d-red-40':  'hsla(345, 65%, 50%, 1)',
            'color-d-alpha-red': 'hsla(347, 75%, 60%, 0.2)',
            # Orange
            'color-d-orange-10': 'hsla(28, 80%, 58%, 1)',
            'color-d-orange-20': 'hsla(25, 78%, 50%, 1)',
            'color-d-orange-30': 'hsla(22, 75%, 46%, 1)',
            'color-d-orange-40': 'hsla(20, 72%, 40%, 1)',
            'color-d-alpha-orange': 'hsla(25, 85%, 50%, 0.2)',
            # Yellow → Amber
            'color-d-yellow-10': 'hsla(40, 70%, 62%, 1)',
            'color-d-yellow-20': 'hsla(38, 78%, 52%, 1)',
            'color-d-yellow-30': 'hsla(36, 76%, 48%, 1)',
            'color-d-yellow-40': 'hsla(34, 72%, 42%, 1)',
            'color-d-alpha-yellow': 'hsla(38, 85%, 50%, 0.2)',
            # Green → Emerald
            'color-d-green-10': 'hsla(162, 50%, 54%, 1)',
            'color-d-green-20': 'hsla(164, 55%, 42%, 1)',
            'color-d-green-30': 'hsla(166, 65%, 30%, 1)',
            'color-d-green-40': 'hsla(168, 62%, 26%, 1)',
            'color-d-alpha-green': 'hsla(164, 55%, 40%, 0.2)',
            # Blue → Cyan
            'color-d-blue-10':  'hsla(192, 55%, 62%, 1)',
            'color-d-blue-20':  'hsla(194, 58%, 55%, 1)',
            'color-d-blue-30':  'hsla(197, 50%, 48%, 1)',
            'color-d-blue-40':  'hsla(200, 48%, 40%, 1)',
            'color-d-alpha-blue': 'hsla(194, 55%, 50%, 0.2)',
            # Purple → Lavender
            'color-d-purple-10': 'hsla(250, 52%, 70%, 1)',
            'color-d-purple-20': 'hsla(248, 48%, 58%, 1)',
            'color-d-purple-30': 'hsla(246, 45%, 52%, 1)',
            'color-d-purple-40': 'hsla(244, 42%, 46%, 1)',
            'color-d-alpha-purple': 'hsla(248, 70%, 65%, 0.2)',
            # Accent
            'accent-h-dark': '215',
            'accent-s-dark': '25%',
            'accent-l-dark': '22%',
            # Special colors (dark)
            'color-gray-rgb-dark':   '155, 162, 172',
            'color-gray-dark':       'rgb(155, 162, 172)',
            'color-red-rgb-dark':    '215, 95, 105',
            'color-red-dark':        'rgb(190, 80, 85)',
            'color-orange-rgb-dark': '225, 155, 85',
            'color-orange-dark':     'rgb(195, 125, 55)',
            'color-yellow-rgb-dark': '235, 195, 75',
            'color-yellow-dark':     'rgb(215, 170, 60)',
            'color-green-rgb-dark':  '85, 190, 120',
            'color-green-dark':      'rgb(70, 185, 100)',
            'color-cyan-rgb-dark':   '80, 175, 185',
            'color-cyan-dark':       'rgb(65, 168, 178)',
            'color-blue-rgb-dark':   '85, 150, 190',
            'color-blue-dark':       'rgb(60, 132, 172)',
            'color-purple-rgb-dark': '130, 115, 190',
            'color-purple-dark':     'rgb(110, 95, 185)',
            'color-pink-rgb-dark':   '210, 110, 130',
            'color-pink-dark':       'rgb(175, 95, 100)',
        }
    },
}


DARK_SPLIT = '/*\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n            Dark Palette'

def split_light_dark(content):
    """Safely split content into light and dark sections using the header comment."""
    parts = content.split(DARK_SPLIT, 1)
    return parts[0], DARK_SPLIT + parts[1] if len(parts) > 1 else ''

def apply_palette(original_content: str, palette: dict) -> str:
    """Replace color primitive HSL values in the palette file."""
    content = original_content
    
    # Replace palette name in header
    content = content.replace('in Classic Original', f'in {palette["name"]}')
    
    light = palette['light']
    dark = palette['dark']
    
    # Replace light grayscale
    for key in [f'color-l-gray-{n}' for n in [10,20,30,40,50,60,70,80,90,100,110,120,130,140]]:
        if key in light:
            # Match: --color-l-gray-XX: hsla(...);
            pattern = rf'(--{key}:\s*)hsla\([^)]+\)'
            content = re.sub(pattern, rf'\g<1>{light[key]}', content)
    
    # Replace light alpha gray
    if 'color-l-alpha-gray' in light:
        pattern = r'(--color-l-alpha-gray:\s*)hsla\([^)]+\)'
        content = re.sub(pattern, rf'\g<1>{light["color-l-alpha-gray"]}', content)
    
    # Replace light semantic colors
    for color in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
        for shade in [10, 20, 30, 40]:
            key = f'color-l-{color}-{shade}'
            if key in light:
                pattern = rf'(--{key}:\s*)hsla\([^)]+\)'
                content = re.sub(pattern, rf'\g<1>{light[key]}', content)
        alpha_key = f'color-l-alpha-{color}'
        if alpha_key in light:
            pattern = rf'(--{alpha_key}:\s*)hsla\([^)]+\)'
            content = re.sub(pattern, rf'\g<1>{light[alpha_key]}', content)
    
    # Replace light accent (in .theme-light only - first occurrence)
    if 'accent-h-light' in light:
        # Split on the dark palette section header comment, not the CSS class
        split_marker = '/*───────────────────────────────────\n            Dark Palette'
        parts = content.split(split_marker, 1)
        light_section = parts[0]
        dark_section = split_marker + parts[1] if len(parts) > 1 else ''
        
        light_section = re.sub(r'(--accent-h:\s*)\d+', rf'\g<1>{light["accent-h-light"]}', light_section)
        light_section = re.sub(r'(--accent-s:\s*)\d+%', rf'\g<1>{light["accent-s-light"]}', light_section)
        light_section = re.sub(r'(--accent-l:\s*)\d+%', rf'\g<1>{light["accent-l-light"]}', light_section)
        
        content = light_section + dark_section
    
    # Replace light special colors
    special_map = {
        'color-gray-rgb-light':   ('--color-gray-rgb:', light.get('color-gray-rgb-light', '')),
        'color-gray-light':       ('--color-gray:', light.get('color-gray-light', '')),
        'color-red-rgb-light':    ('--color-red-rgb:', light.get('color-red-rgb-light', '')),
        'color-red-light':        ('--color-red:', light.get('color-red-light', '')),
        'color-orange-rgb-light': ('--color-orange-rgb:', light.get('color-orange-rgb-light', '')),
        'color-orange-light':     ('--color-orange:', light.get('color-orange-light', '')),
        'color-yellow-rgb-light': ('--color-yellow-rgb:', light.get('color-yellow-rgb-light', '')),
        'color-yellow-light':     ('--color-yellow:', light.get('color-yellow-light', '')),
        'color-green-rgb-light':  ('--color-green-rgb:', light.get('color-green-rgb-light', '')),
        'color-green-light':      ('--color-green:', light.get('color-green-light', '')),
        'color-cyan-rgb-light':   ('--color-cyan-rgb:', light.get('color-cyan-rgb-light', '')),
        'color-cyan-light':       ('--color-cyan:', light.get('color-cyan-light', '')),
        'color-blue-rgb-light':   ('--color-blue-rgb:', light.get('color-blue-rgb-light', '')),
        'color-blue-light':       ('--color-blue:', light.get('color-blue-light', '')),
        'color-purple-rgb-light': ('--color-purple-rgb:', light.get('color-purple-rgb-light', '')),
        'color-purple-light':     ('--color-purple:', light.get('color-purple-light', '')),
        'color-pink-rgb-light':   ('--color-pink-rgb:', light.get('color-pink-rgb-light', '')),
        'color-pink-light':       ('--color-pink:', light.get('color-pink-light', '')),
    }
    
    # Apply special color replacements in light section only
    light_section, dark_section = split_light_dark(content)
    
    for key, (var_prefix, value) in special_map.items():
        if value:
            # Match the variable and its value up to semicolon
            pattern = rf'({re.escape(var_prefix)}\s*)[^;]+(?=;)'
            light_section = re.sub(pattern, rf'\g<1>{value}', light_section, count=1)
    
    content = light_section + dark_section
    
    # ── DARK MODE ──
    
    # Replace dark grayscale
    for key in [f'color-d-gray-{n}' for n in [10,20,30,40,50,60,70,80,90,100,110,120,130,140]]:
        if key in dark:
            pattern = rf'(--{key}:\s*)hsla\([^)]+\)'
            content = re.sub(pattern, rf'\g<1>{dark[key]}', content)
    
    if 'color-d-alpha-gray' in dark:
        pattern = r'(--color-d-alpha-gray:\s*)hsla\([^)]+\)'
        content = re.sub(pattern, rf'\g<1>{dark["color-d-alpha-gray"]}', content)
    
    # Replace dark semantic colors
    for color in ['red', 'orange', 'yellow', 'green', 'blue', 'purple']:
        for shade in [10, 20, 30, 40]:
            key = f'color-d-{color}-{shade}'
            if key in dark:
                pattern = rf'(--{key}:\s*)hsla\([^)]+\)'
                content = re.sub(pattern, rf'\g<1>{dark[key]}', content)
        alpha_key = f'color-d-alpha-{color}'
        if alpha_key in dark:
            pattern = rf'(--{alpha_key}:\s*)hsla\([^)]+\)'
            content = re.sub(pattern, rf'\g<1>{dark[alpha_key]}', content)
    
    # Replace dark accent
    if 'accent-h-dark' in dark:
        # Only replace in dark section
        light_section, dark_section = split_light_dark(content)
        
        dark_section = re.sub(r'(--accent-h:\s*)\d+', rf'\g<1>{dark["accent-h-dark"]}', dark_section)
        dark_section = re.sub(r'(--accent-s:\s*)\d+%', rf'\g<1>{dark["accent-s-dark"]}', dark_section)
        dark_section = re.sub(r'(--accent-l:\s*)\d+%', rf'\g<1>{dark["accent-l-dark"]}', dark_section)
        
        content = light_section + dark_section
    
    # Replace dark special colors
    dark_special_map = {
        'color-gray-rgb-dark':   '--color-gray-rgb:',
        'color-red-rgb-dark':    '--color-red-rgb:',
        'color-orange-rgb-dark': '--color-orange-rgb:',
        'color-yellow-rgb-dark': '--color-yellow-rgb:',
        'color-green-rgb-dark':  '--color-green-rgb:',
        'color-cyan-rgb-dark':   '--color-cyan-rgb:',
        'color-blue-rgb-dark':   '--color-blue-rgb:',
        'color-purple-rgb-dark': '--color-purple-rgb:',
        'color-pink-rgb-dark':   '--color-pink-rgb:',
        'color-gray-dark':       '--color-gray:',
        'color-red-dark':        '--color-red:',
        'color-orange-dark':     '--color-orange:',
        'color-yellow-dark':     '--color-yellow:',
        'color-green-dark':      '--color-green:',
        'color-cyan-dark':       '--color-cyan:',
        'color-blue-dark':       '--color-blue:',
        'color-purple-dark':     '--color-purple:',
        'color-pink-dark':       '--color-pink:',
    }
    
    light_section, dark_section = split_light_dark(content)
    
    for key, var_prefix in dark_special_map.items():
        if key in dark:
            pattern = rf'({re.escape(var_prefix)}\s*)[^;]+(?=;)'
            dark_section = re.sub(pattern, rf'\g<1>{dark[key]}', dark_section, count=1)
    
    content = light_section + dark_section
    
    return content


def main():
    print("🎨 Primary Theme Palette Generator")
    print("=" * 40)
    
    # Read original
    with open(ORIGINAL, 'r') as f:
        original = f.read()
    
    for slug, palette in PALETTES.items():
        output_file = os.path.join(PALETTES_DIR, f'_{slug}.scss')
        print(f"\n🖌️  Generating: {palette['name']} → _{slug}.scss")
        
        result = apply_palette(original, palette)
        
        with open(output_file, 'w') as f:
            f.write(result)
        
        print(f"   ✅ Written to {output_file}")
    
    print(f"\n🎉 Done! Generated {len(PALETTES)} palette(s).")
    print("\nTo use a palette, update src/scss/index.scss:")
    print("  @use '10_foundations/palettes/<palette-name>';")
    print("\nThen build with: npx grunt")


if __name__ == '__main__':
    main()
