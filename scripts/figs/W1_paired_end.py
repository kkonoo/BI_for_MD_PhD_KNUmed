# W1 §1 Single-end vs. paired-end: 조각 하나에서 한쪽 끝만 읽나, 양쪽 끝을 다 읽나
# 원본: assets/img/part1/paired_end.png (외부 그림, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(p=["① Single-end (단일 말단)", "② Paired-end (양 말단)"],
               n=["조각 1개 = read 1개", "조각 1개 = read 2개"], frag="cDNA 조각"),
    "en": dict(p=["① Single-end", "② Paired-end"],
               n=["1 fragment = 1 read", "1 fragment = 2 reads"], frag="cDNA fragment"),
}
R1, R2 = CAT[0], CAT[3]          # Read 1 / Read 2
FRAG = mix(TEXT2, 0.3)


def read(ax, x, y, w, c, left=False):
    hw, hl, h = 0.13, 0.13, 0.11
    if left:
        pts = [(x + w, y - h / 2), (x + hl, y - h / 2), (x + hl, y - hw / 2 - 0.02), (x, y),
               (x + hl, y + hw / 2 + 0.02), (x + hl, y + h / 2), (x + w, y + h / 2)]
    else:
        pts = [(x, y - h / 2), (x + w - hl, y - h / 2), (x + w - hl, y - hw / 2 - 0.02), (x + w, y),
               (x + w - hl, y + hw / 2 + 0.02), (x + w - hl, y + h / 2), (x, y + h / 2)]
    ax.add_patch(mp.Polygon(pts, closed=True, fc=c, ec="none", zorder=4))


def draw(t):
    fig, ax = new(6.9, 2.55)
    fw, rw = 2.3, 0.85
    for k in range(2):
        x0 = 0.1 + k * 3.55
        label(ax, x0, 2.35, t["p"][k], fs=12.5, w="bold", ha="left")
        for j, off in enumerate([0.0, 0.45, 0.2]):
            x, y = x0 + off, 1.85 - j * 0.42
            ax.plot([x, x + fw], [y - 0.12, y - 0.12], color=FRAG, lw=4, solid_capstyle="butt", zorder=2)
            read(ax, x, y, rw, R1)
            if k == 1:
                read(ax, x + fw - rw, y, rw, R2, left=True)
                ax.plot([x + rw + 0.05, x + fw - rw - 0.05], [y, y], color=TEXT2, lw=1, ls=(0, (2, 2)))
        label(ax, x0, 0.62, t["n"][k], fs=12.5, w="bold", c=TEXT, ha="left")
    # 범례
    ax.plot([0.1, 0.45], [0.22, 0.22], color=FRAG, lw=4, solid_capstyle="butt")
    label(ax, 0.55, 0.22, t["frag"], fs=11, c=TEXT2, ha="left")
    read(ax, 2.3, 0.22, 0.4, R1); label(ax, 2.8, 0.22, "Read 1", fs=11, c=TEXT2, ha="left")
    read(ax, 3.75, 0.22, 0.4, R2, left=True); label(ax, 4.25, 0.22, "Read 2", fs=11, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/paired_end{suffix}.png")
