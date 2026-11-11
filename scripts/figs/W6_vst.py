# W6 §1 vst: 발현량에 따라 커지던 퍼짐을 고르게 만듦 (모의실험). 50% 칸에 들어가는 좁은 그림(~3.3 in), 위아래로 쌓음.
# 원본: assets/img/part2/W6_vst.png (영어, 오타 있는 식 포함) → 다시 그림. 식은 본문에 없어 뺌.
from medfig import *

L = {
    "ko": dict(p1="① vst 전", p2="② vst 후", n1="발현량이 클수록 퍼짐 ↑", n2="퍼짐이 고르게",
               x="평균 발현량", y="편차"),
    "en": dict(p1="① before vst", p2="② after vst", n1="spread grows with expression", n2="even spread",
               x="mean expression", y="deviation"),
}
STABLE, RAW = CAT[0], mix(TEXT2, 0.55)     # W6_hetero와 같은 색
rng = np.random.default_rng(11)
x = rng.uniform(0, 10, 600)
y_raw = rng.normal(0, 0.1 + 0.2 * x)
y_vst = rng.normal(0, 0.75, x.size)


def panel(ax, y, c, title, note, t):
    ax.scatter(x, y, s=6, color=c, alpha=0.55, lw=0)
    ax.set_xlim(0, 10); ax.set_ylim(-5.2, 5.2)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel(t["x"], fontsize=11, labelpad=2); ax.set_ylabel(t["y"], fontsize=11, labelpad=2)
    ax.text(0, 1.05, title, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")
    ax.text(0.03, 0.95, note, transform=ax.transAxes, fontsize=11, color=TEXT2, ha="left", va="top")


def draw(t):
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(3.3, 4.6), gridspec_kw=dict(hspace=0.55))
    panel(a1, y_raw, RAW, t["p1"], t["n1"], t)
    panel(a2, y_vst, STABLE, t["p2"], t["n2"], t)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.93, bottom=0.07)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W6_vst{suffix}.png")
