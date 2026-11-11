# W1 §1 NGS: 라이브러리 제작 8단계 (Illumina Stranded mRNA Prep)
# 원본: assets/img/part1/RNA_seq.png (Illumina 그림, 영어) → 다시 그림. 원본의 '6.5 hours'는 본문에 없어 뺌.
from medfig import *

L = {
    "ko": dict(s=["mRNA 선별", "RNA 절편화 · 변성", "cDNA 합성", "A-tailing (A 꼬리 붙이기)",
                  "어댑터 연결 (ligation)", "PCR 증폭", "정량 · 농도 맞추기", "시퀀싱 준비 완료"],
               g=["RNA", "cDNA"]),
    "en": dict(s=["mRNA selection", "RNA fragmentation and denaturation", "cDNA synthesis", "A-tailing",
                  "Ligation", "PCR amplification", "Quantification and normalization", "Ready for sequencing"],
               g=["RNA", "cDNA"]),
}
COL = [CAT[0]] * 2 + [CAT[1]] * 5 + [CAT[2]]          # RNA 단계 / cDNA 단계 / 시퀀싱


def draw(t):
    fig, ax = new(4.4, 4.5)
    dy, top, cx = 0.54, 4.2, 0.95
    ys = [top - i * dy for i in range(8)]
    ax.plot([cx, cx], [ys[-1], ys[0]], color=LINE, lw=2, zorder=1)
    for i, (y, s, c) in enumerate(zip(ys, t["s"], COL)):
        num(ax, cx, y, i + 1, fc=c, r=0.17, fs=12)
        label(ax, cx + 0.3, y, s, fs=12, w="semibold" if i == 7 else "regular",
              c=shade(c, 0.1), ha="left")
    # 묶음 표시: 1–2 = RNA, 3–7 = cDNA
    for (a, b), g, c in [((0, 1), t["g"][0], CAT[0]), ((2, 6), t["g"][1], CAT[1])]:
        y1, y2 = ys[a] + 0.15, ys[b] - 0.15
        ax.plot([0.5, 0.42, 0.42, 0.5], [y1, y1, y2, y2], color=mix(c, 0.6), lw=1.4)
        label(ax, 0.3, (y1 + y2) / 2, g, fs=11, w="semibold", c=c, rotation=90)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/RNA_seq{suffix}.png")
