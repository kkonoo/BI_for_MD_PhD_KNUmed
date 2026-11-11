# W9 §2 항아리 문제: 배경 20,000개(빨강 = 경로 1,000개)에서 500개(DEG)를 뽑았더니 빨강 100 · 흰색 400
# 원본: assets/img/part3/W9_urn.png → 다시 그림. 숫자는 본문 2×2 표와 같음. 공 개수는 비율만 나타냄(설명용).
from medfig import *

L = {
    "ko": dict(urn="항아리 = 배경 유전자 20,000개", red="빨강: 염증 경로 유전자 1,000개",
               white="흰색: 경로에 없는 유전자 19,000개",
               draw="500개를 뽑음\n= 내 DEG", got="빨강 100 · 흰색 400",
               q="빨강이 우연보다\n많이 나왔는가?"),
    "en": dict(urn="Urn = 20,000 background genes", red="red: 1,000 Inflammation pathway genes",
               white="white: 19,000 genes not in the pathway",
               draw="draw 500\n= my DEGs", got="100 red · 400 white",
               q="More red than\nchance predicts?"),
}
RED = CAT[0]


def balls(ax, x0, y0, cols, rows, reds, r=0.085, gap=0.22):
    k = 0
    for j in range(rows):
        for i in range(cols):
            c = RED if k in reds else "white"
            ax.add_patch(mp.Circle((x0 + i * gap + (j % 2) * gap / 2, y0 + j * gap * 0.9), r,
                                   fc=c, ec=RED if k in reds else "#9AA1AB", lw=1.1, zorder=4))
            k += 1


def draw(t):
    fig, ax = new(6.9, 2.8)
    # 항아리: 40개 중 2개 빨강 (5%)
    box(ax, 0.1, 0.92, 2.4, 1.36, fc=FAINT, ec=LINE, r=0.12)
    balls(ax, 0.38, 1.2, 8, 5, reds={11, 28})
    label(ax, 1.3, 2.5, t["urn"], fs=12, w="semibold")
    # 범례
    ax.add_patch(mp.Circle((0.24, 0.62), 0.07, fc=RED, ec=RED, zorder=4))
    label(ax, 0.38, 0.62, t["red"], ha="left")
    ax.add_patch(mp.Circle((0.24, 0.3), 0.07, fc="white", ec="#9AA1AB", lw=1.1, zorder=4))
    label(ax, 0.38, 0.3, t["white"], ha="left")
    # 뽑기
    arrow(ax, 2.65, 1.6, 3.75, 1.6, color="#9AA1AB", lw=2, ms=16)
    label(ax, 3.2, 2.02, t["draw"], fs=12, w="semibold", linespacing=1.3)
    # 뽑은 500개: 20개 중 4개 빨강 (20%)
    box(ax, 3.9, 1.0, 1.25, 1.2, fc=FAINT, ec=LINE, r=0.12)
    balls(ax, 4.1, 1.3, 5, 4, reds={0, 6, 12, 18})
    label(ax, 4.525, 0.75, t["got"], fs=12, w="bold", c=shade(RED, 0.15))
    label(ax, 5.35, 1.6, t["q"], fs=11.5, c=TEXT2, ha="left", linespacing=1.35)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W9_urn{suffix}.png")
