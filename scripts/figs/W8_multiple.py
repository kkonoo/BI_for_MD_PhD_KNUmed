# W8 §1 다중검정 문제: p-value의 뜻(귀무분포의 꼬리)과, p < 0.05로 많이 검정하면 우연히 유의한 수가 늘어남
# 원본: assets/img/part3/W8_multiple.png (외부 그림 + 영어 글상자) → 다시 그림. 숫자는 본문(10,000 → 500)과 원본 그대로.
from medfig import *
from statistics import NormalDist

L = {
    "ko": dict(null="귀무가설(H₀) 분포\n그룹 간 차이 없음", obs="관측값", pv="p-value",
               xr="가능한 결과", head="p < 0.05로 검정하면",
               rows=[("유전자 100개", "우연히 유의 5개"), ("유전자 1,000개", "우연히 유의 50개"),
                     ("유전자 10,000개", "우연히 유의 500개")],
               foot="검정이 많을수록 위양성이 늘어남"),
    "en": dict(null="H₀ distribution\nno group difference", obs="observed", pv="p-value",
               xr="possible results", head="Testing at p < 0.05",
               rows=[("100 genes", "5 by chance"), ("1,000 genes", "50 by chance"),
                     ("10,000 genes", "500 by chance")],
               foot="More tests → more false positives"),
}
SIG = CAT[0]                     # 유의(p < 0.05) = W8_FDR과 같은 색


def draw(t):
    fig, ax = new(6.9, 3.1)
    # ── 왼쪽: 귀무분포와 p-value ──
    z = np.linspace(-3.4, 3.4, 300)
    X = lambda v: 0.2 + 2.9 * (v + 3.4) / 6.8
    y0, H = 0.62, 1.75
    pdf = np.array([NormalDist().pdf(v) for v in z]) / NormalDist().pdf(0) * H
    zo = 1.9
    tail = z >= zo
    ax.fill_between(X(z[tail]), y0, y0 + pdf[tail], color=SIG, lw=0, zorder=2)
    ax.plot(X(z), y0 + pdf, color=TEXT, lw=1.8, zorder=3)
    arrow(ax, 0.15, y0, 3.25, y0, color="#9AA1AB", lw=1.2, ms=10)
    label(ax, 1.7, y0 - 0.2, t["xr"], c=TEXT2)
    label(ax, X(0), y0 + H + 0.32, t["null"], fs=11.5, linespacing=1.3)
    ax.plot([X(zo)], [y0], "o", ms=6, color=TEXT, zorder=4)
    arrow(ax, X(zo) - 0.45, y0 + 0.55, X(zo) - 0.05, y0 + 0.07, color=TEXT2, lw=1.2, ms=9)
    label(ax, X(zo) - 0.5, y0 + 0.66, t["obs"], c=TEXT2, ha="right")
    arrow(ax, X(zo) + 0.62, y0 + 0.52, X(zo) + 0.2, y0 + 0.14, color=SIG, lw=1.2, ms=9)
    label(ax, X(zo) + 0.62, y0 + 0.66, t["pv"], fs=12, w="bold", c=SIG)

    # ── 오른쪽: 검정 수 → 우연히 유의한 수 ──
    x0 = 3.65
    label(ax, x0, 2.78, t["head"], fs=12.5, w="bold", ha="left")
    for i, (a, b) in enumerate(t["rows"]):
        y = 2.1 - i * 0.56
        box(ax, x0, y, 1.3, 0.42, fc=FAINT, ec=LINE)
        label(ax, x0 + 0.65, y + 0.21, a)
        arrow(ax, x0 + 1.36, y + 0.21, x0 + 1.6, y + 0.21, color="#9AA1AB", lw=1.4, ms=10)
        last = i == 2
        box(ax, x0 + 1.66, y, 1.6, 0.42, fc=ACCENT if last else mix(SIG, 0.12),
            ec="none" if last else mix(SIG, 0.35))
        label(ax, x0 + 2.46, y + 0.21, b, fs=11, w="bold" if last else "semibold",
              c=ON_ACCENT if last else shade(SIG, 0.25))
    label(ax, x0, 0.82, t["foot"], c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W8_multiple{suffix}.png")
