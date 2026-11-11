# W8 §1 BH 절차 (새 그림): 본문 코드 예시의 p-value 5개를 순위대로 놓고 기준선 (i/m)·α와 비교
# p = 0.0001, 0.001, 0.04, 0.05, 0.2 / m = 5 / α = 0.05 → 순위 1–2 통과, 3–5 탈락
from medfig import *

L = {
    "ko": dict(x="순위 i (p-value 작은 순)", y="p-value", line="기준선 (i/m)·α",
               ok="통과", no="탈락", note="m = 5, α = 0.05", off="0.2\n(축 밖)"),
    "en": dict(x="rank i (smallest p first)", y="p-value", line="threshold (i/m)·α",
               ok="pass", no="fail", note="m = 5, α = 0.05", off="0.2\n(off scale)"),
}
genes = ["GeneD", "GeneB", "GeneA", "GeneC", "GeneE"]       # 코드의 정렬 결과
p = np.array([0.0001, 0.001, 0.04, 0.05, 0.2])
m, alpha = 5, 0.05
i = np.arange(1, m + 1)
thr = i / m * alpha
PASS, FAIL = CAT[0], TEXT2
TOP = 0.066                                                  # y축 위쪽 끝(0.2는 축 밖 표시)


def draw(t):
    fig, ax = plt.subplots(figsize=(6.6, 3.7))
    fig.subplots_adjust(left=0.12, right=0.97, top=0.95, bottom=0.2)
    ax.plot(np.r_[0.5, i, 5.5], np.r_[0.5, i, 5.5] / m * alpha, color=TEXT, lw=1.3, ls=(0, (4, 3)))
    ax.text(5.45, 0.041, t["line"], ha="right", va="top", fontsize=11.5, color=TEXT)
    for k in range(m):
        ok = p[k] <= thr[k]
        y = min(p[k], TOP - 0.004)
        c = PASS if ok else FAIL
        ax.plot([i[k]], [y], "o", ms=10, color=c if ok else "white", mec=c, mew=2, zorder=4, clip_on=False)
        if p[k] > TOP:                                       # 0.2: 축 밖이라 화살표로
            ax.annotate("", xy=(i[k], TOP + 0.005), xytext=(i[k], y + 0.0025),
                        arrowprops=dict(arrowstyle="-|>", color=FAIL, lw=1.4), annotation_clip=False)
            ax.text(i[k] - 0.14, y, t["off"], ha="right", va="center", fontsize=11, color=FAIL, linespacing=1.2)
        else:
            ax.text(i[k] + (0.16 if ok else -0.14), p[k] + 0.0035, f"{p[k]:g}", ha="left" if ok else "right",
                    va="bottom", fontsize=11,
                    color=shade(PASS, 0.2) if ok else TEXT2)
    # 통과 / 탈락 구역
    ax.axvspan(0.5, 2.5, color=mix(PASS, 0.08), lw=0, zorder=0)
    ax.text(1.5, 0.052, t["ok"], ha="center", fontsize=12.5, fontweight="bold", color=PASS)
    ax.text(4.0, 0.006, t["no"], ha="center", fontsize=12.5, fontweight="bold", color=TEXT2)
    ax.text(0.62, TOP - 0.003, t["note"], ha="left", va="top", fontsize=11, color=TEXT2)
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0, TOP)
    ax.set_xticks(i); ax.set_xticklabels([f"{k}\n{g}" for k, g in zip(i, genes)], fontsize=11)
    ax.set_yticks([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06])
    ax.tick_params(axis="y", labelsize=11)
    ax.set_xlabel(t["x"], fontsize=11.5); ax.set_ylabel(t["y"], fontsize=11.5)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part3/W8_BH{suffix}.png")
