# W1 §1 NGS: 라이브러리 제작(절편화 → 어댑터 연결 → 변성)과 플로우셀 위 브리지 증폭
# 원본: assets/img/part1/library_prep.png (자체 제작, 영어) → 다시 그림
from medfig import *

L = {
    "ko": dict(r1="① 라이브러리 제작", r2="② 브리지 증폭 (플로우셀)",
               a=["절편화", "어댑터 연결", "변성 (한 가닥으로)"],
               b=["올리고에 결합", "다리 모양으로\n휘어 복제", "변성 → 두 가닥", "반복 → 클러스터"],
               ad="어댑터"),
    "en": dict(r1="① Library prep", r2="② Bridge amplification (flow cell)",
               a=["Fragmentation", "Adapter ligation", "Denaturation"],
               b=["binds an oligo", "bends into a\nbridge, copied", "denature → 2 strands", "repeat → cluster"],
               ad="adapter"),
}
INS = mix(TEXT2, 0.45)          # 삽입 DNA
P5, P7 = CAT[0], CAT[3]         # 두 어댑터 끝 (RNA_seq_library_prep의 P5/P7과 같은 색)


def bar(ax, x, y, w, ends=True, lw=5):
    e = 0.22
    if ends:
        ax.plot([x, x + e], [y, y], color=P5, lw=lw, solid_capstyle="butt")
        ax.plot([x + w - e, x + w], [y, y], color=P7, lw=lw, solid_capstyle="butt")
        ax.plot([x + e, x + w - e], [y, y], color=INS, lw=lw, solid_capstyle="butt")
    else:
        ax.plot([x, x + w], [y, y], color=INS, lw=lw, solid_capstyle="butt")


def strand(ax, pts, c_lo, c_hi, lw=3):
    """pts를 따라 그린 한 가닥: 앞 18% = c_lo, 끝 18% = c_hi, 가운데 = 삽입 DNA."""
    pts = np.asarray(pts)
    n = len(pts); k = max(2, int(n * 0.18))
    ax.plot(*pts[:k + 1].T, color=c_lo, lw=lw, solid_capstyle="butt", zorder=4)
    ax.plot(*pts[k:n - k].T, color=INS, lw=lw, solid_capstyle="butt", zorder=3)
    ax.plot(*pts[n - k - 1:].T, color=c_hi, lw=lw, solid_capstyle="butt", zorder=4)


def vline(x, y0, h=0.85):
    return np.c_[np.full(40, x), np.linspace(y0, y0 + h, 40)]


def arch(x1, x2, y0, h=0.75):
    s = np.linspace(0, 1, 60)
    up = np.c_[np.full(20, x1), np.linspace(y0, y0 + h * 0.55, 20)]
    th = np.linspace(np.pi, 0, 40)
    cx, r = (x1 + x2) / 2, (x2 - x1) / 2
    top = np.c_[cx + r * np.cos(th), y0 + h * 0.55 + r * 0.9 * np.sin(th)]
    down = np.c_[np.full(20, x2), np.linspace(y0 + h * 0.55, y0, 20)]
    return np.r_[up, top, down]


def surface(ax, x, y, w, n=6):
    box(ax, x, y - 0.1, w, 0.1, fc=mix(TEXT2, 0.25), ec="none", r=0.02)
    xs = np.linspace(x + 0.1, x + w - 0.1, n)
    for i, xx in enumerate(xs):
        ax.plot([xx, xx], [y, y + 0.12], color=P7 if i % 2 == 0 else P5, lw=2.2, solid_capstyle="butt")
    return xs


def draw(t):
    fig, ax = new(6.9, 4.3)
    # ── ① 라이브러리 제작 ──
    label(ax, 0.05, 4.15, t["r1"], fs=12.5, w="bold", ha="left")
    y = 3.35
    # 절편화
    for x0, w in [(0.1, 0.4), (0.56, 0.3), (0.92, 0.45), (1.43, 0.3)]:
        bar(ax, x0, y + 0.1, w, ends=False)
        bar(ax, x0, y - 0.04, w, ends=False)
    arrow(ax, 1.85, y + 0.03, 2.2, y + 0.03)
    # 어댑터 연결 (두 가닥)
    bar(ax, 2.35, y + 0.1, 1.85); bar(ax, 2.35, y - 0.04, 1.85)
    label(ax, 2.35, y + 0.33, t["ad"], fs=11, c=P5, ha="left")
    label(ax, 4.2, y + 0.33, t["ad"], fs=11, c=shade(P7, 0.2), ha="right")
    arrow(ax, 4.35, y + 0.03, 4.7, y + 0.03)
    # 변성 (한 가닥씩 떨어짐)
    bar(ax, 4.85, y + 0.2, 1.85); bar(ax, 4.85, y - 0.14, 1.85)
    for (cx, s) in zip([0.85, 3.27, 5.77], t["a"]):
        label(ax, cx, y - 0.48, s, fs=11.5, w="semibold")
    ax.plot([0.05, 6.85], [2.5, 2.5], color=LINE, lw=1)

    # ── ② 브리지 증폭 ──
    label(ax, 0.05, 2.25, t["r2"], fs=12.5, w="bold", ha="left")
    w, gap, y0 = 1.42, 0.37, 0.95
    for i in range(4):
        x = 0.1 + i * (w + gap)
        xs = surface(ax, x, y0, w)
        if i == 0:      # 한 가닥이 같은 색 올리고에 붙음
            strand(ax, vline(xs[2], y0 + 0.12), P7, P5)
        elif i == 1:    # 끝이 휘어 이웃 P5 올리고에 붙고(다리), 그 올리고에서 복제 가닥이 자람
            strand(ax, arch(xs[1], xs[4], y0 + 0.12)[::-1], P7, P5)
            strand(ax, arch(xs[1] + 0.07, xs[4] - 0.07, y0 + 0.12, h=0.62), P5, P7, lw=2.4)
        elif i == 2:    # 변성 → 두 가닥이 따로 섬
            strand(ax, vline(xs[2], y0 + 0.12), P7, P5)
            strand(ax, vline(xs[3], y0 + 0.12), P5, P7)
        else:           # 반복 → 같은 서열의 클러스터
            for j, xx in enumerate(xs):
                strand(ax, vline(xx, y0 + 0.12, 0.78 + 0.07 * (j % 2)), *((P7, P5) if j % 2 == 0 else (P5, P7)),
                       lw=2.4)
        if i < 3:
            arrow(ax, x + w + 0.07, y0 + 0.45, x + w + gap - 0.07, y0 + 0.45)
        label(ax, x + w / 2, y0 - 0.25, t["b"][i], fs=11, c=TEXT, va="top", linespacing=1.3)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/library_prep{suffix}.png")
