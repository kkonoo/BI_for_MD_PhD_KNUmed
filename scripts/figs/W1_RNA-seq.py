# W1 §2 Bulk RNA-seq 흐름: 시료 → RNA 추출 → cDNA 전환 → 시퀀싱, 단계마다 주의할 점
# 원본: assets/img/part1/RNA-seq.png (자체 제작, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(s=["시료", "RNA 추출", "cDNA 전환", "시퀀싱"],
               n=["연구 설계\n라이브러리 선택\n(total vs. mRNA?\nRibo-zero? 농축?)",
                  "주의!\nRNA는 쉽게 분해됨", "역전사로 만듦", "가장 좋은 방법:\n한 배치로!"]),
    "en": dict(s=["Sample", "RNA\nextraction", "cDNA\nconversion", "Sequencing"],
               n=["Study design\nLibrary selection\n(total vs. mRNA?\nRibo-zero? Enriched?)",
                  "Handle with care!\nRNA is vulnerable", "by reverse\ntranscription", "Best:\na single batch!"]),
}
COL = ramp(4)                    # RNA 추출 = CAT[0], cDNA = CAT[1] (RNA_seq 8단계 그림과 같은 색)


def draw(t):
    fig, ax = new(6.9, 2.55)
    w = 1.75
    for i, (s, n, c) in enumerate(zip(t["s"], t["n"], COL)):
        x = 0.05 + i * (w - 0.04)
        chevron(ax, x, 1.7, w - 0.06, 0.72, fc=c, first=(i == 0))
        label(ax, x + w / 2 + (0 if i == 0 else 0.06), 2.06, s, fs=12.5, w="bold", c="white", linespacing=1.15)
        last = i == 3
        label(ax, x + w / 2, 1.55, n, fs=11.5 if last else 11, w="bold" if last else "regular",
              c=ACCENT_INK if last else TEXT2, va="top", linespacing=1.35)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/RNA-seq{suffix}.png")
