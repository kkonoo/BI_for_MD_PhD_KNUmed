# W1 §1 NGS: 생어 염기서열 분석 — dNTP와 ddNTP(3′-OH 없음), 형광 ddNTP에서 멈춘 조각들
# 원본: assets/img/part1/sanger_seq.png (외부 그림 조합, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(d="dNTP: 3′-OH 있음\n→ 다음 염기가 붙음", dd="ddNTP: 3′-OH 없음\n→ 합성이 멈춤",
               tmpl="주형", frag="형광 ddNTP에서 멈춘 조각들"),
    "en": dict(d="dNTP: has 3′-OH\n→ next base can attach", dd="ddNTP: no 3′-OH\n→ synthesis stops",
               tmpl="template", frag="fragments ending in a fluorescent ddNTP"),
}
BASE = {"A": CAT[0], "C": CAT[1], "G": CAT[2], "T": CAT[3]}     # 염기 색 (SBS_cycle과 같음)
GREY = mix(TEXT2, 0.55)


def nucleotide(ax, x0, y0, three, key, t_note):
    """인산 3개 + 당(오각형) + 염기. three = 3′ 자리의 원자('OH' 또는 'H')."""
    cx, cy, r = x0 + 1.75, y0, 0.36
    ang = np.deg2rad([90, 18, -54, -126, 162])          # O, C1′, C2′, C3′, C4′
    v = np.c_[cx + r * np.cos(ang), cy + r * np.sin(ang)]
    ax.add_patch(mp.Polygon(v, closed=True, fc=mix(TEXT2, 0.10), ec=TEXT2, lw=1.4, zorder=2))
    label(ax, *v[0] + [0, 0.13], "O", fs=11, c=TEXT2)
    # 인산 사슬 → C4′
    px = [x0 + 0.15, x0 + 0.5, x0 + 0.85]
    ax.plot([px[0], v[4][0], v[4][0]], [y0 + 0.45, y0 + 0.45, v[4][1]], color=GREY, lw=1.4, zorder=1)
    for x in px:
        ax.add_patch(mp.Circle((x, y0 + 0.45), 0.13, fc=GREY, ec="none", zorder=3))
        label(ax, x, y0 + 0.45, "P", fs=11, w="bold", c="white")
    # 염기 (C1′)
    ax.plot([v[1][0], v[1][0] + 0.25], [v[1][1], v[1][1] + 0.2], color=TEXT2, lw=1.4)
    label(ax, v[1][0] + 0.28, v[1][1] + 0.3, "Base", fs=11, c=TEXT2, ha="left")
    # 3′ 자리
    ax.plot([v[3][0], v[3][0]], [v[3][1], v[3][1] - 0.22], color=TEXT2, lw=1.4)
    label(ax, v[3][0] - 0.1, v[3][1] + 0.02, "3′", fs=11, c=TEXT2, ha="right")
    if key:
        pill(ax, v[3][0], v[3][1] - 0.38, three, fc=ACCENT, tc=ON_ACCENT, fs=12, h=0.28, padx=0.1)
    else:
        label(ax, v[3][0], v[3][1] - 0.38, three, fs=12, w="bold")
    label(ax, x0 + 0.05, y0 - 0.88, t_note, fs=11.5 if key else 11, w="semibold" if key else "regular",
          c=TEXT, ha="left", va="top", linespacing=1.35)


def draw(t):
    fig, ax = new(6.9, 4.1)
    nucleotide(ax, 0.05, 3.45, "OH", False, t["d"])
    nucleotide(ax, 0.05, 1.35, "H", True, t["dd"])
    ax.plot([2.85, 2.85], [0.1, 4.0], color=LINE, lw=1)
    # 오른쪽: 사다리
    tmpl = "AGCTTCAGTC"
    comp = "TCGAAGTCAG"                                  # 3′→5′로 쓴 상보 가닥
    dx, x0, top = 0.27, 3.6, 3.75
    xs = [x0 + i * dx for i in range(10)]
    label(ax, x0 - 0.2, top, "5′", fs=12, w="bold", c=TEXT2, ha="right")
    for x, b in zip(xs, tmpl):
        label(ax, x, top, b, fs=12.5, w="bold")
    label(ax, xs[-1] + 0.2, top, "3′", fs=12, w="bold", c=TEXT2, ha="left")
    label(ax, x0 - 0.2, top + 0.34, t["tmpl"], fs=11, c=TEXT2, ha="left")
    ax.plot([x0 - 0.1, xs[-1] + 0.1], [top - 0.2, top - 0.2], color=LINE, lw=1)
    label(ax, x0 - 0.2, top - 0.42, t["frag"], fs=11, c=TEXT2, ha="left")
    for k in range(1, 11):
        y = top - 0.5 - k * 0.29
        for j in range(10 - k, 10):
            b = comp[j]
            end = j == 10 - k
            label(ax, xs[j], y, b, fs=12.5, w="bold" if end else "regular", c=BASE[b] if end else TEXT)
            if end:
                ax.add_patch(mp.Circle((xs[j] + 0.1, y + 0.1), 0.035, fc=BASE[b], ec="none", zorder=5))
        label(ax, xs[-1] + 0.2, y, "5′", fs=11, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/sanger_seq{suffix}.png")
