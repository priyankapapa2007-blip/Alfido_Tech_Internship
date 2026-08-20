from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path('d:/Alfido_tech')
OUTPUTS = [
    BASE / 'samples' / 'output.txt',
    BASE / 'tests' / 'test_results.txt',
]
SCREENSHOT_DIR = BASE / 'screenshots'
SCREENSHOT_DIR.mkdir(exist_ok=True)

font = ImageFont.load_default()

dummy = Image.new('RGB', (1, 1), 'white')
draw_dummy = ImageDraw.Draw(dummy)

for path in OUTPUTS:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines() or ['']
    max_width = max(draw_dummy.textbbox((0, 0), line, font=font)[2] for line in lines) + 20
    line_height = draw_dummy.textbbox((0, 0), 'Ay', font=font)[3] + 4
    height = line_height * len(lines) + 20
    img = Image.new('RGB', (max_width, height), 'white')
    draw = ImageDraw.Draw(img)
    y = 10
    for line in lines:
        draw.text((10, y), line, fill='black', font=font)
        y += line_height
    out_path = SCREENSHOT_DIR / f'{path.stem}.png'
    img.save(out_path)
    print(f'Saved {out_path}')
