# W1 §1 3' kit vs. 5' kit: mRNA의 어느 끝을 읽는지와 주된 용도
# 원본: assets/img/part1/3_5_kit.png (어두운 배경, 영어) → 밝은 스타일로 다시 그림
from medfig import *

L = {
    "ko": dict(cap="5′ cap", cds="암호화 영역", tail="poly-A 꼬리",
               k3="poly-A 꼬리를 표적 → 3′ 말단만 읽음", u3="scRNA-seq 표준 (10x Genomics) · 발현량 정량",
               k5="5′ 말단만 읽음", u5="TCR/BCR V(D)J 프로파일링 (CDR3가 5′ 쪽)",
               reads="읽는 구간"),
    "en": dict(cap="5′ cap", cds="coding region", tail="poly-A tail",
               k3="targets the poly-A tail → reads the 3′ end only", u3="scRNA-seq standard (10x Genomics) · gene expression",
               k5="reads the 5′ end only", u5="TCR/BCR V(D)J profiling (CDR3 is at the 5′ end)",
               reads="reads"),
}
K3, K5 = CAT[0], CAT[2]
X0, X1, XT, XE = 0.75, 1.45, 5.65, 6.8        # cap 시작 · 암호화 영역 시작 · 꼬리 시작 · 끝


def draw(t):
    fig, ax = new(6.9, 3.65)
    # mRNA
    y = 3.2
    label(ax, 0.05, y, "mRNA", fs=12, w="bold", ha="left")
    box(ax, X0, y - 0.22, X1 - X0, 0.44, fc=mix(TEXT2, 0.3), ec="none", r=0.06)
    label(ax, (X0 + X1) / 2, y, t["cap"], fs=11, w="semibold")
    box(ax, X1, y - 0.12, XT - X1, 0.24, fc=FAINT, ec=LINE, r=0.04)
    label(ax, (X1 + XT) / 2, y, t["cds"], fs=11, c=TEXT2)
    box(ax, XT, y - 0.22, XE - XT, 0.44, fc=mix(TEXT2, 0.3), ec="none", r=0.06)
    label(ax, (XT + XE) / 2, y, t["tail"], fs=11, w="semibold")
    # 두 kit: (이름, 색, 읽는 구간, 설명, 용도, 막대 y)
    rows = [("3′ kit", K3, (XT - 1.0, XT), t["k3"], t["u3"], 2.35),
            ("5′ kit", K5, (X1, X1 + 1.0), t["k5"], t["u5"], 1.05)]
    for name, c, (a, b), k, u, yy in rows:
        pill(ax, 0.05, yy, name, fc=c, fs=12, ha="left", h=0.32)
        box(ax, X1, yy - 0.09, XT - X1, 0.18, fc=FAINT, ec=LINE, r=0.03)
        box(ax, a, yy - 0.09, b - a, 0.18, fc=c, ec="none", r=0.03, z=3)
        label(ax, (a + b) / 2, yy + 0.24, t["reads"], fs=11, w="semibold", c=c)
        label(ax, X1, yy - 0.34, k, fs=11.5, w="semibold", ha="left")
        label(ax, X1, yy - 0.63, u, fs=11, c=TEXT2, ha="left")
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part1/3_5_kit{suffix}.png")
