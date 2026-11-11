# W6 §2 PCA vs. MDS: 유전자가 많은 고차원 자료 → 분산이 가장 큰 방향으로 투영 → PC1–PC2 평면에서 Normal / Tumor가 갈라짐
# 원본: assets/img/part2/W6_PCA_theory.png (AI 삽화, 한국어) → 삽화 없이 다시 그림. 점은 설명용 가상 자료.
from medfig import *

L = {
    "ko": dict(p=["① 시료 × 유전자", "② 분산이 가장 큰 방향", "③ PC1–PC2 평면"],
               s="시료", g=["유전자 1", "유전자 2", "유전자 3", "⋮", "유전자 n"],
               n=["유전자 수만큼의 차원\n→ 눈으로 볼 수 없음", "그 방향이 PC1,\n직각인 다음 방향이 PC2",
                  "두 축만 남겨도\nNormal과 Tumor가 갈라짐"]),
    "en": dict(p=["① samples × genes", "② max-variance direction", "③ the PC1–PC2 plane"],
               s="samples", g=["gene 1", "gene 2", "gene 3", "⋮", "gene n"],
               n=["one dimension per gene\n→ too many to see", "that direction is PC1;\nthe next, at a right angle, PC2",
                  "with just two axes,\nNormal and Tumor separate"]),
}
NORM, TUM = CAT[3], CAT[0]
rng = np.random.default_rng(8)
grp = np.r_[np.zeros(10), np.ones(10)]
pc1 = np.where(grp == 0, -1.0, 1.0) + rng.normal(0, 0.32, 20)
pc2 = rng.normal(0, 0.32, 20)
col = [NORM if g == 0 else TUM for g in grp]


def draw(t):
    fig, ax = new(6.9, 3.2)
    X = [0.05, 2.45, 4.85]
    for x, p in zip(X, t["p"]):
        label(ax, x, 3.05, p, fs=12, w="bold", ha="left")
    for x, n in zip(X, t["n"]):
        label(ax, x, 0.5, n, fs=11, c=TEXT2, ha="left", linespacing=1.35)

    # ① 행렬: 열 = 시료(Normal 3, Tumor 3), 행 = 유전자
    gx, cw, rh, top = 0.75, 0.2, 0.22, 2.55
    for j in range(6):
        box(ax, gx + j * cw + 0.01, top + 0.05, cw - 0.02, 0.12, fc=NORM if j < 3 else TUM, ec="none", r=0.02)
    label(ax, gx + 3 * cw, top + 0.32, t["s"], fs=11, c=TEXT2)
    vals = rng.uniform(0.08, 0.3, (5, 6))
    vals[0, 3:] += 0.25; vals[2, :3] += 0.2; vals[4, 3:] += 0.2   # 몇몇 유전자는 그룹 차이
    for i, g in enumerate(t["g"]):
        y = top - (i + 1) * rh
        label(ax, gx - 0.08, y + rh / 2, g, fs=11, c=TEXT2, ha="right")
        if g == "⋮":
            for j in range(6):
                label(ax, gx + (j + 0.5) * cw, y + rh / 2, "⋮", fs=11, c=TEXT2)
            continue
        for j in range(6):
            box(ax, gx + j * cw + 0.01, y + 0.01, cw - 0.02, rh - 0.02, fc=mix(TEXT2, vals[i, j]), ec="none", r=0.02)
    arrow(ax, 2.0, 1.9, 2.35, 1.9)

    # ② 비스듬한 점 구름 + PC1(가장 긴 방향) · PC2
    cx, cy, ang = 3.45, 1.75, np.deg2rad(25)
    u, v = np.array([np.cos(ang), np.sin(ang)]), np.array([-np.sin(ang), np.cos(ang)])
    pts = np.outer(pc1 * 0.5, u) + np.outer(pc2 * 0.5, v) + [cx, cy]
    box(ax, 2.45, 0.85, 2.0, 1.9, fc="none", ec=LINE, r=0.04)
    ax.scatter(pts[:, 0], pts[:, 1], s=22, c=col, lw=0, zorder=4)
    a, b = np.array([cx, cy]) - 0.95 * u, np.array([cx, cy]) + 0.95 * u
    arrow(ax, *a, *b, color=ACCENT_INK, lw=2.2, ms=13, z=5)
    label(ax, b[0] - 0.05, b[1] + 0.17, "PC1", fs=12, w="bold", c=ACCENT_INK)
    c2 = np.array([cx, cy]) + 0.5 * v
    arrow(ax, cx, cy, *c2, color=TEXT2, lw=1.4, ms=10, z=5)
    label(ax, c2[0] - 0.22, c2[1] + 0.02, "PC2", fs=11, w="bold", c=TEXT2)
    arrow(ax, 4.5, 1.9, 4.8, 1.9)

    # ③ PC1–PC2 평면
    ox, oy, W, H = 4.95, 0.95, 1.6, 1.75
    ax.plot([ox, ox + W], [oy, oy], color="#9AA1AB", lw=1)
    ax.plot([ox, ox], [oy, oy + H], color="#9AA1AB", lw=1)
    label(ax, ox + W + 0.06, oy, "PC1", fs=11, w="bold", c=TEXT2, ha="left")
    label(ax, ox - 0.05, oy + H, "PC2", fs=11, w="bold", c=TEXT2, ha="right")
    ax.scatter(ox + W / 2 + 0.05 + pc1 * 0.45, oy + 0.8 + pc2 * 0.5, s=22, c=col, lw=0, zorder=4)
    label(ax, ox + 0.15, oy + 1.55, "Normal", fs=11, w="semibold", c=NORM, ha="left")
    label(ax, ox + W, oy + 1.55, "Tumor", fs=11, w="semibold", c=TUM, ha="right")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W6_PCA_theory{suffix}.png")
