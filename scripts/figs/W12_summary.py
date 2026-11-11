# W12 전체 분석 파이프라인: 8단계, 단계마다 나오는 결과물과 확인할 점(원본의 체크리스트 그대로)
# 원본: assets/img/part4/W12_summary.png (영어, 고리 모양) → 2열 세로 흐름으로 다시 그림. "lfcshrink" → lfcShrink 오타 수정.
from medfig import *

# (제목, 결과물, [(확인할 점, 강조여부), ...])
L = {
    "ko": [("데이터 확보", ".fastq", [("연구 설계는?", 0), ("배치 효과는?", 0), ("N > 30, 표현형이 명확한가?", 0)]),
           ("전처리", ".bam", [("시퀀싱 품질은?", 0), ("read 트리밍", 0), ("read 정렬", 0)]),
           ("정량", "count matrix (raw)", [("정렬 기반 (alignment-based)", 0), ("정렬 없이 (alignment-free)", 0)]),
           ("정규화", "count matrix (정규화)", [("시료 간 비교를 위해", 0), ("library size와 유전자 분산", 0),
                                              ("TMM(edgeR) 또는 RLE(DESeq2)", 1), ("불필요한 유전자 필터링", 1)]),
           ("EDA / 시료 점검", "count matrix (변환)", [("변환 (vst/rlog)", 0), ("PCA plot", 0), ("배치 효과? 이상치?", 0)]),
           ("차등 발현 검정", "결과 (유전자)", [("design matrix", 0), ("log2FoldChange (ref: control)", 1),
                                          ("p-value와 FDR 보정 p-value", 1)]),
           ("시각화", "그림", [("lfcShrink", 0), ("volcano plot", 0), ("heatmap", 0)]),
           ("기능 분석", "결과 (경로)", [("과대표현 분석 (ORA)", 0), ("유전자 집합 농축 분석 (GSEA)", 1)])],
    "en": [("Data acquisition", ".fastq", [("study design?", 0), ("batch effect?", 0), ("N > 30, clear phenotype?", 0)]),
           ("Pre-processing", ".bam", [("sequencing quality?", 0), ("read trimming", 0), ("read alignment", 0)]),
           ("Quantification", "count matrix (raw)", [("alignment-based", 0), ("alignment-free", 0)]),
           ("Normalization", "count matrix (normalized)", [("for sample-sample comparison", 0),
                                                           ("library size & gene dispersion", 0),
                                                           ("TMM(edgeR) or RLE(DESeq2)", 1),
                                                           ("unnecessary gene filtering", 1)]),
           ("EDA / sample check", "count matrix (transformed)", [("transformation (vst/rlog)", 0), ("PCA plot", 0),
                                                                ("batch effect? outliers?", 0)]),
           ("Differential test", "results (genes)", [("design matrix", 0), ("log2FoldChange (ref: control)", 1),
                                                    ("p-value & FDR-corrected p-value", 1)]),
           ("Visualization", "plots", [("lfcShrink", 0), ("volcano plot", 0), ("heatmap", 0)]),
           ("Functional analysis", "results (pathways)", [("over-representation analysis (ORA)", 0),
                                                         ("gene set enrichment analysis (GSEA)", 1)])],
}
COL = ramp(8)
TH, OH, CH, GAP = 0.36, 0.36, 0.26, 0.24   # 제목 줄 / 결과물 줄 / 체크 줄 / 단계 사이 (인치)


def check(ax, x, y, c):
    ax.plot([x - 0.06, x - 0.015, x + 0.065], [y, y - 0.05, y + 0.06], color=c, lw=1.8,
            solid_capstyle="round", solid_joinstyle="round", zorder=4)


def draw(steps):
    hcol = [sum(TH + OH + CH * len(s[2]) + GAP for s in steps[k:k + 4]) for k in (0, 4)]
    H = max(hcol) + 0.1
    fig, ax = new(6.9, H)
    for k, (title, out, items) in enumerate(steps):
        x = 0.05 if k < 4 else 3.55
        if k in (0, 4):
            y = H - 0.25
        c = COL[k]
        num(ax, x + 0.17, y, k + 1, fc=c, r=0.16, fs=11.5)
        label(ax, x + 0.43, y, title, fs=12.5, w="bold", ha="left")
        pill(ax, x + 0.43, y - OH, out, fc=mix(c, 0.14), tc=shade(c, 0.1), fs=11, h=0.27,
             padx=0.09, ha="left")
        for j, (s, b) in enumerate(items):
            yy = y - OH - TH + 0.06 - j * CH
            check(ax, x + 0.5, yy, c)
            label(ax, x + 0.65, yy, s, fs=11, w="semibold" if b else "regular", ha="left")
        y_next = y - TH - OH - CH * len(items) - GAP + 0.06
        if k not in (3, 7):
            ax.plot([x + 0.17, x + 0.17], [y - 0.18, y_next + 0.18], color=LINE, lw=2, zorder=1)
        y = y_next
    return fig


for lang, suffix in [("ko", ""), ("en", "_en")]:
    save(draw(L[lang]), f"../../assets/img/part4/W12_summary{suffix}.png")
