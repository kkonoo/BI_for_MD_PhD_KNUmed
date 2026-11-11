# W5 §4 정규화가 필요한 이유 ①: 라이브러리 크기(시퀀싱 깊이)가 다르면 단순 count를 비교할 수 없음
# 원본: assets/img/part2/W5_library.png (자체 제작, 한국어) → 다시 그림. 예시 숫자는 원본 그대로(설명용 가상 자료).
from medfig import *

L = {
    "ko": dict(s=["샘플 A", "샘플 B"], lib="총 리드 수", cnt="유전자 K count", rat="비율 (K / 총 리드)",
               tot=["1,000만", "5,000만"],
               c1="단순 count는 B가 2.5배 높지만 (250 vs 100)",
               c2="총 리드 수로 보정한 비율은 오히려 A가 2배 높다"),
    "en": dict(s=["Sample A", "Sample B"], lib="total reads", cnt="gene K count", rat="ratio (K / total)",
               tot=["10,000,000", "50,000,000"],
               c1="The raw count is 2.5× higher in B (250 vs 100),",
               c2="but the ratio to total reads is 2× higher in A"),
}
SC = [CAT[0], CAT[3]]                      # 샘플 A / 샘플 B
TOT, CNT, RAT = [1, 5], ["100", "250"], ["0.001%", "0.0005%"]
BX, BMAX, XC, XR = 1.0, 1.9, 4.55, 6.0     # 막대 시작 · 최대 길이 · count 칸 · 비율 칸 중심


def draw(t):
    fig, ax = new(6.9, 2.75)
    label(ax, BX, 2.55, t["lib"], fs=11, c=TEXT2, ha="left")
    label(ax, XC, 2.55, t["cnt"], fs=11, c=TEXT2)
    label(ax, XR, 2.55, t["rat"], fs=11, c=TEXT2)
    ax.plot([0.05, 6.85], [2.35, 2.35], color=LINE, lw=1)
    for i in range(2):
        y = 1.95 - i * 0.6
        label(ax, 0.05, y, t["s"][i], fs=12, w="bold", c=SC[i], ha="left")
        w = BMAX * TOT[i] / 5
        box(ax, BX, y - 0.14, w, 0.28, fc=SC[i], ec="none", r=0.03)
        label(ax, BX + w + 0.1, y, t["tot"][i], fs=11, ha="left")
        label(ax, XC, y, CNT[i], fs=13, w="bold")
        label(ax, XR, y, RAT[i], fs=13, w="bold")
    ax.plot([0.05, 6.85], [1.0, 1.0], color=LINE, lw=1)
    label(ax, 3.45, 0.62, t["c1"], fs=11.5, c=TEXT2)
    label(ax, 3.45, 0.27, t["c2"], fs=12, w="bold", c=ACCENT_INK)
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part2/W5_library{suffix}.png")
