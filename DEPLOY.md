# XJTU-thesis 论文项目部署与运行文档

本文档说明 XJTU-thesis 1.2.7 西安交通大学学位论文 LaTeX 模板的完整部署、编译与日常使用方法。

---

## 一、项目概述

| 项目 | 说明 |
|------|------|
| 模板名称 | XJTU-thesis |
| 版本 | 1.2.7 |
| 用途 | 西安交通大学硕博学位论文 LaTeX 排版 |
| 主文档 | `main.tex` |
| 编译引擎 | XeLaTeX（必须，支持中文） |
| TeX Live | 要求 ≥ 2019 |

---

## 二、环境要求

### 2.1 必需软件

| 工具 | 用途 | 最低版本 |
|------|------|----------|
| XeLaTeX | 编译主文档 | TeX Live 2019+ |
| latexmk | 自动编排编译流程 | 随 TeX Live |
| biber | 处理参考文献 | - |
| makeglossaries | 处理术语表/缩略词 | - |

### 2.2 字体要求

- **中文**：宋体、黑体（或等价字体）
- **英文**：Times New Roman

> 注意：不要使用 CTeX 套装，推荐使用 TeX Live。

---

## 三、部署步骤

### 3.1 方案 A：系统级 TeX Live（推荐，需 sudo）

```bash
sudo apt-get update
sudo apt-get install texlive-xetex texlive-lang-chinese texlive-fonts-recommended \
  texlive-latex-extra latexmk biber
```

安装后 `xelatex`、`biber`、`latexmk`、`makeglossaries` 可直接使用。

### 3.2 方案 B：Conda 环境（texlive-core）

若已通过 Conda 安装 `texlive-core`，需额外处理：

1. **创建 xelatex 符号链接**（因 Conda texlive-core 可能只提供 `xelatex-unsafe`）：
   ```bash
   ln -sf xelatex-unsafe "$(dirname $(which pdflatex))/xelatex"
   ```

2. **安装 biber**（二选一）：
   ```bash
   # 方式 1：apt
   sudo apt-get install biber

   # 方式 2：tlmgr
   tlmgr install biber
   tlmgr path add
   ```

### 3.3 配置中文字体（Linux）

模板在 Linux 下从 `Materials/Fonts/` 加载字体，需放置以下文件：

| 文件名 | 用途 |
|--------|------|
| `fzsong.ttf` | 宋体 |
| `fzhei.ttf` | 黑体 |
| `times.ttf` | Times New Roman 正体 |
| `timesbd.ttf` | Times 粗体 |
| `timesi.ttf` | Times 斜体 |
| `timesbi.ttf` | Times 粗斜体 |

**获取字体：**

- 从 Windows `C:\Windows\Fonts` 复制 `simsun.ttc`、`simhei.ttf`、`times.ttf` 等，按上表重命名后放入 `Materials/Fonts/`
- 或使用 Fandol、Noto CJK 等免费字体，并相应修改 `XJTU-thesis.cls` 中 Linux 分支的字体配置

> macOS 下会自动使用 Songti SC、STHeiti，需在编译时启用 `--shell-escape`。

### 3.4 安装缺失宏包

首次编译若出现 `File 'xxx.sty' not found`，可用 tlmgr 安装：

```bash
tlmgr search --global --file "/gbt7714.sty"   # 查找包名
tlmgr install <包名>
tlmgr path add
```

---

## 四、项目结构

```
XJTU-thesis-1.2.7 2/
├── main.tex              # 主文档入口
├── XJTU-thesis.cls       # 文档类
├── latexmkrc             # latexmk 配置
├── clear.sh / clear.bat  # 清理临时文件
├── Main_Spine/           # 正文章节
│   ├── c1.tex .. c6.tex
├── Main_Miscellaneous/   # 摘要、致谢、附录等
│   ├── abstract_chs.tex
│   ├── abstract_eng.tex
│   ├── acknowledegment.tex
│   ├── glossary.tex      # 术语表/缩略词
│   └── ...
├── Figures/              # 图片
├── Codes/                # 代码片段
├── References/           # 参考文献 .bib
│   └── reference.bib
└── Materials/            # 模板资源
    ├── Fonts/            # 字体文件
    ├── BiblographyStyles/
    ├── Icons/
    └── Tools/
```

---

## 五、编译与运行

### 5.1 使用 latexmk（推荐）

```bash
cd "/home/luohonglin/myPapers/XJTU-thesis-1.2.7 2"
latexmk main.tex
```

`latexmkrc` 会依次执行：xelatex → xelatex → biber → makeglossaries → xelatex，并自动打开生成的 PDF。

### 5.2 手动编译

```bash
cd "/home/luohonglin/myPapers/XJTU-thesis-1.2.7 2"
xelatex -synctex=1 --shell-escape -interaction=nonstopmode main.tex
xelatex -synctex=1 --shell-escape -interaction=nonstopmode main.tex
biber main
makeglossaries main
xelatex -synctex=1 --shell-escape -interaction=nonstopmode main.tex
```

### 5.3 清理临时文件

```bash
./clear.sh
# 或
latexmk -c
```

---

## 六、IDE 配置

### 6.1 VS Code + LaTeX Workshop

- 编译引擎：latexmk
- 若使用 MiKTeX（Windows），需安装 [Perl](http://strawberryperl.com/)

### 6.2 TeXstudio / Texmaker

将编译引擎设置为 **latexmk**，工作目录为项目根目录。

---

## 七、环境检查

将以下内容保存为 `check_env.sh` 并执行：

```bash
#!/bin/bash
echo "=== XJTU-thesis 环境检查 ==="
echo -n "xelatex: "; which xelatex && xelatex --version 2>&1 | head -1 || echo "未找到"
echo -n "latexmk: "; which latexmk || echo "未找到"
echo -n "biber:   "; which biber || echo "未找到（需安装）"
echo -n "makeglossaries: "; which makeglossaries || echo "未找到"
echo ""
echo "字体目录 Materials/Fonts:"
ls -la Materials/Fonts/*.ttf Materials/Fonts/*.ttc 2>/dev/null || echo "  (空，需添加字体)"
```

---

## 八、故障排查

| 现象 | 可能原因 | 处理 |
|------|----------|------|
| `xelatex: command not found` | 未安装或 Conda 未正确配置 | 安装 texlive-xetex，或创建 xelatex→xelatex-unsafe 链接 |
| `Font ... not found` | 缺少字体 | 向 `Materials/Fonts/` 添加所需字体并按要求命名 |
| `biber: command not found` | 未安装 biber | `apt install biber` 或 `tlmgr install biber` |
| `File 'xxx.sty' not found` | 宏包缺失 | `tlmgr install <包名>` |
| 编译卡住或极慢 | 网络或首次生成格式 | 检查网络，可加 `-interaction=nonstopmode` |

---

## 九、相关链接

- [项目 README](README.md)
- [使用手册](使用手册.pdf)
- [研究生院模板及要求](http://gs.xjtu.edu.cn/info/1209/7605.htm)
- [图书馆硕博论文要求](http://www.lib.xjtu.edu.cn/info/1102/1217.htm)
