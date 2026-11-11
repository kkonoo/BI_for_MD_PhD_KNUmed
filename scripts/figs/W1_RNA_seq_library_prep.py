# W1 §1 NGS 라이브러리 분자: 어댑터(P5/P7 · Index · 프라이머 자리) + 삽입체
# 원본: assets/img/part1/RNA_seq_library_prep.png (Illumina 그림, 영어) → 본문 글머리표에 맞춰 분자 하나만 다시 그림
from medfig import *

L = {
    "ko": dict(ins="삽입체 (cDNA 조각)", ad="어댑터",
               leg=[("P5 / P7", "플로우셀에 결합"),
                    ("Index", "시료 식별자 (6–12 nt), 다중화(multiplexing)용"),
                    ("Rd1 / Rd2 SP", "시퀀싱 프라이머가 붙는 자리")]),
    "en": dict(ins="insert (cDNA fragment)", ad="adapter",
               leg=[("P5 / P7", "binds to the flow cell"),
                    ("Index", "sample identifier (6–12 nt), for multiplexing"),
                    ("Rd1 / Rd2 SP", "where the sequencing primer binds")]),
}
FC, IDX, PRM, INS = CAT[0], CAT[2], CAT[1], mix(TEXT2, 0.3)     # P5 · Index · primer · 삽입체
P7 = CAT[3]                                                     # library_prep의 두 어댑터 끝과 같은 색


def draw(t):
    fig, ax = new(6.9, 2.75)
    segs = [("P5", 0.6, FC), ("Index2", 0.78, IDX), ("Rd1 SP", 0.78, PRM), (t["ins"], 2.18, INS),
            ("Rd2 SP", 0.78, PRM), ("Index1", 0.78, IDX), ("P7", 0.6, P7)]
    x, y, h = 0.1, 1.55, 0.5
    edges = []
    for name, w, c in segs:
        box(ax, x, y, w, h, fc=c, ec="white", lw=1.5, r=0.03)
        label(ax, x + w / 2, y + h / 2, name, fs=11.5, w="bold", c=on(c))
        edges.append((x, x + w)); x += w
    # 위: 어댑터 / 삽입체 / 어댑터 묶음
    for a, b in [(edges[0][0], edges[2][1]), (edges[4][0], edges[6][1])]:
        ax.plot([a + 0.03, a + 0.03, b - 0.03, b - 0.03], [y + h + 0.1, y + h + 0.18, y + h + 0.18, y + h + 0.1],
                color=TEXT2, lw=1.2)
        label(ax, (a + b) / 2, y + h + 0.36, t["ad"], fs=12, w="semibold", c=TEXT2)
    # 아래: 본문 글머리표와 같은 설명
    for i, ((k, v), c) in enumerate(zip(t["leg"], [FC, IDX, PRM])):
        yy = 1.08 - i * 0.36
        if i == 0:
            box(ax, 0.15, yy - 0.09, 0.09, 0.18, fc=FC, ec="none", r=0.02)
            box(ax, 0.26, yy - 0.09, 0.09, 0.18, fc=P7, ec="none", r=0.02)
        else:
            box(ax, 0.15, yy - 0.09, 0.2, 0.18, fc=c, ec="none", r=0.02)
        label(ax, 0.48, yy, k, fs=11.5, w="bold", ha="left")
        label(ax, 1.85, yy, v, fs=11, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/RNA_seq_library_prep{suffix}.png")
