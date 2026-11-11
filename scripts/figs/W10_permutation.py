# W10 §2-3) 순열 검정: 실제 라벨로 ES 계산 → 라벨을 1,000번 섞어 무작위 ES 1,000개(귀무분포) → 관측 ES 위치 확인
# 원본: assets/img/part3/W10_permutation.png (외부 그림 조합) → 다시 그림. 히스토그램은 모의실험.
from medfig import *

L = {
    "ko": dict(r1="① 실제 라벨로 계산", r2="② 라벨을 1,000번 섞어 계산", obs="관측 ES",
               rnd="무작위 ES\n1,000개", null="귀무분포", x="ES", y="횟수"),
    "en": dict(r1="① ES from the real labels", r2="② Shuffle labels 1,000 times", obs="observed ES",
               rnd="1,000\nrandom ES", null="null distribution", x="ES", y="count"),
}
GA, GB = mix(TEXT2, 0.8), mix(TEXT2, 0.22)        # 시료 그룹 A / B (중립색)
rng = np.random.default_rng(4)
null = rng.normal(0, 1, 1000)                     # 모의실험: 무작위 ES 1,000개
OBS = 3.0


def samples(ax, x, y, labs, s=0.27, g=0.05, z=3):
    for i, l in enumerate(labs):
        c = GA if l == "A" else GB
        box(ax, x + i * (s + g), y, s, s, fc=c, ec="white", lw=1, r=0.04, z=z)
        ax.text(x + i * (s + g) + s / 2, y + s / 2, l, ha="center", va="center", fontsize=11,
                fontweight="bold", color=on(c), zorder=z + 1)


def draw(t):
    fig, ax = new(6.9, 3.1)
    # ① 실제 라벨
    label(ax, 0.05, 2.9, t["r1"], fs=12, w="bold", ha="left")
    samples(ax, 0.1, 2.3, list("AAABBB"))
    arrow(ax, 2.1, 2.435, 2.45, 2.435, color="#9AA1AB", lw=1.4, ms=10)
    pill(ax, 2.5, 2.435, t["obs"], fc=ACCENT, tc=ON_ACCENT, fs=11.5, h=0.34, ha="left")
    # ② 섞은 라벨 (겹친 카드 3장)
    label(ax, 0.05, 1.62, t["r2"], fs=12, w="bold", ha="left")
    for k, off in enumerate([0.24, 0.12, 0.0]):
        labs = list(rng.permutation(list("AAABBB")))
        box(ax, 0.04 + off, 0.5 + off, 2.0, 0.42, fc="white", ec=LINE, r=0.06, z=3 + 3 * k)
        samples(ax, 0.1 + off, 0.575 + off, labs, z=4 + 3 * k)
    arrow(ax, 2.38, 0.85, 2.73, 0.85, color="#9AA1AB", lw=1.4, ms=10)
    label(ax, 2.8, 0.85, t["rnd"], fs=11.5, ha="left", linespacing=1.3)

    # 귀무분포 히스토그램
    h = fig.add_axes([3.95 / 6.9, 0.55 / 3.1, 2.6 / 6.9, 2.2 / 3.1])
    n, _, _ = h.hist(null, bins=np.linspace(-3.6, 3.6, 25), color=mix(TEXT2, 0.35), edgecolor="white", lw=0.6)
    h.set_xlim(-3.8, 3.9); h.set_ylim(0, n.max() * 1.35)
    h.set_xticks([0]); h.set_yticks([]); h.tick_params(labelsize=11)
    h.set_xlabel(t["x"], fontsize=11); h.set_ylabel(t["y"], fontsize=11)
    h.text(-3.6, n.max() * 1.22, t["null"], fontsize=11, color=TEXT2, va="center")
    h.annotate("", xy=(OBS, 0), xytext=(OBS, n.max() * 0.62),
               arrowprops=dict(arrowstyle="-|>", color=ACCENT_INK, lw=1.8))
    h.text(OBS, n.max() * 0.68, t["obs"], ha="center", va="bottom", fontsize=11.5, fontweight="bold",
           color=ACCENT_INK)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W10_permutation{suffix}.png")
