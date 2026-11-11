# W5 §4 정규화가 필요한 이유 ②: 유전자가 길수록 리드가 더 많이 붙음 → 길이로 나눠야 비교 가능
# 원본: assets/img/part2/W5_depth.jpg (자체 제작, 한국어) → W5_depth.png 로 다시 그림.
# 예시 숫자(1 kb·3 kb, 100·300)는 원본 그대로(설명용 가상 자료). 리드 조각 수는 개념 표시.
from medfig import *

L = {
    "ko": dict(g=["유전자 L (1 kb)", "유전자 M (3 kb)"], gene="유전자 길이와 붙은 리드",
               cnt="단순 count", per="길이 보정 (count / kb)",
               c1="실제 발현량이 같아도 긴 유전자 M에 리드가 3배 붙는다 (300 vs 100)",
               c2="길이로 나누면 둘 다 100으로 같다"),
    "en": dict(g=["Gene L (1 kb)", "Gene M (3 kb)"], gene="gene length and its reads",
               cnt="raw count", per="per kb (count / kb)",
               c1="Same true expression, yet the longer gene M gets 3× the reads (300 vs 100)",
               c2="Divided by length, both are 100"),
}
GENE, READ = mix(TEXT2, 0.25), CAT[2]
KB, CNT, PER = [1, 3], ["100", "300"], ["100", "100"]
GX, KW, XC, XR = 1.6, 0.75, 4.95, 6.15     # 유전자 시작 · 1 kb 길이 · count 칸 · 보정 칸 중심


def draw(t):
    fig, ax = new(6.9, 2.95)
    label(ax, GX, 2.75, t["gene"], fs=11, c=TEXT2, ha="left")
    label(ax, XC, 2.75, t["cnt"], fs=11, c=TEXT2)
    label(ax, XR, 2.75, t["per"], fs=11, c=TEXT2)
    ax.plot([0.05, 6.85], [2.55, 2.55], color=LINE, lw=1)
    for i in range(2):
        y = 2.05 - i * 0.7
        label(ax, 0.05, y, t["g"][i], fs=12, w="bold", ha="left")
        w = KW * KB[i]
        box(ax, GX, y - 0.22, w, 0.16, fc=GENE, ec="none", r=0.03)
        n = 4 * KB[i]                                   # 같은 밀도로 리드 조각
        for k in range(n):
            x0 = GX + k * w / n + 0.03
            row = k % 2
            ax.plot([x0, x0 + 0.13], [y + 0.02 + row * 0.12] * 2, color=READ, lw=2.4,
                    solid_capstyle="butt")
        label(ax, XC, y, CNT[i], fs=13, w="bold")
        label(ax, XR, y, PER[i], fs=13, w="bold")
    ax.plot([0.05, 6.85], [1.0, 1.0], color=LINE, lw=1)
    label(ax, 3.45, 0.62, t["c1"], fs=11.5, c=TEXT2)
    label(ax, 3.45, 0.27, t["c2"], fs=12, w="bold", c=ACCENT_INK)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W5_depth{suffix}.png")
