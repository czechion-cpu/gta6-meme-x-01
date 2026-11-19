#!/usr/bin/env python3
"""Compose meme.png for the make.fun gta6-meme-x-01 bounty.

Takes the AI-generated Vice City street scene (dev/base-scene.png), warps the
caption onto the blank billboard in perspective, stands the make.fun ghost
mark on the street next to the couple, and adds a punchline bar at the bottom.

Run from the repo root:  python3 dev/compose_meme.py
Writes meme.png (1024x1024) at the repo root.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

BASE = os.path.join(HERE, "base-scene.png")
GHOST = os.path.join(ROOT, "assets", "makefun-mark-1024.png")
OUT = os.path.join(ROOT, "meme.png")

SIZE = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Billboard corners in the 1600x1600 base scene (measured from the render):
# top-left, top-right, bottom-right, bottom-left.
BILLBOARD_1600 = [(705, 235), (1395, 55), (1395, 465), (705, 595)]

BILLBOARD_LINES = ["WAITED 13 YEARS", "FOR GTA 6."]
BAR_LINES = ["MY AI AGENT MADE $500", "ON MAKE.FUN WHILE I WAITED."]


def solve_linear(a, b):
    """Solve a x = b by Gaussian elimination (small dense system)."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for col in range(n):
        piv = max(range(col, n), key=lambda r: abs(m[r][col]))
        m[col], m[piv] = m[piv], m[col]
        pv = m[col][col]
        m[col] = [v / pv for v in m[col]]
        for r in range(n):
            if r != col and m[r][col]:
                f = m[r][col]
                m[r] = [v - f * w for v, w in zip(m[r], m[col])]
    return [m[i][n] for i in range(n)]


def perspective_coeffs(target_quad, source_size):
    """Coefficients mapping output pixels onto the source rectangle.

    target_quad: 4 (x, y) points in the output image, in TL, TR, BR, BL order.
    source_size: (w, h) of the rectangular source image.
    """
    w, h = source_size
    source = [(0, 0), (w, 0), (w, h), (0, h)]
    rows, rhs = [], []
    for (tx, ty), (sx, sy) in zip(target_quad, source):
        rows.append([tx, ty, 1, 0, 0, 0, -sx * tx, -sx * ty])
        rhs.append(sx)
        rows.append([0, 0, 0, tx, ty, 1, -sy * tx, -sy * ty])
        rhs.append(sy)
    return solve_linear(rows, rhs)


def inset_quad(quad, frac):
    """Shrink a quad toward its centroid by frac (0..1)."""
    cx = sum(p[0] for p in quad) / 4
    cy = sum(p[1] for p in quad) / 4
    return [(cx + (x - cx) * (1 - frac), cy + (y - cy) * (1 - frac))
            for x, y in quad]


def fit_font(draw, lines, max_w, start_size):
    """Largest bold size at which the widest line fits max_w."""
    size = start_size
    while size > 10:
        font = ImageFont.truetype(BOLD, size)
        if max(draw.textlength(t, font=font) for t in lines) <= max_w:
            return font
        size -= 2
    return ImageFont.truetype(BOLD, 10)


def main():
    base = Image.open(BASE).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS)

    # --- 1. Caption warped onto the billboard ------------------------------
    scale = SIZE / 1600.0
    quad = [(x * scale, y * scale) for x, y in BILLBOARD_1600]
    quad = inset_quad(quad, 0.18)

    layer = Image.new("RGBA", (700, 320), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    font = fit_font(ld, BILLBOARD_LINES, 520, 88)
    lh = int(font.size * 1.12)
    total = lh * len(BILLBOARD_LINES)
    y = (320 - total) // 2
    for line in BILLBOARD_LINES:
        ld.text((350, y), line, font=font, fill=(20, 20, 20, 255),
                anchor="ma")
        y += lh
    warped = layer.transform((SIZE, SIZE), Image.PERSPECTIVE,
                             perspective_coeffs(quad, layer.size),
                             Image.BICUBIC)
    base = Image.alpha_composite(base.convert("RGBA"), warped)

    # --- 2. The make.fun ghost standing on the street ----------------------
    ghost = Image.open(GHOST).convert("RGBA")
    ghost = ghost.resize((190, 190), Image.LANCZOS)
    gx, gy = 775, 700
    shadow = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.ellipse([gx + 25, gy + 172, gx + 165, gy + 192], fill=(0, 0, 0, 130))
    shadow = shadow.filter(ImageFilter.GaussianBlur(6))
    base = Image.alpha_composite(base, shadow)
    base.alpha_composite(ghost, (gx, gy))

    # --- 3. Punchline bar along the bottom ---------------------------------
    bar = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bar)
    bd.rectangle([0, 906, SIZE, SIZE], fill=(0, 0, 0, 235))
    bd.rectangle([0, 906, SIZE, 910], fill=(214, 0, 140, 255))  # magenta rule
    font = fit_font(bd, BAR_LINES, 940, 52)
    lh = int(font.size * 1.12)
    total = lh * len(BAR_LINES)
    y = 906 + (SIZE - 906 - total) // 2
    for line in BAR_LINES:
        bd.text((SIZE // 2, y), line, font=font, fill=(255, 255, 255, 255),
                anchor="ma")
        y += lh
    base = Image.alpha_composite(base, bar)

    base.convert("RGB").save(OUT, "PNG")
    print(f"wrote {OUT} ({SIZE}x{SIZE})")


if __name__ == "__main__":
    main()
