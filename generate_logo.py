import random
from html.parser import HTMLParser
from pathlib import Path

# Generate a simple SVG logo for AI Handpicked
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 100" width="400" height="100">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#667eea"/>
      <stop offset="100%" style="stop-color:#764ba2"/>
    </linearGradient>
    <linearGradient id="ai" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00d4ff"/>
      <stop offset="100%" style="stop-color:#7c3aed"/>
    </linearGradient>
    <linearGradient id="text" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ffffff"/>
      <stop offset="100%" style="stop-color:#e0e7ff"/>
    </linearGradient>
  </defs>

  <!-- Background rounded rect -->
  <rect width="400" height="100" rx="20" fill="url(#bg)"/>

  <!-- Hand/thumb up icon -->
  <g transform="translate(20, 15)">
    <!-- Thumb up shape -->
    <rect x="22" y="30" width="16" height="28" rx="8" fill="url(#ai)"/>
    <rect x="38" y="40" width="8" height="18" rx="4" fill="url(#ai)"/>
    <rect x="10" y="40" width="8" height="18" rx="4" fill="url(#ai)"/>
    <rect x="0" y="40" width="8" height="18" rx="4" fill="url(#ai)"/>
    <!-- Palm -->
    <rect x="8" y="48" width="34" height="22" rx="8" fill="url(#ai)"/>
    <!-- Sparkle star -->
    <text x="38" y="18" font-size="16" fill="#00d4ff">✦</text>
  </g>

  <!-- Text: AI -->
  <text x="85" y="42" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="800" fill="url(#ai)">AI</text>

  <!-- Divider line -->
  <rect x="115" y="22" width="2" height="56" rx="1" fill="rgba(255,255,255,0.25)"/>

  <!-- Text: Handpicked -->
  <text x="130" y="42" font-family="'Segoe UI', Arial, sans-serif" font-size="28" font-weight="700" fill="url(#text)">Handpicked</text>

  <!-- Subtitle -->
  <text x="130" y="68" font-family="'Segoe UI', Arial, sans-serif" font-size="13" fill="rgba(255,255,255,0.6)">Curated AI Tools Directory</text>

  <!-- Decorative dots -->
  <circle cx="370" cy="20" r="4" fill="rgba(255,255,255,0.2)"/>
  <circle cx="385" cy="35" r="3" fill="rgba(255,255,255,0.15)"/>
  <circle cx="360" cy="80" r="5" fill="rgba(255,255,255,0.1)"/>
</svg>"""

# Save SVG
output_path = Path(r"C:\Users\sharkcheung\.qclaw\workspace\aihandpicked\static\images\logo.svg")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(svg_content, encoding='utf-8')
print(f"Saved: {output_path}")

# Also save as PNG using reportlab (if available) or cairosvg
try:
    import cairosvg
    png_path = output_path.with_suffix('.png')
    cairosvg.svg2png(bytestring=svg_content.encode('utf-8'), write_to=str(png_path), output_width=800, output_height=200)
    print(f"Saved PNG: {png_path}")
except ImportError:
    print("cairosvg not available, SVG only")
    # Try with pillow + lxml alternative approach
    try:
        from PIL import Image, ImageDraw, ImageFont
        # Create a simple PNG fallback using PIL
        # We'll create a gradient background with text
        from PIL import Image
        img = Image.new('RGBA', (400, 100), (102, 126, 234, 255))
        draw = ImageDraw.Draw(img)
        # Save as PNG
        png_path = output_path.with_suffix('.png')
        img.save(png_path)
        print(f"Saved PNG: {png_path}")
    except Exception as e2:
        print(f"PIL fallback failed: {e2}")