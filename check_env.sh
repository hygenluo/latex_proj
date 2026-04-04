#!/bin/bash
# XJTU-thesis 环境检查脚本
# 执行: ./check_env.sh

echo "=== XJTU-thesis 环境检查 ==="
echo ""
echo -n "xelatex:       "; which xelatex >/dev/null 2>&1 && (xelatex --version 2>&1 | head -1) || echo "未找到"
echo -n "latexmk:       "; which latexmk >/dev/null 2>&1 && echo "已安装" || echo "未找到"
echo -n "biber:         "; which biber >/dev/null 2>&1 && echo "已安装" || echo "未找到（需安装）"
echo -n "makeglossaries: "; which makeglossaries >/dev/null 2>&1 && echo "已安装" || echo "未找到"
echo ""
echo "字体目录 Materials/Fonts:"
ls -la Materials/Fonts/*.ttf Materials/Fonts/*.ttc 2>/dev/null || echo "  (空，需添加字体)"
echo ""
echo "检查完成。"
