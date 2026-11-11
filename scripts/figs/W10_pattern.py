# W10 §2-2) ES 패턴 세 가지: 발현 증가 경로(위쪽에서 정점) / 무작위(0 근처 진동) / 발현 감소 경로(아래쪽에서 정점)
# 원본: assets/img/part3/W10_pattern.png (세로 3단 그래프) → 다시 그림. 설명용 가상 자료.
from medfig import *

L = {
    "ko": dict(p=["① 발현이 증가한 경로", "② 무작위 (농축 없음)", "③ 발현이 감소한 경로"],
               n=["위쪽에서 정점", "0 근처에서 진동", "아래쪽에서 정점"], r1="1", rN="N"),
    "en": dict(p=["① Up-regulated", "② Random", "③ Down-regulated"],
               n=["peak near the top", "fluctuates around zero", "peak near the bottom"], r1="1", rN="N"),
}
GENE = CAT[2]                                    # W10_threshold · W10_ES와 같은 색
COL = [CAT[0], TEXT2, CAT[1]]                    # 상향 / 무작위 / 하향 (W10_threshold와 같은 색)
N, K = 200, 20
rng = np.random.default_rng(5)
sets = [np.sort(np.r_[rng.choice(np.arange(0, 50), 15, replace=False), rng.choice(np.arange(50, 200), 5, replace=False)]),
        np.sort(rng.choice(np.arange(N), K, replace=False)),
        np.sort(np.r_[rng.choice(np.arange(0, 150), 5, replace=False), rng.choice(np.arange(150, 200), 15, replace=False)])]


def walk(h):
    step = np.where(np.isin(np.arange(N), h), 1 / K, -1 / (N - K))
    return np.r_[0, np.cumsum(step)]


def draw(t):
    fig, ax = new(6.9, 2.9)
    sc = 0.72 / max(abs(walk(s)).max() for s in sets)
    for j, (h, c) in enumerate(zip(sets, COL)):
        X0, W = 0.05 + j * 2.32, 2.1
        rs = walk(h); xs = X0 + W * np.arange(N + 1) / N
        base = 1.55
        label(ax, X0, 2.72, t["p"][j], fs=12, w="bold", ha="left")
        ax.plot([X0, X0 + W], [base, base], color="#9AA1AB", lw=1, zorder=2)
        ax.fill_between(xs, base, base + rs * sc, color=mix(c, 0.14), lw=0, zorder=1)
        ax.plot(xs, base + rs * sc, color=c, lw=1.8, zorder=3)
        box(ax, X0, 0.5, W, 0.26, fc=FAINT, ec=LINE, r=0.04)
        ax.vlines([X0 + W * (i + 0.5) / N for i in h], 0.53, 0.73, color=GENE, lw=1.2, zorder=4)
        label(ax, X0, 0.36, t["r1"], fs=11, c=TEXT2, ha="left")
        label(ax, X0 + W, 0.36, t["rN"], fs=11, c=TEXT2, ha="right")
        label(ax, X0 + W / 2, 0.08, t["n"][j], fs=11.5, c=shade(c, 0.15) if j != 1 else TEXT2, w="semibold")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W10_pattern{suffix}.png")
