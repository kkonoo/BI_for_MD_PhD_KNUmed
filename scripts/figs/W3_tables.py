# W3 dplyr / tidyr 동사 그림 14개: 한 가지 표 모양으로 다시 그림
# 원본: assets/img/part1/W3_*.png (dplyr·tidyr 치트시트 / R4DS 그림 계열)
# 표에는 열 이름과 값만 있어 번역할 글자가 없음 → 파일 하나를 KO·EN 페이지가 같이 씀
from medfig import *

OUT = "../../assets/img/part1/"
HEAD, BODY = TEXT2, LINE        # 중립 머리칸 / 몸칸
XC, YC = TEXT2, CAT[1]          # join: x 표 / y 표에서 온 값
P1, P2 = CAT[3], CAT[0]         # tidyr: 앞 조각(cases, century) / 뒤 조각(pop, year)
SEL = CAT[0]                    # dplyr 동사가 고른 열·행
NEW = CAT[2]                    # mutate 새 열 · summarise 결과
GAP = 0.03                      # 칸 사이 흰 틈(인치)


def tint(c):
    return mix(c, 0.32)


def cell(ax, x, y, w, h, fc, text="", fs=11, bold=False):
    box(ax, x + GAP / 2, y + GAP / 2, w - GAP, h - GAP, fc=fc, ec="none", r=0.02)
    if text:
        c = TEXT2 if text == "NA" else on(fc)
        label(ax, x + w / 2, y + h / 2, text, fs=fs, w="bold" if bold else "regular", c=c)


def table(ax, x, top, head, body, cw, rh, hfc, bfc, fs=11):
    """head: 열 이름, body: 행 목록, hfc: 열별 머리칸 색, bfc(i, j): 몸칸 색. top = 위쪽 y."""
    cw = cw if isinstance(cw, (list, tuple)) else [cw] * len(head)
    xs = np.r_[x, x + np.cumsum(cw)]
    for j, h in enumerate(head):
        cell(ax, xs[j], top - rh, cw[j], rh, hfc[j], h, fs, bold=True)
    for i, row in enumerate(body):
        for j, v in enumerate(row):
            cell(ax, xs[j], top - rh * (i + 2), cw[j], rh, bfc(i, j), v, fs)
    return xs[-1], top - rh * (len(body) + 1)


def grid(ax, x, top, ncol, nrow, hfc, bfc, cw=0.3, rh=0.2):
    """글자 없는 아이콘 표."""
    return table(ax, x, top, [""] * ncol, [[""] * ncol] * nrow, cw, rh, hfc, bfc)


def go(ax, x1, x2, y):
    arrow(ax, x1, y, x2, y, color="#9AA1AB", lw=1.8, ms=13)


# ── dplyr 핵심 동사 5개 (아이콘) ─────────────────────────────────────────────
def select():
    fig, ax = new(2.1, 1.3)
    pick = (0, 2)
    grid(ax, 0, 1.2, 3, 5, [SEL if j in pick else HEAD for j in range(3)],
         lambda i, j: tint(SEL) if j in pick else BODY)
    go(ax, 0.98, 1.35, 0.7)
    grid(ax, 1.45, 1.2, 2, 5, [SEL] * 2, lambda i, j: tint(SEL))
    return fig


def filter_():
    fig, ax = new(2.4, 1.3)
    pick = (1, 3)
    grid(ax, 0, 1.2, 3, 5, [HEAD] * 3, lambda i, j: tint(SEL) if i in pick else BODY)
    go(ax, 0.98, 1.35, 0.7)
    grid(ax, 1.45, 1.0, 3, 2, [HEAD] * 3, lambda i, j: tint(SEL))
    return fig


def mutate():
    fig, ax = new(2.7, 1.3)
    grid(ax, 0, 1.2, 3, 5, [HEAD] * 3, lambda i, j: BODY)
    go(ax, 0.98, 1.35, 0.7)
    grid(ax, 1.45, 1.2, 4, 5, [HEAD] * 3 + [NEW], lambda i, j: tint(NEW) if j == 3 else BODY)
    return fig


def arrange():
    fig, ax = new(2.4, 1.3)
    lv = [0.55, 0.15, 0.85, 0.35, 0.7]                    # 정렬 기준 값의 크기(진할수록 큼)
    sl = sorted(lv, reverse=True)                          # desc(): 큰 값이 위로
    grid(ax, 0, 1.2, 3, 5, [SEL, HEAD, HEAD], lambda i, j: mix(SEL, lv[i]) if j == 0 else BODY)
    go(ax, 0.98, 1.35, 0.7)
    grid(ax, 1.45, 1.2, 3, 5, [SEL, HEAD, HEAD], lambda i, j: mix(SEL, sl[i]) if j == 0 else BODY)
    return fig


def group_by():
    fig, ax = new(3.6, 2.25)
    G = [CAT[0], CAT[1], CAT[3]]
    g = [0, 1, 0, 2, 1, 2, 0]                              # 행마다 속한 그룹
    grid(ax, 0, 1.92, 3, 7, [HEAD] * 3,
         lambda i, j: tint(G[g[i]]) if j == 0 else BODY)
    go(ax, 1.0, 1.35, 1.12)
    top = 2.22
    for k in range(3):                                     # 그룹별로 나눈 조각
        n = g.count(k)
        grid(ax, 1.45, top, 3, n, [HEAD] * 3,
             lambda i, j, k=k: tint(G[k]) if j == 0 else BODY)
        top -= 0.2 * (n + 1) + 0.1
    go(ax, 2.45, 2.8, 1.12)
    grid(ax, 2.9, 1.52, 2, 3, [HEAD, NEW],                 # summarise: 그룹당 한 행
         lambda i, j: tint(G[i]) if j == 0 else tint(NEW))
    return fig


# ── join ─────────────────────────────────────────────────────────────────────
JH = ["A", "B", "C", "D"]
CW, RH, JFS = 0.42, 0.34, 13


def jtable(ax, x, top, rows, src):
    """src: 열마다 'x' 또는 'y' (행마다 다르면 리스트)."""
    col = lambda s: XC if s == "x" else YC
    hfc = [col(s if isinstance(s, str) else "x") for s in src]
    def bfc(i, j):
        if rows[i][j] == "NA":
            return FAINT
        s = src[j] if isinstance(src[j], str) else src[j][i]
        return BODY if s == "x" else tint(YC)
    return table(ax, x, top, JH[:len(rows[0])], rows, CW, RH, hfc, bfc, fs=JFS)


def join():
    fig, ax = new(3.5, 1.9)
    label(ax, 0.05, 1.75, "x", fs=15, w="bold", c=TEXT2, ha="left")
    label(ax, 2.05, 1.75, "y", fs=15, w="bold", c=shade(YC, 0.1), ha="left")
    table(ax, 0, 1.5, ["A", "B", "C"], [["a", "t", "1"], ["b", "u", "2"], ["c", "v", "3"]],
          CW, RH, [XC] * 3, lambda i, j: BODY, fs=JFS)
    label(ax, 1.65, 0.97, "+", fs=24, w="bold", c="#9AA1AB")
    table(ax, 2.05, 1.5, ["A", "B", "D"], [["a", "t", "3"], ["b", "u", "2"], ["d", "w", "1"]],
          CW, RH, [YC] * 3, lambda i, j: tint(YC), fs=JFS)
    return fig


def left():
    fig, ax = new(1.8, 1.45)
    jtable(ax, 0, 1.4, [["a", "t", "1", "3"], ["b", "u", "2", "2"], ["c", "v", "3", "NA"]],
           ["x", "x", "x", "y"])
    return fig


def right():
    fig, ax = new(1.8, 1.45)
    jtable(ax, 0, 1.4, [["a", "t", "1", "3"], ["b", "u", "2", "2"], ["d", "w", "NA", "1"]],
           ["y", "y", "x", "y"])
    return fig


def inner():
    fig, ax = new(1.8, 1.1)
    jtable(ax, 0, 1.05, [["a", "t", "1", "3"], ["b", "u", "2", "2"]], ["x", "x", "x", "y"])
    return fig


def full():
    fig, ax = new(1.8, 1.8)
    ab = ["x", "x", "x", "y"]
    jtable(ax, 0, 1.75, [["a", "t", "1", "3"], ["b", "u", "2", "2"], ["c", "v", "3", "NA"],
                         ["d", "w", "NA", "1"]], [ab, ab, "x", "y"])
    return fig


# ── tidyr ────────────────────────────────────────────────────────────────────
TW, TR = 0.72, 0.27              # 칸 너비·높이


def pivot_longer():
    # 원본 그림은 rate "0.7K/19M"을 행으로 쪼개는 그림(separate_rows)이라 pivot_longer가 아님.
    # 같은 계열 값(R4DS table4a: cases)으로 wide → long을 그림.
    fig, ax = new(5.25, 2.05)
    Y = CAT[2]                                             # 열 이름 1999 · 2000 → year 값
    wide = [["A", "0.7K", "2K"], ["B", "37K", "80K"], ["C", "212K", "213K"]]
    table(ax, 0, 1.6, ["country", "1999", "2000"], wide, TW, TR, [HEAD, Y, Y],
          lambda i, j: tint(P1) if j else BODY)
    go(ax, 2.35, 2.85, 1.05)
    long = [[c, y, v] for c, a, b in wide for y, v in (("1999", a), ("2000", b))]
    table(ax, 3.0, 1.95, ["country", "year", "cases"], long, TW, TR, [HEAD, Y, P1],
          lambda i, j: [BODY, tint(Y), tint(P1)][j])
    return fig


def pivot_wider():
    fig, ax = new(6.6, 3.65)
    rows = [("A", "1999", "0.7K", "19M"), ("A", "2000", "2K", "20M"), ("B", "1999", "37K", "172M"),
            ("B", "2000", "80K", "174M"), ("C", "1999", "212K", "1T"), ("C", "2000", "213K", "1T")]
    long = [[c, y, t, v] for c, y, a, b in rows for t, v in (("cases", a), ("pop", b))]
    K = lambda t: P1 if t == "cases" else P2
    table(ax, 0, 3.55, ["country", "year", "type", "count"], long, TW, TR, [HEAD] * 4,
          lambda i, j: tint(K(long[i][2])) if j >= 2 else BODY)
    go(ax, 3.05, 3.5, 3.15)
    table(ax, 3.7, 3.55, ["country", "year", "cases", "pop"], [list(r) for r in rows], TW, TR,
          [HEAD, HEAD, P1, P2], lambda i, j: [BODY, BODY, tint(P1), tint(P2)][j])
    return fig


def split_table(ax, x, top, head, rows, cws, hfc, split_col, parts):
    """split_col 열은 두 조각(앞 P1 · 뒤 P2)으로 칠한 칸."""
    xs = np.r_[x, x + np.cumsum(cws)]
    for j, h in enumerate(head):
        cell(ax, xs[j], top - TR, cws[j], TR, hfc[j], h, bold=True)
    for i, row in enumerate(rows):
        y = top - TR * (i + 2)
        for j, v in enumerate(row):
            if j != split_col:
                cell(ax, xs[j], y, cws[j], TR, BODY, v)
        a, b, sep = parts[i]
        w = cws[split_col] / 2
        x0 = xs[split_col]
        cell(ax, x0, y, w + GAP / 2, TR, tint(P1))
        cell(ax, x0 + w - GAP / 2, y, w + GAP / 2, TR, tint(P2))
        if sep:
            label(ax, x0 + w - 0.04, y + TR / 2, a, ha="right")
            label(ax, x0 + w, y + TR / 2, sep, c=TEXT2)
            label(ax, x0 + w + 0.04, y + TR / 2, b, ha="left")
        else:                                              # unite: 붙여 쓴 한 값
            label(ax, x0 + w, y + TR / 2, a, ha="right")
            label(ax, x0 + w, y + TR / 2, b, ha="left")
    return xs[-1]


def separate():
    fig, ax = new(6.4, 1.45)
    vals = [("A", "1999", "0.7K", "19M"), ("A", "2000", "2K", "20M"),
            ("B", "1999", "37K", "172M"), ("B", "2000", "80K", "174M")]
    split_table(ax, 0, 1.4, ["country", "year", "rate"], [[c, y, ""] for c, y, _, _ in vals],
                [TW, TW, 1.2], [HEAD, HEAD, HEAD], 2, [(a, b, "/") for _, _, a, b in vals])
    go(ax, 2.8, 3.25, 0.72)
    table(ax, 3.4, 1.4, ["country", "year", "cases", "pop"], [list(v) for v in vals], TW * 0.86 + 0.06,
          TR, [HEAD, HEAD, P1, P2], lambda i, j: [BODY, BODY, tint(P1), tint(P2)][j])
    return fig


def unite():
    fig, ax = new(4.6, 1.45)
    vals = [("A", "19", "99"), ("A", "20", "00"), ("B", "19", "99"), ("B", "20", "00")]
    table(ax, 0, 1.4, ["country", "century", "year"], [list(v) for v in vals], TW, TR,
          [HEAD, P1, P2], lambda i, j: [BODY, tint(P1), tint(P2)][j])
    go(ax, 2.35, 2.8, 0.72)
    split_table(ax, 2.95, 1.4, ["country", "year"], [[c, ""] for c, _, _ in vals], [TW, TW],
                [HEAD, HEAD], 1, [(a, b, "") for _, a, b in vals])
    return fig


for name, fn in [("W3_select", select), ("W3_fjilter", filter_), ("W3_mutate", mutate),
                 ("W3_arrange", arrange), ("W3_group_by", group_by), ("W3_join", join),
                 ("W3_left", left), ("W3_right", right), ("W3_inner", inner), ("W3_full", full),
                 ("W3_pivet_long", pivot_longer), ("W3_pivot_wider", pivot_wider),
                 ("W3_separate", separate), ("W3_unite", unite)]:
    save(fn(), OUT + name + ".png")
