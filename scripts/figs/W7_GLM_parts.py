# W7 §3-3) GLM: DESeq2 모형의 두 부분(평균 모형 · 분산 모형)과 분산 분해
# 원본: assets/img/part2/W7_GLM_parts.png (자체 제작, 한·영 섞임) → 다시 그림
from medfig import *

L = {
    "ko": dict(q1="평균은 어디?", q2="얼마나 퍼져?",
               p1="① 평균 모형", s1="유전자마다 기대 발현량은?",
               p2="② 분산 모형", s2="μ 주변에 얼마나 흩어지나?",
               t=["기준선", "= LFC", "batch 보정", "표본 추출 잡음", "생물학적 변이"],
               dec="분산 분해: 전체 분산 = Condition + Batch + Residual",
               b=["β₁이 설명하는 분산", "β₂가 설명하는 분산", "NB 분산(μ + α·μ²)이 담당"]),
    "en": dict(q1="Where is the mean?", q2="How spread out?",
               p1="① Mean model", s1="Expected expression of each gene?",
               p2="② Variance model", s2="How much scatter around μ?",
               t=["baseline", "= LFC", "batch correction", "sampling noise", "biological variation"],
               dec="Variance decomposition: total = Condition + Batch + Residual",
               b=["variance explained by β₁", "variance explained by β₂", "handled by NB (μ + α·μ²)"]),
}
C1, C2 = CAT[0], CAT[1]          # 평균 모형 / 분산 모형


def draw(t):
    fig, ax = new(6.9, 6.2)
    # 맨 위: 모형 전체
    box(ax, 1.35, 5.55, 4.2, 0.55, fc=FAINT, ec=LINE)
    label(ax, 3.45, 5.825, "Y ~ NegBinomial(μ, α)", fs=14, w="semibold")
    for x, q, c in [(1.75, t["q1"], C1), (5.15, t["q2"], C2)]:
        arrow(ax, x, 5.55, x, 4.98, color="#9AA1AB")
        label(ax, x + 0.12, 5.27, q, fs=11, c=TEXT2, ha="left")

    # 두 부분: 머리 칸 + 식 칸
    parts = [(0.05, 3.4, C1, t["p1"], t["s1"], "log(μ) = β₀ + β₁·cond + β₂·batch"),
             (3.6, 3.25, C2, t["p2"], t["s2"], "Var = μ + α·μ²")]
    for x, w, c, p, s, eq in parts:
        box(ax, x, 4.3, w, 0.66, fc=c, ec="none")
        label(ax, x + w / 2, 4.75, p, fs=12.5, w="bold", c="white")
        label(ax, x + w / 2, 4.47, s, fs=11, c="white")
        box(ax, x, 3.62, w, 0.52, fc=mix(c, 0.10), ec=mix(c, 0.35))
        label(ax, x + w / 2, 3.88, eq, fs=12.5, w="semibold", c=shade(c, 0.25))

    # 항: β₀ β₁ β₂ / μ α·μ²
    terms = [(0.6, "β₀", C1, False), (1.75, "β₁", C1, True), (2.9, "β₂", C1, False),
             (4.4, "μ", C2, False), (6.05, "α·μ²", C2, False)]
    for (cx, sym, c, key), sub in zip(terms, t["t"]):
        arrow(ax, cx, 3.62, cx, 3.2, color=mix(c, 0.55), lw=1.4, ms=10)
        fc = ACCENT if key else mix(c, 0.10)
        box(ax, cx - 0.45, 2.7, 0.9, 0.48, fc=fc, ec="none" if key else mix(c, 0.35))
        label(ax, cx, 2.94, sym, fs=13, w="bold", c=ON_ACCENT if key else shade(c, 0.25))
        label(ax, cx, 2.48, sub, fs=11.5 if key else 11, w="bold" if key else "regular",
              c=ACCENT_INK if key else TEXT2)

    # 점선: 어느 항이 어느 분산을 설명하는지 (β₁ → Condition, β₂ → Batch, 분산 모형 → Residual)
    dash = dict(lw=1.2, ls=(0, (3, 2)), zorder=1)
    ax.plot([1.75, 1.75], [2.33, 2.02], color=mix(C1, 0.55), **dash)
    ax.plot([2.9, 2.9], [2.33, 2.02], color=mix(C1, 0.55), **dash)
    ax.plot([4.4, 4.4, 6.05, 6.05], [2.33, 2.2, 2.2, 2.33], color=mix(C2, 0.55), **dash)
    ax.plot([5.2, 5.2], [2.2, 2.02], color=mix(C2, 0.55), **dash)
    # 분산 분해 띠
    box(ax, 0.05, 1.5, 6.8, 0.5, fc=FAINT, ec=LINE)
    label(ax, 3.45, 1.75, t["dec"], fs=12, w="semibold")
    comps = [(1.15, "Condition", C1), (3.45, "Batch", C1), (5.75, "Residual", C2)]
    for (cx, name, c), sub in zip(comps, t["b"]):
        arrow(ax, cx, 1.5, cx, 1.14, color="#9AA1AB", lw=1.4, ms=10)
        box(ax, cx - 1.1, 0.3, 2.2, 0.82, fc=mix(c, 0.10), ec=mix(c, 0.35))
        label(ax, cx, 0.89, name, fs=12.5, w="bold", c=shade(c, 0.25))
        label(ax, cx, 0.55, sub, fs=11, c=TEXT2)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W7_GLM_parts{suffix}.png")
