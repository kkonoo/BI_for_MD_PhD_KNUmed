# W6 §1 이분산성: 이상적인 등분산 vs 발현량이 클수록 퍼짐이 커지는 RNA-seq (모의실험)
# 원본: assets/img/part2/W6_hetero.png (영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(p1="① 등분산 (이상적)", p2="② 이분산 (전형적인 RNA-seq)",
               x="평균 발현량", y="평균에서 벗어난 정도", n2="발현량이 클수록\n더 넓게 퍼짐"),
    "en": dict(p1="① Homoscedastic (ideal)", p2="② Heteroscedastic (typical RNA-seq)",
               x="mean expression", y="deviation from the mean", n2="higher expression,\nwider spread"),
}
STABLE, RAW = CAT[0], mix(TEXT2, 0.55)     # 안정된 분산 / 변환 전(같은 장의 vst·rlog 그림과 같은 색)
rng = np.random.default_rng(5)
x = rng.uniform(0, 10, 700)
sd_flat = np.full_like(x, 1.0)
sd_fan = 0.1 + 0.2 * x
y_flat, y_fan = rng.normal(0, sd_flat), rng.normal(0, sd_fan)


def panel(ax, y, sd, c, title, t):
    ax.scatter(x, y, s=7, color=c, alpha=0.55, lw=0)
    o = np.argsort(x)
    for k in (2, -2):
        ax.plot(x[o], k * sd[o], color=TEXT, lw=1.1, ls=(0, (3, 2)))
    ax.set_xlim(0, 10); ax.set_ylim(-5.2, 5.2)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(t["x"], fontsize=11)
    ax.text(0, 1.04, title, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")


def draw(t):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.9, 2.9), gridspec_kw=dict(wspace=0.12))
    panel(a1, y_flat, sd_flat, STABLE, t["p1"], t)
    panel(a2, y_fan, sd_fan, RAW, t["p2"], t)
    a1.set_ylabel(t["y"], fontsize=11)
    a2.text(0.03, 0.95, t["n2"], transform=a2.transAxes, fontsize=11, color=TEXT2, va="top", linespacing=1.35)
    fig.subplots_adjust(left=0.06, right=0.99, top=0.86, bottom=0.12)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W6_hetero{suffix}.png")
