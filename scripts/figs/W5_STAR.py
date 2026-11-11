# W5 §3 정렬 기반 정량(STAR): MMP 1 → MMP 2 로 리드를 두 엑손에 나눠 붙임
# 원본: assets/img/part2/W5_STAR.gif (외부 그림, 영어) → W5_STAR.png 로 다시 그림
from medfig import *

L = {
    "ko": dict(read="RNA-seq 리드", exon="게놈의 엑손", sj="splice junction",
               n1="① MMP 1: 리드 앞부분에서 참조에 그대로 맞는 가장 긴 조각",
               n2="② MMP 2: 남은 부분을 다시 찾아 다음 엑손에 붙임"),
    "en": dict(read="RNA-seq read", exon="exons in the genome", sj="splice junction",
               n1="① MMP 1: longest piece from the read's start that matches the reference",
               n2="② MMP 2: search again with the rest; it lands on the next exon"),
}
M1, M2 = CAT[0], CAT[1]              # W6_star의 seed 1 / seed 2와 같은 색
EXON = mix(TEXT2, 0.25)
H = 0.34


def draw(t):
    fig, ax = new(6.6, 3.0)
    ry, a, m, b = 2.05, 1.75, 3.3, 4.85
    e1, e2 = (0.45, 3.3), (4.25, 6.3)
    # MMP 구간 표시
    for x0, x1, s, c in [(a, m, "MMP 1", M1), (m, b, "MMP 2", M2)]:
        arrow(ax, x0 + 0.03, ry + H + 0.2, x1 - 0.06, ry + H + 0.2, color=c, lw=1.4, ms=10)
        label(ax, (x0 + x1) / 2, ry + H + 0.42, s, fs=12, w="bold", c=c)
    box(ax, a, ry, m - a, H, fc=mix(M1, 0.25), ec=M1, lw=1.2, r=0.03)
    box(ax, m, ry, b - m, H, fc=mix(M2, 0.25), ec=M2, lw=1.2, r=0.03)
    label(ax, b + 0.15, ry + H / 2, t["read"], fs=11, c=TEXT2, ha="left")
    # 게놈
    gy = 1.0
    ax.plot([0.0, 6.6], [gy + H / 2] * 2, color="#9AA1AB", lw=1.4, zorder=1)
    for x0, x1 in (e1, e2):
        box(ax, x0, gy, x1 - x0, H, fc=EXON, ec="none", r=0.03)
    label(ax, 0.45, gy - 0.22, t["exon"], fs=11, c=TEXT2, ha="left")
    # 붙는 자리
    ax.plot([a, a], [ry, gy + H], color=M1, lw=1.2)
    ax.plot([m - 0.02, m - 0.02], [ry, gy + H], color=M1, lw=1.2)
    ax.plot([m + 0.02, e2[0]], [ry, gy + H], color=M2, lw=1.2)
    ax.plot([b, e2[0] + (b - m)], [ry, gy + H], color=M2, lw=1.2)
    ax.plot([m, m], [gy - 0.1, ry + H + 0.1], color=TEXT, lw=1.3, ls=(0, (3, 2)), zorder=5)
    label(ax, m + 0.1, gy - 0.22, t["sj"], fs=11, c=TEXT, ha="left")
    # 설명
    label(ax, 0.45, 0.35, t["n1"], fs=11, ha="left")
    label(ax, 0.45, 0.05, t["n2"], fs=11, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W5_STAR{suffix}.png")
