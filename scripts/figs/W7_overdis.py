# W7 §3-1) 과대산포: 이상적 자료는 분산이 평균과 무관, RNA-seq는 분산 ≫ 평균 (설명용 가상 자료)
# 원본: assets/img/part2/W7_overdis.png (외부 그림 조합, 영어, 기울임꼴) → 다시 그림
from medfig import *

L = {
    "ko": dict(p1="① 이상적인 경우", p2="② 실제 RNA-seq", x="평균 발현량", y="분산",
               n1="분산과 평균이 무관\n→ 정규분포 (LM)", n2="분산 ≫ 평균\n→ 음이항분포 (GLM)"),
    "en": dict(p1="① Ideal", p2="② Typical RNA-seq", x="mean expression", y="variance",
               n1="variance independent of mean\n→ normal distribution (LM)",
               n2="variance ≫ mean\n→ negative binomial (GLM)"),
}
IDEAL, RNA = mix(TEXT2, 0.55), CAT[1]    # RNA-seq 쪽 = 분산 모형 색 (W7_GLM_parts와 같게)
rng = np.random.default_rng(5)
m = rng.uniform(0.3, 10, 260)
v_ideal = 30 + rng.normal(0, 7, m.size)                     # 평균과 무관
a = 0.5
v_rna = (m + a * m ** 2) * np.exp(rng.normal(0, 0.28, m.size))   # μ + α·μ² 주변
xx = np.linspace(0, 10, 100)


def draw(t):
    fig = plt.figure(figsize=(6.8, 3.6))
    axs = [fig.add_axes([0.08, 0.36, 0.40, 0.55]), fig.add_axes([0.58, 0.36, 0.40, 0.55])]
    for ax, p, v, c, n in [(axs[0], t["p1"], v_ideal, IDEAL, t["n1"]), (axs[1], t["p2"], v_rna, RNA, t["n2"])]:
        ax.scatter(m, v, s=9, color=c, lw=0, zorder=2)
        ax.set_xlim(0, 10.5); ax.set_ylim(0, 82)
        ax.set_xticks([]); ax.set_yticks([])
        ax.set_xlabel(t["x"], fontsize=11, color=TEXT2); ax.set_ylabel(t["y"], fontsize=11, color=TEXT2)
        ax.text(0, 1.06, p, transform=ax.transAxes, fontsize=12, fontweight="bold", va="bottom")
        ax.text(0.5, -0.2, n, transform=ax.transAxes, fontsize=11, ha="center", va="top", linespacing=1.4)
    ax = axs[1]
    ax.plot(xx, xx + a * xx ** 2, color=shade(RNA, 0.25), lw=2, zorder=3)
    ax.plot(xx, xx, color=TEXT2, lw=1.2, ls=(0, (3, 2)), zorder=3)
    ax.text(10.4, 10.4 + 3, "Var = μ", fontsize=11, color=TEXT2, ha="right", va="bottom")
    ax.text(7.6, 79, "Var = μ + α·μ²", fontsize=11.5, fontweight="bold", color=shade(RNA, 0.25),
            ha="right", va="top")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W7_overdis{suffix}.png")
