"""Matplotlib 中文字体与 XJTU-thesis.cls（Linux: Materials/Fonts/SIMSUN.TTC）对齐。"""
import os

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 仅作拉丁/符号回退，不参与中文优先匹配
_LATIN_FALLBACK = ['DejaVu Sans']


def setup_thesis_plot_fonts():
    """优先使用模板同款宋体；否则 SimSun / 衬线类 CJK，避免 Noto Sans 与正文不一致。"""
    root = os.path.dirname(os.path.abspath(__file__))
    simsun_path = os.path.join(root, 'Materials', 'Fonts', 'SIMSUN.TTC')

    if os.path.isfile(simsun_path):
        try:
            fm.fontManager.addfont(simsun_path)
            prop = fm.FontProperties(fname=simsun_path)
            cjk_name = prop.get_name()
            plt.rcParams['font.sans-serif'] = [cjk_name] + _LATIN_FALLBACK
            plt.rcParams['font.family'] = 'sans-serif'
            return
        except OSError:
            pass

    plt.rcParams['font.sans-serif'] = [
        'SimSun',
        'NSimSun',
        'Noto Serif CJK SC',
        'WenQuanYi Zen Hei',
        'Source Han Serif SC',
    ] + _LATIN_FALLBACK
    plt.rcParams['font.family'] = 'sans-serif'


def emphasis_fontproperties(size: float) -> fm.FontProperties:
    """图题与坐标轴标签用黑体文件，保证可见「加粗」（SimSun 的 fontweight=bold 常无效）。"""
    root = os.path.dirname(os.path.abspath(__file__))
    simhei_path = os.path.join(root, 'Materials', 'Fonts', 'SIMHEI.TTF')
    if os.path.isfile(simhei_path):
        try:
            return fm.FontProperties(fname=simhei_path, size=size)
        except OSError:
            pass
    return fm.FontProperties(family='Noto Sans CJK SC', weight='bold', size=size)
