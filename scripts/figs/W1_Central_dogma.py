# W1 §1 중심 원리: DNA → RNA → 단백질, 각 층을 다루는 오믹스와 질문. 이 수업은 전사체(RNA)에 집중.
# 원본: assets/img/part1/Central_dogma.png (BioRender 그림, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(m=["DNA", "RNA", "단백질"], tx="전사", rt="역전사", tl="번역",
               layer=["유전체 (설계도)", "전사체 (전달자)", "단백체 (기계)"],
               omics=["Genomics", "Transcriptomics", "Proteomics"],
               q=["질병과 관련된\n유전 변이는?", "환자에서 발현이 달라진\n유전자는?", "양이 달라진\n단백질은?"]),
    "en": dict(m=["DNA", "RNA", "Protein"], tx="Transcription", rt="Reverse\ntranscription", tl="Translation",
               layer=["Genome (blueprint)", "Transcriptome (messenger)", "Proteome (machine)"],
               omics=["Genomics", "Transcriptomics", "Proteomics"],
               q=["Which mutations are\nlinked to disease?", "Which genes are differentially\nexpressed in patients?",
                  "Which proteins show\naltered abundance?"]),
}
FILL = [CAT[0], ACCENT, CAT[2]]          # 이 수업이 다루는 RNA만 강조


def draw(t):
    fig, ax = new(6.9, 3.4)
    xs, cy, r = [1.2, 3.45, 5.7], 2.75, 0.55
    for x, m, c in zip(xs, t["m"], FILL):
        ax.add_patch(mp.Circle((x, cy), r, fc=c, ec="none", zorder=3))
        label(ax, x, cy, m, fs=15, w="bold", c=ON_ACCENT if c == ACCENT else "white")
    # 화살표
    a1, b1 = xs[0] + r + 0.1, xs[1] - r - 0.1
    arrow(ax, a1, cy + 0.12, b1, cy + 0.12, color=TEXT2, lw=1.8)
    label(ax, (a1 + b1) / 2, cy + 0.32, t["tx"], fs=11.5, w="semibold")
    arrow(ax, b1, cy - 0.12, a1, cy - 0.12, color=mix(TEXT2, 0.5), lw=1.4, ls=(0, (3, 2)))
    label(ax, (a1 + b1) / 2, cy - 0.3, t["rt"], fs=11, c=TEXT2, va="top", linespacing=1.2)
    a2, b2 = xs[1] + r + 0.1, xs[2] - r - 0.1
    arrow(ax, a2, cy + 0.12, b2, cy + 0.12, color=TEXT2, lw=1.8)
    label(ax, (a2 + b2) / 2, cy + 0.32, t["tl"], fs=11.5, w="semibold")
    # 층 이름 · 오믹스 · 질문
    for x, ly, om, q in zip(xs, t["layer"], t["omics"], t["q"]):
        label(ax, x, 1.8, ly, fs=12, w="semibold")
        box(ax, x - 1.08, 0.1, 2.16, 1.28, fc=FAINT, ec=LINE)
        label(ax, x, 1.1, om, fs=12.5, w="bold")
        label(ax, x, 0.56, q, fs=11, c=TEXT2, linespacing=1.35)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/Central_dogma{suffix}.png")
