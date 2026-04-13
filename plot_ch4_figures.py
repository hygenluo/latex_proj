import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

from plot_fonts import setup_thesis_plot_fonts, emphasis_fontproperties

setup_thesis_plot_fonts()
_FP_AXIS = emphasis_fontproperties(14)
_FP_TITLE = emphasis_fontproperties(15)
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['mathtext.fontset'] = 'stix'

OUT_DIR = 'Figures'
os.makedirs(OUT_DIR, exist_ok=True)

sessions = ['会话 0', '会话 1', '会话 2', '会话 3', '会话 4', '会话 5']


def setup_ax(ax, ylim_bot=50, ylim_top=100):
    ax.set_xlabel('增量会话', fontproperties=_FP_AXIS, labelpad=6)
    ax.set_ylabel('准确率（%）', fontproperties=_FP_AXIS)
    ax.set_ylim(ylim_bot, ylim_top)
    ax.tick_params(axis='both', labelsize=12)
    ax.grid(color='lightgray', linewidth=0.8, linestyle='--')
    for spine in ax.spines.values():
        spine.set_linewidth(1.2)


def save_fig(fig, name):
    fig.tight_layout()
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f'Saved {path}')


# ── Fig 4-4: Accuracy curves of different FSCIL methods ──
fig, ax = plt.subplots(figsize=(8, 5.5))

baseline = [96.67, 73.81, 63.33, 60.74, 59.00, 56.06]
cec      = [94.63, 80.00, 66.83, 69.76, 69.33, 63.75]
icarl    = [89.94, 7.49, 6.65, 6.15, 5.78, 5.13]
fact     = [90.25, 81.67, 67.17, 70.67, 68.33, 61.08]
cfscil   = [51.38, 39.33, 18.33, 11.81, 8.67, 13.17]
ours     = [90.00, 79.52, 74.17, 75.93, 77.00, 74.24]

ax.plot(sessions, baseline, color=(115/255, 186/255, 214/255), marker='d', ms=6, lw=1.8, label='基线')
ax.plot(sessions, cec,      color=(13/255, 76/255, 109/255),   marker='o', ms=6, lw=1.8, label='CEC')
ax.plot(sessions, icarl,    color=(255/255, 158/255, 2/255),   marker='^', ms=6, lw=1.8, label='iCaRL')
ax.plot(sessions, fact,     color=(140/255, 86/255, 168/255),  marker='v', ms=6, lw=1.8, label='FACT')
ax.plot(sessions, cfscil,   color=(100/255, 100/255, 100/255), marker='x', ms=7, lw=1.8, label='C-FSCIL')
ax.plot(sessions, ours,     color=(219/255, 49/255, 36/255),   marker='s', ms=6, lw=2.2, label='本文方法')

setup_ax(ax, ylim_bot=0, ylim_top=100)
ax.set_title('不同 FSCIL 方法的准确率', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=9, loc='lower left', framealpha=0.92, ncol=2, columnspacing=0.8)
save_fig(fig, 'fig4-4-fscil-acc-curve.pdf')


# ── Fig 4-5: Ablation study accuracy curves ──
fig, ax = plt.subplots(figsize=(8, 5.5))

abl_baseline = [96.67, 73.81, 63.33, 60.74, 59.00, 56.06]
abl_temporal = [87.78, 75.71, 66.25, 58.89, 60.67, 59.09]
abl_graph    = [90.56, 79.05, 69.17, 61.48, 63.00, 60.00]
abl_full     = [92.78, 80.48, 70.42, 71.85, 71.33, 67.88]

ax.plot(sessions, abl_baseline, color=(115/255, 186/255, 214/255), marker='d', ms=7, lw=2, label='基线')
ax.plot(sessions, abl_temporal, color=(75/255, 116/255, 178/255),  marker='o', ms=7, lw=2, label='+ 时序注意力')
ax.plot(sessions, abl_graph,    color=(255/255, 158/255, 2/255),   marker='^', ms=7, lw=2, label='+ 图注意力')
ax.plot(sessions, abl_full,     color=(219/255, 49/255, 36/255),   marker='s', ms=7, lw=2, label='+ 双分类器（完整）')

setup_ax(ax)
ax.set_title('消融配置的准确率', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=11, loc='lower left', framealpha=0.9)
save_fig(fig, 'fig4-5-fscil-ablation.pdf')


print('\nAll Chapter 4 figures generated successfully.')
