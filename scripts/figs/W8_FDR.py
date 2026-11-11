# W8 §1 FDR: 신호가 없을 때와 있을 때의 p-value 분포, α로 자르면 생기는 FP·TP·FN·TN
# 원본: assets/img/part3/W8_FDR.png (외부 그림 조합, 영어) → 다시 그림. 히스토그램은 모의실험.
from medfig import *
from statistics import NormalDist

L = {
    "ko": dict(p1="① 신호가 없을 때 (모두 귀무가설)", p2="② 실제 신호가 섞여 있을 때",
               p3="③ α로 자르면", sig="p < 0.05\n(유의)", x="p-value", y="유전자 수",
               flat="고르게 퍼짐\n→ 5%는 우연히 유의", spike="0 근처에 쌓임",
               null="귀무가설 유전자", true="실제 DEG",
               fdr="FDR = FP / (FP + TP)\n유의하다고 한 것 중 가짜의 비율"),
    "en": dict(p1="① No signal (all genes null)", p2="② Some true signal",
               p3="③ Cutting at α", sig="p < 0.05", x="p-value", y="number of genes",
               flat="flat: 5% are\nsignificant by chance", spike="piles up near 0",
               null="null genes", true="true DEGs",
               fdr="FDR = FP / (FP + TP)\nfalse share of significant calls"),
}
rng = np.random.default_rng(7)
p_null = rng.uniform(size=5000)                                     # 모의실험: 5,000개 모두 귀무가설
z = rng.normal(3.0, 1.0, size=1500)                                 # 모의실험: 1,500개 실제 DEG
p_mix = np.r_[rng.uniform(size=3500), [2 * (1 - NormalDist().cdf(abs(v))) for v in z]]
bins = np.linspace(0, 1, 21)                                        # 첫 칸 = p < 0.05
GREY, SIG = mix(TEXT2, 0.35), CAT[0]


def hist(ax, p, title, note, t):
    n, _, bars = ax.hist(p, bins=bins, color=GREY, edgecolor="white", lw=0.6)
    bars[0].set_facecolor(SIG)
    ax.set_xlim(0, 1); ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "0.5", "1"])
    ax.set_xlabel(t["x"], fontsize=11)
    ax.text(0.0, 1.13, title, transform=ax.transAxes, fontsize=12, fontweight="bold", color=TEXT, va="bottom")
    ax.text(0.98, 0.95, note, transform=ax.transAxes, fontsize=11, color=TEXT2, ha="right", va="top", linespacing=1.35)
    return n


def draw(t):
    fig = plt.figure(figsize=(6.9, 6.0))
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.05], hspace=0.62, wspace=0.28,
                          left=0.1, right=0.98, top=0.9, bottom=0.04)
    a1, a2 = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1])
    n1 = hist(a1, p_null, t["p1"], t["flat"], t)
    a1.set_ylabel(t["y"], fontsize=11); a1.set_ylim(0, n1.max() * 1.6)
    n2 = hist(a2, p_mix, t["p2"], t["spike"], t)
    a2.set_ylim(0, n2.max() * 1.12)
    a1.annotate(t["sig"], xy=(0.03, n1[0]), xytext=(0.08, n1.max() * 1.3), fontsize=11, color=SIG,
                fontweight="bold", ha="left", va="center", linespacing=1.2,
                arrowprops=dict(arrowstyle="-|>", color=SIG, lw=1.2))

    # ③ 개념도: 바닥(귀무가설) + 0 근처 봉우리(실제 DEG), α는 보기 쉽게 넓혀 그림
    a3 = fig.add_subplot(gs[1, :]); a3.axis("off")
    a3.text(0.0, 1.06, t["p3"], transform=a3.transAxes, fontsize=12, fontweight="bold", color=TEXT, va="bottom")
    x = np.linspace(0, 1, 400); al = 0.22
    floor = np.full_like(x, 0.35)
    top = floor + 1.6 * np.exp(-x / 0.13)
    L_, R_ = x <= al, x >= al
    a3.fill_between(x[R_], 0, floor[R_], color=mix(TEXT2, 0.18), lw=0)                 # TN
    a3.fill_between(x[L_], 0, floor[L_], color=ACCENT, lw=0)                          # FP (강조)
    a3.fill_between(x[L_], floor[L_], top[L_], color=SIG, lw=0)                       # TP
    a3.fill_between(x[R_], floor[R_], top[R_], color=mix(SIG, 0.35), lw=0)            # FN
    a3.plot(x, top, color=TEXT, lw=1)
    a3.plot([al, al], [0, 2.05], color=TEXT, lw=1.2, ls=(0, (3, 2)))
    a3.plot([0, 1], [0, 0], color="#9AA1AB", lw=1)
    a3.text(al, -0.12, "α", ha="center", va="top", fontsize=12, fontweight="bold", color=TEXT)
    a3.text(0, -0.12, "0", ha="center", va="top", fontsize=11, color=TEXT2)
    a3.text(1, -0.12, "1", ha="center", va="top", fontsize=11, color=TEXT2)
    a3.text(0.5, -0.12, t["x"], ha="center", va="top", fontsize=11, color=TEXT2)
    a3.text(al / 2, 0.175, "FP", ha="center", va="center", fontsize=12, fontweight="bold", color=ON_ACCENT)
    a3.text(0.045, 0.7, "TP", ha="center", va="center", fontsize=12, fontweight="bold", color="white")
    a3.text(0.6, 0.175, "TN", ha="center", va="center", fontsize=12, fontweight="bold", color=TEXT)
    a3.annotate("FN", xy=(al + 0.04, 0.52), xytext=(al + 0.14, 1.0), fontsize=12, fontweight="bold",
                color=shade(SIG, 0.2), ha="center", arrowprops=dict(arrowstyle="-|>", color=TEXT2, lw=1))
    # 범례
    for i, (c, s) in enumerate([(mix(TEXT2, 0.18), t["null"]), (mix(SIG, 0.35), t["true"])]):
        a3.add_patch(mp.Rectangle((0.5, 1.82 - i * 0.3), 0.025, 0.17, fc=c, ec="none"))
        a3.text(0.535, 1.905 - i * 0.3, s, va="center", fontsize=11, color=TEXT2)
    a3.text(0.8, 1.0, t["fdr"], ha="center", va="center", fontsize=12, color=TEXT, linespacing=1.6,
            bbox=dict(boxstyle="round,pad=0.5", fc=FAINT, ec=LINE))
    a3.set_xlim(-0.02, 1.02); a3.set_ylim(-0.3, 2.1)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W8_FDR{suffix}.png")
