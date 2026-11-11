# W10 §1 기준선 문제: ORA는 잘라낸 DEG 목록만 보고, GSEA는 순위 전체를 본다 (새 그림, 설명용 가상 자료)
from medfig import *

L = {
    "ko": dict(p1="① ORA: 기준선으로 자른 DEG 목록만 사용",
               p2="② GSEA: 모든 유전자를 순위대로 사용",
               up="DEG (상향)", down="DEG (하향)", mid="버림 (padj > 0.05)",
               same="padj = 1e-10도 0.049도\n똑같이 'DEG 1개'",
               miss="경로 유전자가 모두 padj ≈ 0.06\n→ DEG 목록에 0개, ORA는 놓침",
               hit="경로 유전자가 순위 위쪽에 몰림\n→ 누적합이 솟아 GSEA는 잡아냄",
               gene="경로 유전자", rank_l="순위 1 (가장 상향)", rank_r="N (가장 하향)", rs="누적합"),
    "en": dict(p1="① ORA: uses only the DEG list cut at a threshold",
               p2="② GSEA: uses every gene, in rank order",
               up="DEGs (up)", down="DEGs (down)", mid="discarded (padj > 0.05)",
               same="padj = 1e-10 and 0.049\ncount the same: one DEG",
               miss="All pathway genes at padj ≈ 0.06\n→ 0 in the DEG list; ORA misses it",
               hit="Pathway genes cluster near the top\n→ running sum peaks; GSEA catches it",
               gene="pathway gene", rank_l="rank 1 (most up)", rank_r="N (most down)", rs="running sum"),
}

N = 200                      # 설명용: 순위 칸 수
cut_up, cut_dn = 18, 182     # DEG 경계(상향 끝 / 하향 끝)
rng = np.random.default_rng(3)
hits = np.sort(np.r_[np.arange(20, 44, 3), rng.choice(np.arange(60, 190), 3, replace=False)])
X0, W = 0.35, 6.2            # 띠 위치(인치)
xr = lambda i: X0 + W * (i + 0.5) / N
GENE = CAT[2]                # 경로 유전자 표시색(두 패널 같은 색)


def strip(ax, y, h=0.34):
    box(ax, X0, y, W, h, fc=FAINT, ec=LINE, r=0.04)
    ax.vlines([xr(i) for i in hits], y + 0.03, y + h - 0.03, color=GENE, lw=2.2, zorder=4)


def draw(t):
    fig, ax = new(6.9, 5.0)
    # ── ① ORA ──
    label(ax, 0.05, 4.85, t["p1"], fs=12.5, w="bold", ha="left")
    y1 = 3.95
    strip(ax, y1)
    for a, b, c in [(0, cut_up, CAT[0]), (cut_dn, N, CAT[1])]:
        box(ax, xr(a) - W / N / 2, y1, (b - a) * W / N, 0.34, fc=mix(c, 0.35), ec="none", r=0.04, z=3)
    label(ax, xr(cut_up / 2), y1 + 0.52, t["up"], fs=11, w="semibold", c=CAT[0])
    label(ax, xr((cut_dn + N) / 2), y1 + 0.52, t["down"], fs=11, w="semibold", c=CAT[1], ha="center")
    label(ax, xr(N / 2), y1 + 0.52, t["mid"], fs=11, c=TEXT2)
    for c in (cut_up, cut_dn):
        ax.plot([X0 + W * c / N] * 2, [y1 - 0.08, y1 + 0.42], color=TEXT, lw=1.3, ls=(0, (3, 2)), zorder=5)
    # 같은 취급 / 놓침
    arrow(ax, X0 + 0.35, y1 - 0.36, X0 + 0.35, y1 - 0.04, color="#9AA1AB", lw=1.2, ms=9)
    label(ax, X0, y1 - 0.42, t["same"], fs=11, c=TEXT2, ha="left", va="top", linespacing=1.35)
    xm = xr(hits[3])
    arrow(ax, xm + 0.9, y1 - 0.42, xm + 0.05, y1 - 0.06, color=ACCENT_INK, lw=1.4, ms=10, rad=-0.2)
    label(ax, xm + 0.98, y1 - 0.42, t["miss"], fs=11, w="bold", c=ACCENT_INK, ha="left", va="top",
          linespacing=1.35)

    # ── ② GSEA ──
    label(ax, 0.05, 2.85, t["p2"], fs=12.5, w="bold", ha="left")
    y2 = 0.62
    strip(ax, y2)
    # 누적합: 경로 유전자면 +1/K, 아니면 −1/(N−K)
    K = len(hits)
    step = np.where(np.isin(np.arange(N), hits), 1 / K, -1 / (N - K))
    rs = np.r_[0, np.cumsum(step)]
    base, sc = y2 + 0.73, 1.0 / rs.max()
    xs = X0 + W * np.arange(N + 1) / N
    ax.plot([X0, X0 + W], [base, base], color=LINE, lw=1, zorder=2)
    ax.fill_between(xs, base, base + rs * sc, where=rs > 0, color=mix(CAT[0], 0.15), lw=0, zorder=2)
    ax.plot(xs, base + rs * sc, color=CAT[0], lw=2, zorder=3)
    k = rs.argmax()
    label(ax, X0 + W, base - 0.16, t["rs"], fs=11, c=CAT[0], ha="right")
    label(ax, X0 + 3.75, base + rs[k] * sc + 0.08, t["hit"], fs=11, c=TEXT, ha="left", va="top",
          linespacing=1.35)
    # 순위 축
    label(ax, X0, y2 - 0.2, t["rank_l"], fs=11, c=TEXT2, ha="left")
    label(ax, X0 + W, y2 - 0.2, t["rank_r"], fs=11, c=TEXT2, ha="right")
    # 범례: 경로 유전자
    ax.vlines(X0 + W - 1.55, 4.77, 4.93, color=GENE, lw=2.2)
    label(ax, X0 + W - 1.45, 4.85, t["gene"], fs=11, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W10_threshold{suffix}.png")
