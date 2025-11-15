import os
from fontTools.ttLib import TTFont

# Font Dictionary
fonts = {
    "Default": "DS-DIGI.TTF",
    "Squares": "square_sans_serif_7.ttf",
    "Comic": "Sophiecomic-Regular.ttf",
    "Round": "Bartino-Regular.ttf",
    "Sunshine": "A little sunshine.ttf"
}

# Base Path
base_path = os.path.dirname(__file__)

print("=" * 55)
print("FONT FAMILY NAME CHECKER")
print("=" * 55)

for nickname, filename in fonts.items():
    font_path = os.path.join(base_path, "assets", "fonts", filename)
    if os.path.exists(font_path):
        try:
            font = TTFont(font_path)
            family_name = font['name'].getDebugName(1)
            print(f'\n✅ {nickname}:')
            print(f'    Filename: {filename}')
            print(f'    Family Name: "{family_name}"')
        except Exception as e:
            print(f'\n❌ {nickname}: Error reading font - {e}')
    else:
        print(f'\n❌ {nickname}: File not found at {font_path}')
print("=" * 55)