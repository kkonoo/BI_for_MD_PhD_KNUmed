# W7 §3-3) GLM: log(μ)는 직선, 퍼짐은 μ + α·μ² 로 평균과 함께 커진다 (설명용 가상 자료)
# 원본: assets/img/part2/W7_GLM.png (세로로 긴 그림) → 넓고 낮게 다시 그림
from medfig import *
from statistics import NormalDist

L = {
    "ko": dict(var="Var = μ + α·μ²", note="평균이 클수록 더 퍼짐", mu="평균 μ"),
    "en": dict(var="Var = μ + α·μ²", note="spread grows with the mean", mu="mean μ"),
}
MEAN, SPREAD = CAT[0], CAT[1]            # W7_GLM_parts와 같게: 평균 모형 / 분산 모형
XS = [1, 2, 3, 4]
mu = lambda x: np.exp(0.05 + 0.5 * x)
sig = lambda x: 0.32 * np.sqrt(mu(x) + 0.15 * mu(x) ** 2)   # 설명용: Var = μ + α·μ²
Z = [-1.3, -0.55, 0.05, 0.6, 1.25]       # 설명용 관측값 위치(표준점수)
DX = [0.06, 0.2, 0.1, 0.24, 0.13]
pdf = NormalDist().pdf


def draw(t):
    fig = plt.figure(figsize=(6.8, 2.7))
    ax = fig.add_axes([0.06, 0.12, 0.92, 0.84])
    ax.set_xlim(0, 5.2); ax.set_ylim(0, 12)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("X", fontsize=12, labelpad=4); ax.set_ylabel("Y", fontsize=12, rotation=0, labelpad=10)
    xx = np.linspace(0.3, 4.7, 50)
    ax.plot(xx, mu(xx), color=MEAN, lw=2.6, zorder=3)
    ax.text(4.75, mu(4.7), t["mu"], fontsize=11.5, fontweight="bold", color=MEAN, va="center")
    for x in XS:
        y = np.linspace(-2.2, 2.2, 60)
        w = 0.42 * np.array([pdf(v) for v in y]) / pdf(0)
        ax.fill_betweenx(mu(x) + sig(x) * y, x, x + w, color=mix(SPREAD, 0.18), lw=0, zorder=1)
        ax.plot(x + w, mu(x) + sig(x) * y, color=mix(SPREAD, 0.6), lw=1, zorder=2)
        ax.plot([x, x], [mu(x) - 2.2 * sig(x), mu(x) + 2.2 * sig(x)], color=mix(SPREAD, 0.6), lw=1, zorder=2)
        ax.scatter([x + d for d in DX], [mu(x) + sig(x) * z for z in Z], s=22, color=shade(SPREAD, 0.1),
                   edgecolor="white", lw=0.6, zorder=4)
    ax.text(0.15, 10.9, "log(μ) = β₀ + β₁X", fontsize=12.5, fontweight="semibold", va="top")
    ax.text(5.15, 2.2, t["var"], fontsize=12, fontweight="bold", color=shade(SPREAD, 0.25), ha="right")
    ax.text(5.15, 1.1, t["note"], fontsize=11, color=TEXT2, ha="right")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W7_GLM{suffix}.png")
