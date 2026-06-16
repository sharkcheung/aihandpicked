from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 400, 100
img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

def draw_rounded_gradient(draw, xy, radius, color_top, color_bot):
    x0, y0, x1, y1 = xy
    for y in range(y0, y1):
        ratio = (y - y0) / (y1 - y0)
        r = int(color_top[0] + (color_bot[0] - color_top[0]) * ratio)
        g = int(color_top[1] + (color_bot[1] - color_top[1]) * ratio)
        b = int(color_top[2] + (color_bot[2] - color_top[2]) * ratio)
        a = int(color_top[3] + (color_bot[3] - color_top[3]) * ratio)
        draw.line([(x0, y), (x1, y)], fill=(r, g, b, a))

draw_rounded_gradient(draw, (0, 0, W, H), 20,
    (102, 126, 234, 255), (118, 75, 162, 255))

# Thumb icon
draw.rounded_rectangle((42, 45, 58, 73), 8, fill=(0, 180, 255, 255))
draw.rounded_rectangle((58, 55, 66, 73), 4, fill=(0, 180, 255, 255))
draw.rounded_rectangle((30, 55, 38, 73), 4, fill=(0, 180, 255, 255))
draw.rounded_rectangle((20, 55, 28, 73), 4, fill=(0, 180, 255, 255))
draw.rounded_rectangle((28, 63, 62, 85), 8, fill=(0, 180, 255, 255))

# Divider
draw.rectangle((115, 22, 117, 78), fill=(255, 255, 255, 64))

# Try Segoe fonts
font_main = None
for name in ["seguiemj.ttf", "seguisb.ttf", "segoeui.ttf"]:
    try:
        font_main = ImageFont.truetype(f"C:\\Windows\\Fonts\\{name}", 28)
        break
    except:
        pass
if font_main is None:
    font_main = ImageFont.load_default()

font_sub = None
for name in ["seguisb.ttf", "segoeui.ttf"]:
    try:
        font_sub = ImageFont.truetype(f"C:\\Windows\\Fonts\\{name}", 13)
        break
    except:
        pass
if font_sub is None:
    font_sub = ImageFont.load_default()

draw.text((85, 18), "AI", font=font_main, fill=(0, 180, 255, 255))
draw.text((130, 18), "Handpicked", font=font_main, fill=(255, 255, 255, 255))
draw.text((130, 52), "Curated AI Tools Directory", font=font_sub, fill=(200, 200, 255, 200))

# Dots
for cx, cy, r, alpha in [(365, 20, 4, 50), (382, 35, 3, 38), (358, 80, 5, 25)]:
    draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill=(255, 255, 255, alpha))

out_png = Path(r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked\static\images\logo.png")
out_png.parent.mkdir(parents=True, exist_ok=True)
img.save(out_png, 'PNG')
print(f"OK: {out_png}")

# Square version for affiliate
img2 = Image.new('RGBA', (200, 200), (102, 126, 234, 255))
# Scale and center
img_scaled = img.resize((200, 50), Image.LANCZOS)
img2.paste(img_scaled, (0, 75), mask=img_scaled)
out_sq = Path(r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked\static\images\logo_square.png")
img2.save(out_sq, 'PNG')
print(f"OK: {out_sq}")