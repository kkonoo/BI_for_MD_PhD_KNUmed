# W2 §2 행렬 인덱싱: m[2, ] 행 / m[ , 1] 열 / m[2, 3] 원소
# 원본: assets/img/part1/W2_matrix.png (외부 그림, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(d=["행 하나 선택", "열 하나 선택", "원소 하나 선택"]),
    "en": dict(d=["select a row", "select a column", "select an element"]),
}
ON_, OFF = CAT[0], mix(TEXT2, 0.18)
MONO = "DejaVu Sans Mono"
CASES = [("m[2, ]", lambda r, c: r == 2), ("m[ , 1]", lambda r, c: c == 1),
         ("m[2, 3]", lambda r, c: r == 2 and c == 3)]


def draw(t):
    fig, ax = new(4.4, 2.75)
    s, g = 0.2, 0.03
    for k, ((code, pick), d) in enumerate(zip(CASES, t["d"])):
        y0 = 2.6 - k * 0.92
        for r in range(1, 4):
            for c in range(1, 4):
                box(ax, 0.1 + (c - 1) * (s + g), y0 - r * (s + g), s, s, fc=ON_ if pick(r, c) else OFF,
                    ec="none", r=0.02)
        yc = y0 - 2 * (s + g) + s / 2
        ax.text(0.95, yc, code, fontsize=14, fontfamily=MONO, color=TEXT, va="center", ha="left")
        label(ax, 2.2, yc, d, fs=12, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/W2_matrix{suffix}.png")
