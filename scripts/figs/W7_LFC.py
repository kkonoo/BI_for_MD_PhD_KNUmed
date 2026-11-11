# W7 §3-5) LFC: Control은 log μ = β₀, Case는 log μ = β₀ + β₁ → 둘의 간격 β₁ = LFC (새 그림, 숫자 없음)
from medfig import *

# 아래첨자(μ_case)를 Pretendard 바로 쓰기 위해 mathtext 글꼴을 맞춘다 (기울임꼴 없음)
plt.rcParams.update({"mathtext.fontset": "custom", "mathtext.rm": "Pretendard",
                     "mathtext.it": "Pretendard", "mathtext.bf": "Pretendard:bold"})
MU_CASE, MU_CTRL = r"$\mu_{\mathrm{case}}$", r"$\mu_{\mathrm{control}}$"
L = {
    "ko": dict(lfc="= log₂FoldChange (LFC)", gap="두 그룹의 간격"),
    "en": dict(lfc="= log₂FoldChange (LFC)", gap="gap between groups"),
}
CTRL, CASE = CAT[3], CAT[2]          # W7_DEG와 같은 Control / Case 색
AX, XC, XK, Y0, Y1 = 1.15, 2.0, 3.3, 0.95, 2.25     # 축 x, Control x, Case x, β₀ 높이, β₀+β₁ 높이
JIT = [(-0.2, -0.16), (-0.08, 0.12), (0.05, -0.05), (0.17, 0.18), (0.27, -0.13)]


def draw(t):
    fig, ax = new(6.6, 3.0)
    # 축
    arrow(ax, AX, 0.45, AX, 2.85, color="#9AA1AB", lw=1.1, ms=9)
    label(ax, AX, 2.98, "log μ", fs=12, w="semibold", c=TEXT2, va="bottom")
    for x, y, c, name, xv, lv in [(XC, Y0, CTRL, "Control", "X = 0", "β₀"),
                                  (XK, Y1, CASE, "Case", "X = 1", "β₀ + β₁")]:
        ax.plot([AX, XK + 0.75], [y, y], color=mix(c, 0.6), lw=1.2, ls=(0, (3, 2)), zorder=1)
        ax.scatter([x + dx for dx, _ in JIT], [y + dy for _, dy in JIT], s=46, color=c, ec="white",
                   lw=0.8, zorder=3)
        ax.plot([x - 0.38, x + 0.42], [y, y], color=shade(c, 0.2), lw=2.6, zorder=4)
        label(ax, AX - 0.12, y, lv, fs=12.5, w="bold", c=shade(c, 0.1), ha="right")
        label(ax, x + 0.02, 0.3, name, fs=12.5, w="bold", c=c)
        label(ax, x + 0.02, 0.02, xv, fs=11, c=TEXT2)
    # 간격 β₁ (강조)
    xg = XK + 0.75
    arrow(ax, xg, Y0, xg, Y1, color=ACCENT_INK, lw=1.8, ms=12, z=5)
    arrow(ax, xg, Y1, xg, Y0, color=ACCENT_INK, lw=1.8, ms=12, z=5)
    box(ax, xg + 0.14, (Y0 + Y1) / 2 - 0.17, 0.48, 0.34, fc=ACCENT, ec="none", r=0.06)
    label(ax, xg + 0.38, (Y0 + Y1) / 2, "β₁", fs=13, w="bold", c=ON_ACCENT)
    label(ax, xg - 0.12, Y1 + 0.28, t["gap"], fs=11, c=TEXT2, ha="left")
    # 뜻
    label(ax, xg + 0.75, (Y0 + Y1) / 2 + 0.02, f"= log₂({MU_CASE} / {MU_CTRL})", fs=12.5, ha="left",
          va="bottom")
    label(ax, xg + 0.75, (Y0 + Y1) / 2 - 0.08, t["lfc"], fs=12, w="semibold", ha="left", va="top")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W7_LFC{suffix}.png")
