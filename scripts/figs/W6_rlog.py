# W6 §1 rlog: 유전자별 shrinkage로 낮은 count 유전자의 log fold change 잡음을 줄임 (모의실험). 50% 칸용 좁은 그림.
# 원본: assets/img/part2/W6_rlog.png (영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(p1="① log2 (shrinkage 전)", p2="② rlog (shrinkage 후)",
               n1="낮은 count: 잡음 ↑", n2="잡음이 줄어듦", x="평균 발현량", y="log fold change"),
    "en": dict(p1="① log2 (before shrinkage)", p2="② rlog (after shrinkage)",
               n1="low counts: noisy", n2="noise suppressed", x="mean expression", y="log fold change"),
}
STABLE, RAW = CAT[0], mix(TEXT2, 0.55)     # W6_hetero · W6_vst와 같은 색
rng = np.random.default_rng(4)
m = 10 ** rng.uniform(0, 4, 700)                       # 평균 발현량(로그 축)
noise = rng.normal(0, 1, m.size)
y_log = noise * (0.12 + 2.2 / np.sqrt(m))
y_rlog = noise * (0.12 + 0.35 / np.sqrt(m))


def panel(ax, y, c, title, note, t):
    ax.scatter(m, y, s=6, color=c, alpha=0.55, lw=0)
    ax.axhline(0, color=TEXT, lw=1.1, ls=(0, (3, 2)))
    ax.set_xscale("log"); ax.set_xlim(1, 1e4); ax.set_ylim(-4.5, 4.5)
    ax.set_xticks([]); ax.set_yticks([]); ax.minorticks_off()
    ax.set_xlabel(t["x"], fontsize=11, labelpad=2); ax.set_ylabel(t["y"], fontsize=11, labelpad=2)
    ax.text(0, 1.05, title, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")
    ax.text(0.97, 0.94, note, transform=ax.transAxes, fontsize=11, color=TEXT2, ha="right", va="top")


def draw(t):
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(3.3, 4.6), gridspec_kw=dict(hspace=0.55))
    panel(a1, y_log, RAW, t["p1"], t["n1"], t)
    panel(a2, y_rlog, STABLE, t["p2"], t["n2"], t)
    fig.subplots_adjust(left=0.1, right=0.97, top=0.93, bottom=0.07)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W6_rlog{suffix}.png")
