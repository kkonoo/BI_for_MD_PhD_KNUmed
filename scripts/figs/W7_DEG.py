# W7 §1 DEG: 두 조건에서 유전자 X의 발현 분포가 갈라진다 (설명용 가상 자료)
# 원본: assets/img/part2/W7_DEG.png (외부 그림, 25·120은 본문에 없어 뺌) → 다시 그림
from medfig import *
from statistics import NormalDist

L = {
    "ko": dict(x="유전자 X 발현량", gap="평균의 차이", spread="같은 그룹 안에서도 퍼짐"),
    "en": dict(x="Gene X expression", gap="difference in means", spread="spread within each group"),
}
CTRL, CASE = CAT[3], CAT[2]          # W7 전체에서 Control / Case 색
q = np.array([NormalDist().inv_cdf((i + 0.5) / 45) for i in range(45)])   # 설명용: 매끈한 종 모양
vals = {"Control": 3.6 + 1.0 * q, "Case": 7.2 + 1.2 * q}
X0, X1, V0, V1 = 1.05, 5.15, 0.0, 11.0
xi = lambda v: X0 + (X1 - X0) * (v - V0) / (V1 - V0)


def stack(ax, v, y0, c, d=0.105):
    """설명용 점 히스토그램: 값을 칸에 넣고 위로 쌓는다."""
    bw = (V1 - V0) * d / (X1 - X0)
    k = np.floor(np.clip(v, V0, V1 - 1e-6) / bw).astype(int)
    for b in np.unique(k):
        for j in range((k == b).sum()):
            ax.add_patch(mp.Circle((xi((b + 0.5) * bw), y0 + d / 2 + j * d), d * 0.45, fc=c, ec="none", zorder=3))


def draw(t):
    fig, ax = new(5.3, 3.1)
    rows = [("Control", CTRL, 1.85), ("Case", CASE, 0.55)]
    for name, c, y in rows:
        ax.plot([X0, X1], [y, y], color=LINE, lw=1, zorder=1)
        stack(ax, vals[name], y, c)
        label(ax, X0 - 0.12, y + 0.18, name, fs=12.5, w="bold", c=c, ha="right")
        m = xi(vals[name].mean())
        ax.plot([m, m], [y - 0.06, y + 0.7], color=shade(c, 0.2), lw=1.4, ls=(0, (3, 2)), zorder=4)
    # 평균의 차이 (강조)
    m0, m1 = xi(vals["Control"].mean()), xi(vals["Case"].mean())
    arrow(ax, m0, 1.62, m1, 1.62, color=ACCENT_INK, lw=1.8, ms=12, z=5)
    label(ax, (m0 + m1) / 2, 1.47, t["gap"], fs=12, w="bold", c=ACCENT_INK, va="top")
    # 같은 그룹 안의 퍼짐
    label(ax, X1, 2.2, t["spread"], fs=11, c=TEXT2, ha="right")
    # 축
    arrow(ax, X0, 0.38, X1 + 0.12, 0.38, color="#9AA1AB", lw=1, ms=9)
    label(ax, (X0 + X1) / 2, 0.18, t["x"], fs=11, c=TEXT2)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W7_DEG{suffix}.png")
