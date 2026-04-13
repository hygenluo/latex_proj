# 第四章实验部分修订说明（与代码日志对照）

## 1. 正文结构（`Main_Spine/c4.tex` §4.4）

「实验结果与分析」内各小节为连续三级标题（无独立「补充实验」节），当前顺序为：

1. **对比实验结果**（含与第三章 CIL 的并列说明）
2. **消融实验**
3. **基础类别数敏感性**（表 `tab:fscil-baseclass`）
4. **支持集规模对增量性能的影响**（表 `tab:fscil-kshot`）

**说明**：双分类器温度系数 $\tau$ 的**多取值对比实验**未写入正文；$\tau=16$ 作为固定超参在 **§4.3** 与表 `tab:fscil-hyperparams` 中给出，并与 **§4.2.4** 双分类器设计一致。

## 2. 数据来源（实现细节仅在此文档列出）

数值核对可参见 [`04-FSCIL-easy/logs/script/missing/`](../04-少样本增量学习/04-FSCIL-easy/logs/script/missing/) 下日志末次「全会话」测试结果；补跑脚本见同仓库 `script/run_missing_experiments.sh`。

| 实验内容 | 日志文件（示例） |
|----------|-------------------|
| $\mathrm{base\_class}=35$ | `missing_base35_*.log` |
| 每类 3 / 5 支持样本 | `missing_shot_data_3shot_*.log`, `missing_shot_data_5shot_*.log` |
| FACT 基线（CVPR 2022） | TEGA [`logs/new_experiments/train_xrfdataset_fact_start0_*.log`](../../04-少样本增量学习/TEGA/logs/new_experiments/)，汇总见同目录 `fact-results.txt` |
| C-FSCIL 基线（CVPR 2022） | TEGA [`logs/new_experiments/train_xrfdataset_cfscil_start0_*.log`](../../04-少样本增量学习/TEGA/logs/new_experiments/)，汇总见同目录 `results.txt` |

主实验仍以 **表 `tab:fscil-main-compare`** 为准；FACT / C-FSCIL 与本文共用 XRF、`base\_class=30`、5-way 1-shot、`seed=1` 等 §4.3 主设定。

## 3. 编译环境

若全文 `latexmk` 报缺宏包（如 `tcolorbox`），属 TeX 环境依赖，与本章正文修改无直接关系。
