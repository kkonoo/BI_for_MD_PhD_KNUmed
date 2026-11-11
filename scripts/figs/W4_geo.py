# W4 §1 "우리가 시작하는 지점": SRA(FASTQ) → 정렬(서버) → count matrix. 우리는 count matrix부터 시작
# 원본: assets/img/part1/W4_geo.png → 다시 그림
from medfig import *

L = {
    "ko": dict(raw="원본 데이터", aln="정렬", srv="서버에서 이미 처리됨",
               start="우리의 시작점"),
    "en": dict(raw="raw data", aln="Alignment", srv="already done on a server",
               start="where we start"),
}


def draw(t):
    fig, ax = new(6.6, 1.75)
    y, h, w = 0.6, 0.8, 1.75
    xs = [0.0, 2.4, 4.8]
    # ① SRA (FASTQ)
    box(ax, xs[0], y, w, h, fc=mix(CAT[0], 0.12), ec=mix(CAT[0], 0.4))
    label(ax, xs[0] + w / 2, y + h / 2, "SRA (FASTQ)", fs=13, w="bold", c=shade(CAT[0], 0.2))
    label(ax, xs[0] + w / 2, y - 0.25, t["raw"], fs=11.5, c=TEXT)
    # ② 정렬: 흐리게, 점선 테두리
    box(ax, xs[1], y, w, h, fc=FAINT, ec="#9AA1AB", ls=(0, (3, 2)))
    label(ax, xs[1] + w / 2, y + h / 2, t["aln"], fs=13, w="bold", c=TEXT2)
    label(ax, xs[1] + w / 2, y - 0.25, t["srv"], fs=11, c=TEXT2)
    # ③ count matrix: 강조(그림당 하나)
    box(ax, xs[2], y, w, h, fc=ACCENT, ec="none")
    label(ax, xs[2] + w / 2, y + h / 2, "Count matrix", fs=13, w="bold", c=ON_ACCENT)
    label(ax, xs[2] + w / 2, y - 0.25, t["start"], fs=12.5, w="bold", c=ACCENT_INK)
    # 화살표: FASTQ → 정렬은 우리가 하지 않음(✗), 정렬 → count matrix
    am = y + h / 2
    arrow(ax, xs[0] + w + 0.12, am, xs[1] - 0.12, am, color="#C4C9D0", lw=1.6)
    label(ax, (xs[0] + w + xs[1]) / 2, am + 0.01, "✗", fs=18, w="bold", c=TEXT2)
    arrow(ax, xs[1] + w + 0.12, am, xs[2] - 0.12, am, color="#9AA1AB", lw=1.8)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/W4_geo{suffix}.png")
