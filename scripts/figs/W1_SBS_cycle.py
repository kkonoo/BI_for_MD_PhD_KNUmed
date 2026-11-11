# W1 §1 합성에 의한 염기서열 분석(SBS): 한 사이클 = 형광 dNTP 결합 → 촬영 → 형광·차단기 제거 → 다음 사이클
# 원본: SBS0.png · SBS1.png · SBS00.jpg · SBS2.png (동영상 캡처 4장) → 새 그림 하나로 대체
from medfig import *

L = {
    "ko": dict(s=["형광 dNTP 결합", "촬영", "형광 · 차단기 제거", "다음 사이클"],
               n=["차단기 때문에\n한 번에 1개만", "색으로\n염기 판독", "다시 이어 붙일\n수 있게 됨", "같은 과정을\n반복"],
               tmpl="주형", new="새 가닥", blk="차단기", ny=0.86),
    "en": dict(s=["Add fluorescent\ndNTP", "Image", "Remove dye\nand blocker", "Next cycle"],
               n=["blocker: only one\nbase per cycle", "color tells\nthe base", "strand can be\nextended again", "repeat the\nsame steps"],
               tmpl="template", new="new strand", blk="blocker", ny=0.62),
}
BASE = {"A": CAT[0], "C": CAT[1], "G": CAT[2], "T": CAT[3]}     # sanger_seq와 같은 염기 색
TMPL = "TACGT"
COMP = {"A": "T", "T": "A", "C": "G", "G": "C"}
R, DY = 0.13, 0.34


def nt(ax, x, y, b, ec=LINE, fc="white", bold=False):
    ax.add_patch(mp.Circle((x, y), R, fc=fc, ec=ec, lw=1.4, zorder=3))
    label(ax, x, y, b, fs=11.5, w="bold" if bold else "regular", c=TEXT)


def dye(ax, x, y, b, glow=False):
    if glow:
        ax.add_patch(mp.Circle((x, y), 0.17, fc=mix(BASE[b], 0.25), ec="none", zorder=2))
    ax.add_patch(mp.Circle((x, y), 0.075, fc=BASE[b], ec="none", zorder=4))


def blocker(ax, x, y):
    box(ax, x - 0.07, y - 0.05, 0.14, 0.1, fc=TEXT2, ec="none", r=0.02, z=4)


def panel(ax, x0, top, n_done, new=None, glow=False, gone=False):
    xt, xn = x0 + 0.35, x0 + 0.7
    ax.plot([xt, xt], [top + 0.3, top - 4 * DY], color=LINE, lw=1, zorder=1)
    for i, b in enumerate(TMPL):
        nt(ax, xt, top - i * DY, b)
    for i in range(n_done):
        nt(ax, xn, top - i * DY, COMP[TMPL[i]])
    if new is not None:                      # 방금 붙은 염기: 형광 + 차단기
        b = COMP[TMPL[new]]
        y = top - new * DY
        nt(ax, xn, y, b, ec=BASE[b], bold=True)
        dye(ax, xn + 0.24, y, b, glow=glow)
        blocker(ax, xn, y - R - 0.04)
    if gone is not False:                    # 떨어져 나간 형광과 차단기
        b = COMP[TMPL[gone]]
        y = top - gone * DY
        arrow(ax, xn + 0.18, y - 0.05, xn + 0.5, y - 0.35, color=mix(TEXT2, 0.6), lw=1.2, ms=9)
        dye(ax, xn + 0.62, y - 0.42, b)
        blocker(ax, xn + 0.62, y - 0.62)


def draw(t):
    fig, ax = new(6.9, 3.6)
    pw, top = 1.73, 3.0
    for k in range(4):
        x0 = 0.05 + k * pw
        if k == 0:
            panel(ax, x0, top, 2, new=2)
        elif k == 1:
            panel(ax, x0, top, 2, new=2, glow=True)
            # 촬영: 형광 신호 → 염기
            label(ax, x0 + 1.1, top - 2 * DY + 0.2, "→ G", fs=12, w="bold", c=BASE["G"], ha="left")
        elif k == 2:
            panel(ax, x0, top, 3, gone=2)
        else:
            panel(ax, x0, top, 3, new=3)
        label(ax, x0 + 0.05, 1.2, "①②③④"[k] + " " + t["s"][k], fs=12, w="bold", ha="left", va="top",
              linespacing=1.2)
        label(ax, x0 + 0.05, t["ny"], t["n"][k], fs=11, c=TEXT2, ha="left", va="top", linespacing=1.3)
        if k < 3:
            arrow(ax, x0 + pw - 0.2, top - 3.5 * DY, x0 + pw + 0.08, top - 3.5 * DY, color="#9AA1AB")
    # 이름표 (첫 칸만)
    label(ax, 0.4, top + 0.42, t["tmpl"], fs=11, c=TEXT2)
    label(ax, 0.86, top + 0.42, t["new"], fs=11, c=TEXT2, ha="left")
    label(ax, 0.9, top - 2 * DY - 0.25, t["blk"], fs=11, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/SBS_cycle{suffix}.png")
