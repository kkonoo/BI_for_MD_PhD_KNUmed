# W10 §2-2) ES 계산: 순위를 따라 걸으며 경로 유전자면 +1/K, 아니면 −1/(N−K); ES = 0에서 가장 멀리 벗어난 값
# 원본: assets/img/part3/W10_ES.png (외부 그림 + 예시 숫자) → 다시 그림. 본문에 없는 예시 숫자(500/10,000)는 뺌. 설명용 가상 자료.
from medfig import *

L = {
    "ko": dict(rs="누적합", r1="순위 1", rN="N", hit="경로 유전자 → +1/K", miss="그 외 유전자 → −1/(N−K)",
               es="ES\n0에서 가장 멀리\n벗어난 값", k="K = 경로 크기"),
    "en": dict(rs="running sum", r1="rank 1", rN="N", hit="pathway gene → +1/K", miss="other gene → −1/(N−K)",
               es="ES\nlargest distance\nfrom zero", k="K = pathway size"),
}
GENE, CURVE = CAT[2], CAT[0]     # W10_threshold와 같은 색
N = 200
rng = np.random.default_rng(11)
hits = np.sort(np.r_[[3, 7, 10, 16, 21, 27, 33, 41, 52], rng.choice(np.arange(70, 195), 4, replace=False)])
K = len(hits)
step = np.where(np.isin(np.arange(N), hits), 1 / K, -1 / (N - K))
rs = np.r_[0, np.cumsum(step)]


def draw(t):
    fig, ax = new(6.9, 3.0)
    X0, W = 0.5, 4.1
    xs = X0 + W * np.arange(N + 1) / N
    base, sc = 0.95, 1.75 / rs.max()
    # 축과 곡선
    ax.plot([X0, X0], [0.75, 2.85], color="#9AA1AB", lw=1)
    ax.plot([X0, X0 + W], [base, base], color="#9AA1AB", lw=1)
    ax.fill_between(xs, base, base + rs * sc, where=rs > 0, color=mix(CURVE, 0.12), lw=0, zorder=2)
    ax.plot(xs, base + rs * sc, color=CURVE, lw=2, zorder=3)
    label(ax, X0 - 0.24, base + 0.95, t["rs"], c=TEXT2, rotation=90)
    label(ax, X0 - 0.08, base, "0", c=TEXT2, ha="right")
    # 경로 유전자 띠
    box(ax, X0, 0.35, W, 0.3, fc=FAINT, ec=LINE, r=0.04)
    ax.vlines([X0 + W * (h + 0.5) / N for h in hits], 0.38, 0.62, color=GENE, lw=2.2, zorder=4)
    label(ax, X0, 0.16, t["r1"], c=TEXT2, ha="left")
    label(ax, X0 + W, 0.16, t["rN"], c=TEXT2, ha="right")
    arrow(ax, X0 + 0.75, 0.16, X0 + W - 0.25, 0.16, color="#C9CDD3", lw=1.2, ms=9)
    # ES
    k = rs.argmax(); xk = xs[k]; yk = base + rs[k] * sc
    ax.plot([X0, xk], [yk, yk], color=ACCENT_INK, lw=1, ls=(0, (3, 2)), zorder=2)
    ax.annotate("", xy=(xk, yk), xytext=(xk, base), arrowprops=dict(arrowstyle="<|-|>", color=ACCENT_INK,
                lw=1.6, shrinkA=0, shrinkB=0, mutation_scale=12), zorder=5)
    label(ax, xk + 0.12, base + rs[k] * sc / 2, t["es"], fs=11, c=ACCENT_INK, ha="left", linespacing=1.3)
    ax.texts[-1].set_fontweight("bold")
    # 규칙
    x1 = 4.95
    box(ax, x1, 1.0, 1.95, 1.2, fc=FAINT, ec=LINE)
    ax.vlines(x1 + 0.17, 1.83, 2.03, color=GENE, lw=2.2)
    label(ax, x1 + 0.3, 1.93, t["hit"], ha="left")
    ax.vlines(x1 + 0.17, 1.43, 1.63, color="#C9CDD3", lw=2.2)
    label(ax, x1 + 0.3, 1.53, t["miss"], ha="left")
    label(ax, x1 + 0.3, 1.17, t["k"], c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W10_ES{suffix}.png")
