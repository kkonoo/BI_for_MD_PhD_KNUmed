# W2 §3 데이터 프레임: 열마다 자료형이 다를 수 있음 (x = 숫자, y = 문자)
# 원본: assets/img/part1/W2_df.png → 같은 값으로 다시 그림. 옮길 글자가 없어 한 파일을 두 언어가 같이 씀.
from medfig import *

HEAD = CAT[0]


def draw():
    fig, ax = new(2.0, 2.0)
    w, h, g = 0.9, 0.36, 0.04
    cols = [("x", "<dbl>", ["1", "2", "3"]), ("y", "<chr>", ["a", "b", "c"])]
    for j, (name, typ, vals) in enumerate(cols):
        x = 0.05 + j * (w + g)
        box(ax, x, 1.4, w, 0.55, fc=HEAD, ec="none", r=0.04)
        label(ax, x + w / 2, 1.76, name, fs=13, w="bold", c="white")
        label(ax, x + w / 2, 1.53, typ, fs=11, c=mix(HEAD, 0.25))
        for i, v in enumerate(vals):
            box(ax, x, 1.4 - (i + 1) * (h + g), w, h, fc=FAINT, ec=LINE, r=0.03)
            label(ax, x + w / 2, 1.4 - (i + 1) * (h + g) + h / 2, v, fs=12.5)
    return fig


save(draw(), "../../assets/img/part1/W2_df.png")
