# W7 §4 Design Matrix: 표본 정보 표 → design matrix X, log(μ) = Xβ
# 원본: assets/img/part2/W7_design.png (자체 제작, 기울임꼴 수식) → 다시 그림. 표 값은 원본 그대로.
from medfig import *

# 번역할 글자가 없어 한 파일만 만든다 (KO·EN 페이지가 같은 그림 사용)
T_ = dict(X="design matrix X", code="Case → 1, Control → 0")
COND, BATCH = CAT[0], TEXT2          # condition 열(β₁) / age·batch 열(β₂)
rows = [("Case 1", 60, "Case", 20), ("Case 2", 30, "Case", 40), ("Case 3", 55, "Case", 60),
        ("Control 1", 40, "Control", 1), ("Control 2", 35, "Control", 2), ("Control 3", 50, "Control", 5)]
H, TOP = 0.34, 3.0                    # 행 높이, 머리행 위쪽 y
yc = lambda i: TOP - H * (i + 0.5)     # i = 0 머리행, 1..6 자료행


def bracket(ax, x, y0, y1, side):
    d = 0.07 if side == "l" else -0.07
    ax.plot([x + d, x, x, x + d], [y1, y1, y0, y0], color=TEXT, lw=1.3, zorder=4)


def draw(t):
    fig, ax = new(6.9, 3.5)
    # ── 왼쪽: 표본 정보 표 ──
    ws = [0.9, 0.88, 0.84, 0.66]; xs = np.r_[0.05, 0.05 + np.cumsum(ws)]
    fills = [None, mix(BATCH, 0.14), mix(COND, 0.14), None]
    for j, (head, w) in enumerate(zip(["Sample ID", "Age/Batch", "Condition", "Gene A"], ws)):
        if fills[j]:
            ax.add_patch(mp.Rectangle((xs[j], TOP - 7 * H), w, 6 * H, fc=fills[j], ec="none", zorder=1))
        ax.add_patch(mp.Rectangle((xs[j], TOP - H), w, H, fc=FAINT, ec="none", zorder=1))
        label(ax, xs[j] + w / 2, yc(0), head, fs=11, w="bold")
    for i, r in enumerate(rows, start=1):
        for j, v in enumerate(r):
            label(ax, xs[j] + ws[j] / 2, yc(i), str(v), fs=11)
    for i in range(8):
        ax.plot([xs[0], xs[-1]], [TOP - i * H] * 2, color=LINE if 0 < i < 7 else "#9AA1AB", lw=1, zorder=2)
    arrow(ax, xs[-1] + 0.08, yc(3.5), xs[-1] + 0.38, yc(3.5), color="#9AA1AB", lw=2, ms=16)

    # ── 오른쪽: design matrix X · β ──
    cx = [4.18, 5.07, 5.96]
    heads = [("Intercept", TEXT), ("condition", shade(COND, 0.1)), ("age/batch", shade(BATCH, 0.2))]
    for x, (h, c) in zip(cx, heads):
        label(ax, x, yc(0), h, fs=11, w="bold", c=c)
    for x, f in zip(cx[1:], [mix(COND, 0.14), mix(BATCH, 0.14)]):
        ax.add_patch(mp.Rectangle((x - 0.36, TOP - 7 * H + 0.02), 0.72, 6 * H - 0.04, fc=f, ec="none", zorder=1))
    for i, r in enumerate(rows, start=1):
        for x, v in zip(cx, [1, 1 if r[2] == "Case" else 0, r[1]]):
            label(ax, x, yc(i), str(v), fs=12)
    bracket(ax, 3.74, TOP - 7 * H, TOP - H, "l"); bracket(ax, 6.38, TOP - 7 * H, TOP - H, "r")
    label(ax, 5.07, TOP + 0.17, t["X"], fs=11, c=TEXT2)
    label(ax, xs[2] + ws[2] / 2, TOP - 7 * H - 0.3, t["code"], fs=11, c=TEXT2)
    # 열마다 붙는 계수 (β₁ 강조)
    for x, b in zip(cx, ["β₀", "β₁", "β₂"]):
        y = TOP - 7 * H - 0.3
        arrow(ax, x, TOP - 7 * H - 0.02, x, y + 0.17, color="#9AA1AB", lw=1.2, ms=8)
        if b == "β₁":
            box(ax, x - 0.22, y - 0.15, 0.44, 0.3, fc=ACCENT, ec="none", r=0.05)
        label(ax, x, y, b, fs=12.5, w="bold", c=ON_ACCENT if b == "β₁" else TEXT)
    # 수식
    label(ax, 5.07, TOP - 7 * H - 0.7, "log(μ) = β₀ + β₁·condition + β₂·batch", fs=12.5, w="semibold")
    return fig


save(draw(T_), "../../assets/img/part2/W7_design.png")
