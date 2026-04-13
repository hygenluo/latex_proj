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

sessions = ['会话 0', '会话 1', '会话 2', '会话 3', '会话 4']
cls_nums = np.array([15, 25, 35, 45, 55])

def acc_to_accn(acc):
    return np.array(acc) / 100.0 * cls_nums

def ideal_line(session0_acc):
    return np.array([session0_acc / 100.0 * n for n in cls_nums])

def setup_ax(ax, ylim_top=55):
    ax.set_xlabel('增量会话', fontproperties=_FP_AXIS, labelpad=6)
    ax.set_ylabel('ACCN', fontproperties=_FP_AXIS)
    ax.set_ylim(0, ylim_top)
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


# ── 图 3-6: 各方法 ACCN 曲线对比 ──
baseline = [89.67, 38.84, 26.97, 21.83, 16.25]
icarl    = [90.41, 74.09, 66.90, 63.68, 63.49]
bic      = [86.11, 64.91, 52.56, 50.10, 44.35]
ucir     = [88.07, 77.16, 69.24, 61.73, 63.58]
simplecil  = [90.85, 60.80, 44.78, 37.27, 30.52]
il2a       = [90.30, 73.31, 56.43, 48.90, 38.21]
ours       = [91.52, 80.47, 74.24, 72.72, 73.57]

fig, ax = plt.subplots(figsize=(9.2, 5.8))

ax.plot(sessions, ideal_line(91.52), color='gray', marker='o', ms=7, lw=2, ls='--', label='理想')
ax.plot(sessions, acc_to_accn(baseline), color=(115/255, 186/255, 214/255), marker='d', ms=7, lw=2, label='基线')
ax.plot(sessions, acc_to_accn(icarl), color=(13/255, 76/255, 109/255), marker='o', ms=7, lw=2, label='iCaRL')
ax.plot(sessions, acc_to_accn(bic), color=(255/255, 158/255, 2/255), marker='p', ms=7, lw=2, label='BiC')
ax.plot(sessions, acc_to_accn(ucir), color='yellowgreen', marker='^', ms=7, lw=2, label='UCIR')
ax.plot(sessions, acc_to_accn(simplecil), color=(0.45, 0.45, 0.45), marker='<', ms=7, lw=2, label='SimpleCIL')
ax.plot(sessions, acc_to_accn(il2a), color=(0.85, 0.45, 0.35), marker='>', ms=7, lw=2, label='IL2A')
ax.plot(sessions, acc_to_accn(ours), color=(219/255, 49/255, 36/255), marker='s', ms=7, lw=2, label='本文方法')

setup_ax(ax)
ax.set_title('不同类增量学习方法的 ACCN', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=9.5, ncol=3, loc='upper left', framealpha=0.92)
fig.tight_layout()
for ext in ('.pdf', '.png'):
    path = os.path.join(OUT_DIR, 'fig3-6-accn-main' + ext)
    fig.savefig(path, bbox_inches='tight', dpi=300)
    print(f'Saved {path}')
plt.close(fig)


# ── 图 3-7: 骨干网络 ACCN 曲线对比 ──
fig, ax = plt.subplots(figsize=(7, 5))

resnet = [89.37, 71.47, 62.00, 61.40, 58.41]
unet   = [91.52, 80.47, 74.24, 72.72, 73.57]

ax.plot(sessions, ideal_line(91.52), color='gray', marker='o', ms=7, lw=2, ls='--', label='理想')
ax.plot(sessions, acc_to_accn(resnet), color='chocolate', marker='d', ms=7, lw=2, label='ResNet')
ax.plot(sessions, acc_to_accn(unet), color='yellowgreen', marker='s', ms=7, lw=2, label='UNet')

setup_ax(ax)
ax.set_title('不同骨干网络的 ACCN', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
save_fig(fig, 'fig3-7-accn-backbone.pdf')


# ── 图 3-8: KD 与 BKD 的 ACCN 曲线对比 ──
fig, ax = plt.subplots(figsize=(7, 5))

kd  = [91.19, 78.13, 72.78, 72.42, 70.20]
bkd = [91.52, 80.47, 74.24, 72.72, 73.57]

ax.plot(sessions, ideal_line(91.52), color='gray', marker='o', ms=7, lw=2, ls='--', label='理想')
ax.plot(sessions, acc_to_accn(kd), color=(75/255, 116/255, 178/255), marker='d', ms=7, lw=2, label='KD')
ax.plot(sessions, acc_to_accn(bkd), color=(219/255, 49/255, 36/255), marker='s', ms=7, lw=2, label='BKD')

setup_ax(ax)
ax.set_title('KD 与 BKD 的 ACCN 对比', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
save_fig(fig, 'fig3-8-accn-kd.pdf')


# ── 图 3-9: 样本重放消融 ACCN 曲线 ──
fig, ax = plt.subplots(figsize=(7, 5))

no_replay   = [91.33, 42.00, 34.97, 29.40, 23.19]
with_replay = [91.52, 80.47, 74.24, 72.72, 73.57]

ax.plot(sessions, ideal_line(91.52), color='gray', marker='o', ms=7, lw=2, ls='--', label='理想')
ax.plot(sessions, acc_to_accn(no_replay), color=(223/255, 122/255, 94/255), marker='d', ms=7, lw=2, label='无重放')
ax.plot(sessions, acc_to_accn(with_replay), color=(130/255, 178/255, 154/255), marker='s', ms=7, lw=2, label='有重放')

setup_ax(ax)
ax.set_title('有无样本重放的 ACCN', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
save_fig(fig, 'fig3-9-accn-replay.pdf')


# ── 图 3-10: 知识巩固消融 ACCN 曲线 ──
fig, ax = plt.subplots(figsize=(7, 5))

no_consolidation   = [91.30, 3.87, 2.86, 2.27, 1.82]
with_consolidation = [91.52, 80.47, 74.24, 72.72, 73.57]

ax.plot(sessions, ideal_line(91.52), color='gray', marker='o', ms=7, lw=2, ls='--', label='理想')
ax.plot(sessions, acc_to_accn(no_consolidation), color=(145/255, 213/255, 66/255), marker='d', ms=7, lw=2, label='无知识巩固')
ax.plot(sessions, acc_to_accn(with_consolidation), color=(237/255, 104/255, 37/255), marker='s', ms=7, lw=2, label='有知识巩固')

setup_ax(ax)
ax.set_title('有无知识巩固的 ACCN', fontproperties=_FP_TITLE, pad=10)
ax.legend(fontsize=11, loc='upper left', framealpha=0.9)
save_fig(fig, 'fig3-10-accn-compress.pdf')

print('\nAll 5 figures generated successfully.')
