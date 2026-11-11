# W5 §3 정렬 없는 정량(Salmon): transcript로 k-mer 인덱스 → 리드는 k-mer 일치만 확인 → EM으로 isoform에 나눔
# 원본: assets/img/part2/W5_salmon.png (Salmon 문서 그림, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(tx="참조 transcript", rd="리드 (FASTQ)",
               b1=("Salmon index", "k-mer (k = 31)"), b2=("quasi-mapping", "k-mer 일치만 확인"),
               b3=("EM 알고리즘", "여러 곳에 맞는 리드를\nisoform별 확률로 나눔"),
               ex="예: read A → X (0.6), Y (0.4)", nobam="BAM 파일 없이 진행\n→ 매우 빠름"),
    "en": dict(tx="reference transcripts", rd="reads (FASTQ)",
               b1=("Salmon index", "k-mers (k = 31)"), b2=("quasi-mapping", "check k-mer matches only"),
               b3=("EM algorithm", "splits multi-mapping reads\ninto isoform probabilities"),
               ex="e.g. read A → X (0.6), Y (0.4)", nobam="no BAM file needed\n→ very fast"),
}
C = ramp(3)


def step(ax, x, y, w, c, head, sub, h=0.62):
    """머리 칸(y 위) + 설명 칸(y 아래, 높이 h). y = 두 칸 경계."""
    box(ax, x, y + 0.04, w, 0.4, fc=c, ec="none")
    label(ax, x + w / 2, y + 0.24, head, fs=12, w="bold", c=on(c))
    box(ax, x, y - h, w, h, fc=mix(c, 0.08), ec=mix(c, 0.3))
    label(ax, x + w / 2, y - h / 2, sub, fs=11, c=TEXT, linespacing=1.3)


def draw(t):
    fig, ax = new(6.9, 3.0)
    # 입력: transcript(긴 선) / 리드(짧은 선)
    rng = np.random.default_rng(1)
    for i in range(4):
        ax.plot([0.05 + 0.1 * (i % 2), 1.25 - 0.1 * (i % 3)], [2.75 - i * 0.12] * 2, color=TEXT2, lw=1.6)
    label(ax, 0.05, 2.2, t["tx"], fs=11, c=TEXT2, ha="left")
    for i in range(10):
        x0 = 0.05 + rng.uniform(0, 0.95)
        ax.plot([x0, x0 + 0.22], [1.0 - (i % 5) * 0.12 + (i // 5) * 0.04] * 2, color=TEXT2, lw=1.6)
    label(ax, 0.05, 0.3, t["rd"], fs=11, c=TEXT2, ha="left")
    # 단계
    step(ax, 1.75, 2.55, 2.05, C[0], *t["b1"], h=0.5)
    step(ax, 1.75, 0.95, 2.05, C[1], *t["b2"])
    step(ax, 4.45, 0.95, 2.4, C[2], *t["b3"])
    arrow(ax, 1.35, 2.55, 1.7, 2.55)
    arrow(ax, 1.35, 0.75, 1.7, 0.75)
    arrow(ax, 2.775, 2.03, 2.775, 1.42)
    arrow(ax, 3.85, 0.75, 4.4, 0.75)
    label(ax, 5.65, 0.1, t["ex"], fs=11, c=TEXT2)
    label(ax, 4.45, 2.4, t["nobam"], fs=11, w="semibold", c=TEXT, ha="left", linespacing=1.35)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W5_salmon{suffix}.png")
