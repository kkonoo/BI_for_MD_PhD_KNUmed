# W5 §2 STAR: splice junction을 걸친 리드를 두 조각(seed)으로 나눠 각 엑손에 붙이고 이어 붙임
# 원본: assets/img/part2/W6_star.png (외부 그림, 영어) → 다시 그림. 좁은 그림(~3.4 in).
from medfig import *

L = {
    "ko": dict(read="리드", exon="엑손", intron="인트론", out="이어 붙인 리드", skip="인트론은 건너뜀"),
    "en": dict(read="read", exon="exon", intron="intron", out="stitched read", skip="intron skipped"),
}
S1, S2 = CAT[0], CAT[1]              # seed 1 / seed 2 (W5_STAR의 MMP 1 / MMP 2와 같은 색)
EXON = mix(TEXT2, 0.25)
H = 0.3


def draw(t):
    fig, ax = new(3.6, 3.3)
    # 리드: seed 1 | seed 2
    ry, a, m, b = 2.75, 0.6, 1.35, 2.1
    box(ax, a, ry, m - a, H, fc=S1, ec="none", r=0.03)
    box(ax, m, ry, b - m, H, fc=S2, ec="none", r=0.03)
    label(ax, (a + m) / 2, ry + H / 2, "seed 1", fs=11, w="semibold", c="white")
    label(ax, (m + b) / 2, ry + H / 2, "seed 2", fs=11, w="semibold", c="white")
    label(ax, b + 0.12, ry + H / 2, t["read"], fs=11, c=TEXT2, ha="left")
    # 게놈: 엑손 – 인트론 – 엑손
    gy = 1.55
    e1, e2 = (0.15, 1.35), (2.6, 3.45)
    ax.plot([0.0, 3.6], [gy + H / 2] * 2, color="#9AA1AB", lw=1.4, zorder=1)
    for x0, x1 in (e1, e2):
        box(ax, x0, gy, x1 - x0, H, fc=EXON, ec="none", r=0.03)
        label(ax, (x0 + x1) / 2, gy - 0.2, t["exon"], fs=11, c=TEXT2)
    label(ax, (e1[1] + e2[0]) / 2, gy - 0.2, t["intron"], fs=11, c=TEXT2)
    # 어디에 붙는지: 점선
    d = dict(color=TEXT2, lw=1, ls=(0, (3, 2)), zorder=1)
    ax.plot([a, a], [ry, gy + H], **d); ax.plot([m, m], [ry, gy + H], **d)
    ax.plot([m, e2[0]], [ry, gy + H], **d); ax.plot([b, e2[0] + (b - m)], [ry, gy + H], **d)
    # 이어 붙인 리드
    arrow(ax, 1.97, gy - 0.38, 1.97, 0.78, lw=1.4, ms=10)
    oy = 0.35
    box(ax, a, oy, m - a, H, fc=S1, ec="none", r=0.03)
    box(ax, e2[0], oy, b - m, H, fc=S2, ec="none", r=0.03)
    ax.plot([m, e2[0]], [oy + H / 2] * 2, color=TEXT2, lw=1.2, ls=(0, (3, 2)))
    label(ax, (a + e2[0] + b - m) / 2, oy - 0.2, f"{t['out']} · {t['skip']}", fs=11, w="semibold")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W6_star{suffix}.png")
