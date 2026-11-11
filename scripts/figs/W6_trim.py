# W5 §1 Read trimming (TrimGalore): 저품질 끝 · 어댑터를 잘라내고, 너무 짧아진 리드는 버림
# 원본: assets/img/part2/W6_trim.png (외부 그림, 영어; 라이브러리·single/paired 단계 포함) → 본문 3가지 기능만 다시 그림
from medfig import *

L = {
    "ko": dict(raw="원시 리드", trim="다듬은 리드", ins="insert", ada="어댑터", low="저품질 염기",
               n=["① 끝의 저품질 염기 잘라냄\n    (Phred Q20 미만)", "② 어댑터 서열 잘라냄",
                  "③ 너무 짧아진 리드는 버림", "문제없는 리드는 그대로"]),
    "en": dict(raw="raw reads", trim="trimmed reads", ins="insert", ada="adapter", low="low-quality bases",
               n=["① cut low-quality 3' end\n    (below Phred Q20)", "② cut adapter sequence",
                  "③ drop reads left too short", "clean reads unchanged"]),
}
INS, ADA, LOW = mix(CAT[2], 0.30), CAT[1], mix(TEXT2, 0.40)
H = 0.26
# 각 리드: (insert 길이, 잘라낼 부분 길이, 잘라낼 부분 색, 버림 여부)
READS = [(1.4, 0.5, LOW, False), (1.1, 0.8, ADA, False), (0.3, 1.6, ADA, True), (1.9, 0, None, False)]
RX, TX, NX = 0.05, 2.6, 4.7        # 원시 · 다듬은 · 설명 칸의 왼쪽 끝


def draw(t):
    fig, ax = new(7.0, 3.45)
    # 범례
    lx = RX
    for c, s in [(INS, t["ins"]), (ADA, t["ada"]), (LOW, t["low"])]:
        box(ax, lx, 3.2, 0.32, 0.18, fc=c, ec="none", r=0.03)
        tx = label(ax, lx + 0.4, 3.29, s, fs=11, c=TEXT2, ha="left")
        fig.canvas.draw()
        lx += 0.4 + tx.get_window_extent().width / fig.dpi + 0.3
    label(ax, RX, 2.78, t["raw"], fs=12, w="bold", ha="left")
    label(ax, TX, 2.78, t["trim"], fs=12, w="bold", ha="left")
    for i, ((li, lc, cc, drop), note) in enumerate(zip(READS, t["n"])):
        y = 2.25 - i * 0.6
        # 원시 리드
        box(ax, RX, y, li, H, fc=INS, ec="none", r=0.03)
        if lc:
            box(ax, RX + li, y, lc, H, fc=cc, ec="none", r=0.03)
        arrow(ax, 2.1, y + H / 2, 2.42, y + H / 2, lw=1.4, ms=10)
        # 다듬은 리드: 잘린 자리는 점선 테두리만
        dash = dict(fc="none", ec=mix(TEXT2, 0.5), lw=0.9, r=0.03, ls=(0, (2, 2)))
        if drop:
            box(ax, TX, y, li + lc, H, **dash)
            label(ax, TX + (li + lc) / 2, y + H / 2, "✗", fs=13, w="bold", c=TEXT2)
        else:
            if lc:
                box(ax, TX + li, y, lc, H, **dash)
            box(ax, TX, y, li, H, fc=INS, ec="none", r=0.03)
        label(ax, NX, y + H / 2, note, fs=11, c=TEXT2 if i == 3 else TEXT, ha="left", linespacing=1.3)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W6_trim{suffix}.png")
