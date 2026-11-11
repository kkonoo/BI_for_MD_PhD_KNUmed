# W1 §1 생물정보학이란: 생물학 + 컴퓨터 과학 + 통계학, 시료 → 오믹스 데이터 → 분석
# 원본: assets/img/part1/Bioinformatics.png (BioRender 그림, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(f=["생물학", "컴퓨터 과학", "통계학"],
               s=["시료 채취", "데이터 생산", "분석"],
               n=["Bio: 특정 표현형을 가진\n사람의 시료", "Information:\n오믹스 데이터", "생물학적 의미는?"]),
    "en": dict(f=["Biology", "Computer science", "Statistics"],
               s=["Sampling", "Data generation", "Analysis"],
               n=["Bio: human samples\nwith a phenotype", "Information:\nomics data", "Any biological meaning?"]),
}


def draw(t):
    fig, ax = new(6.9, 3.2)
    # 위: 세 분야의 합
    w, gap = 1.98, 0.42
    for i, (name, c) in enumerate(zip(t["f"], CAT[:3])):
        x = 0.1 + i * (w + gap)
        box(ax, x, 2.15, w, 0.62, fc=c, ec="none")
        label(ax, x + w / 2, 2.46, name, fs=12.5, w="bold", c="white")
        if i < 2:
            label(ax, x + w + gap / 2, 2.46, "+", fs=18, w="bold", c=TEXT2)
    # 아래: 작업 흐름
    cw = 2.3
    for i, (s, c) in enumerate(zip(t["s"], ramp(3))):
        x = 0.1 + i * (cw - 0.02)
        chevron(ax, x, 1.25, cw - 0.06, 0.62, fc=mix(c, 0.15), first=(i == 0))
        label(ax, x + cw / 2 + (0 if i == 0 else 0.06), 1.56, s, fs=12.5, w="bold", c=shade(c, 0.3))
        label(ax, x + cw / 2, 1.12, t["n"][i], fs=11, c=TEXT2, va="top", linespacing=1.35)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/Bioinformatics{suffix}.png")
