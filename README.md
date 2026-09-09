# Academic Paper Translation

`academic-paper-translation` 是一个 Codex 技能，用于把英文**学术论文 PDF**制作成完整的中文译文版和中英对照版 Word 文档，并保留一份与原文件字节一致的英文 PDF 副本。正式翻译前，它会根据论文内容、当前设备与系统环境以及可见的模型设置给出粗略耗时范围，再让用户选择精细或快速模式。

它适用于完整论文级别的翻译交付，不适用于短段落摘译、普通非学术文本翻译，也不是独立的命令行自动翻译程序。

## 解决什么问题

英文论文翻译常见的问题不是只把正文翻成中文，而是容易遗漏或破坏论文中的结构化内容，例如图、表、公式、题注、脚注、参考文献、声明、附录和补充材料提示。

本技能提供两套面向不同用途的完整论文交付流程：精细模式保留原有的全面清单、译后润色和逐页精查，适合核心参考文献；快速模式使用最简黑白版式并减少润色与排版迭代，适合文献探索。两种模式都会保留既定交付物和论文实质内容。

## 主要功能

- 翻译前模式选择：提供精细翻译、快速翻译和自定义选项，在用户选择前不开始全文翻译。
- 轻量耗时预估：根据页数、抽样版面复杂度、操作系统、可用 CPU/内存信息以及可见的模型与推理档位，给出两个模式的大致完成时间范围。
- 精细翻译模式：执行完整清单、术语统一、独立润色和逐页内容/版式复核，质量较高，但耗时与 token 用量较多。
- 快速翻译模式：采用单栏黑白 Word 样式、单次分段翻译和最低必要版式修复，耗时与 token 用量较少，译文质量以探索性阅读为目标。
- 生成中文单语 `.docx`：包含英文论文的完整中文译文。
- 生成中英双语 `.docx`：英文内容与对应中文翻译相邻排列，便于对照阅读。
- 归档英文原始 PDF：保存一份不修改内容的英文 PDF 副本。
- 建立源文件清单：记录页数、标题、作者、摘要、关键词、章节标题、图、表、公式、题注、脚注、参考文献、致谢、声明、附录和补充材料提示等。
- 维护一对一覆盖核对：按照 `references/completeness-checklist.md` 检查源文件内容是否都进入两个目标 Word 文档。
- 保留学术细节：要求保留数字、单位、统计符号、样本量、不确定性、限定条件、文内引用和参考文献条目。
- 保留视觉信息：要求图像完整、清晰、不变形，并尽量保留图中的面板、坐标轴、刻度、图例、比例尺、方向标、边框和标注。
- 支持最终包校验：`scripts/verify_translation_package.py` 可检查英文 PDF 副本是否与源 PDF 哈希一致，统计 DOCX 中图片、表格和公式数量，并检查常见占位符。

## 安装方法

将本目录作为 Codex 技能放在 Codex 的技能目录中，例如：

```text
$CODEX_HOME/skills/academic-paper-translation
```

当前技能目录应至少包含以下文件：

```text
academic-paper-translation/
├── SKILL.md
├── agents/openai.yaml
├── references/completeness-checklist.md
├── references/local-artifact-versioning.md
├── references/translation-modes.md
└── scripts/verify_translation_package.py
```

使用该技能完成论文翻译时，还需要 Codex 环境中可用的 PDF 处理能力和 Word 文档生成/渲染能力。校验脚本依赖 Python，并使用 `pypdf` 读取 PDF 页数。

## 使用方法

在 Codex 中提供一篇完整的英文论文 PDF，并明确调用该技能，例如：

```text
Use $academic-paper-translation to estimate the time, ask me to choose fine or fast mode, then translate this English academic paper.
```

技能会先执行轻量预检，并以当前对话语言简要报告页数、复杂度、环境/模型信息以及两个模式的时间范围。随后它会提供以下选择，在用户作答前不会开始全文翻译：

- `A. 精细翻译`：推荐用于核心参考文献，质量较高，耗时和 token 用量较多。
- `B. 快速翻译`：推荐用于文献探索，使用最简黑白版式，速度更快、token 用量更少，但不以出版级润色为目标。
- `C. 自定义`：自行指定交付物、格式或质量与速度侧重。

默认交付物包括：

1. 中文译文版 `.docx`
2. 中英对照版 `.docx`
3. 与源文件字节一致的英文 PDF 副本

如果需要将结果保存为本地成果，应遵守本技能内置的 `references/local-artifact-versioning.md`：在当前项目的 `任务成果` 目录下创建新的、不覆盖旧版本的版本子目录，并把本次交付物放入其中。

### 推荐工作流程

1. 只读取页数、元数据和少量代表性页面，检查可直接获得的设备/系统与模型信息。
2. 给出精细、快速两种模式的粗略耗时范围，并等待用户选择。
3. 精细模式按 `references/completeness-checklist.md` 建立完整清单，执行独立润色和全面内容/版式迭代。
4. 快速模式建立轻量覆盖清单，单次分段翻译并使用简单黑白单栏版式，不复刻期刊设计。
5. 两种模式都生成中文版与中英对照版 Word 文档，归档英文原始 PDF，并渲染检查每一页；快速模式只针对影响完整性和阅读的问题返工。
6. 使用校验脚本辅助检查最终包和英文 PDF 哈希。

### 校验脚本示例

```bash
python scripts/verify_translation_package.py \
  --source-pdf path/to/source.pdf \
  --original-copy path/to/original_copy.pdf \
  --docx path/to/chinese.docx \
  --docx path/to/bilingual.docx \
  --expected-pdf-pages 12 \
  --expected-images 8 \
  --expected-tables 3 \
  --expected-equations 5 \
  --report path/to/verification_report.json
```

`--expected-pdf-pages`、`--expected-images`、`--expected-tables` 和 `--expected-equations` 应来自翻译前建立的源文件清单。脚本检查结果只能作为辅助依据，不能替代人工逐页视觉检查。

## 输入输出示例

### 输入

```text
source.pdf
```

输入文件应是一篇完整的英文学术论文 PDF。

轻量预检后的交互示例：

```text
论文约 18 页，版面复杂度中等；当前设备与模型设置下，粗略预计：
A. 精细翻译：约 2.5-4.5 小时
B. 快速翻译：约 45-90 分钟
C. 自定义
请选择一种模式。该范围会受网络负载、OCR 质量和复杂版式修复影响。
```

示例时间仅演示输出格式，实际估算会依据当前论文和运行环境变化。

### 输出

```text
任务成果/
└── 学术论文翻译_yyyyMMddHHmm_001_初版完整翻译_codex/
    ├── chinese.docx
    ├── bilingual.docx
    ├── original_copy.pdf
    └── verification_report.json
```

实际文件名可以根据论文标题或用户要求调整，但默认交付类型保持为中文 Word 文档、中英对照 Word 文档和英文原 PDF 副本。`verification_report.json` 只有在运行校验脚本并指定 `--report` 时才会生成。

## 真实能力边界

- 本技能描述的是 Codex 执行完整论文翻译交付时应遵循的流程和验收标准。
- 翻译前的时间范围是低成本粗略估算，不是完成时限承诺；扫描质量、网络负载、复杂公式/表格和版式返工都会影响实际耗时。
- 快速模式仍要求内容完整和页面可读，但不会复刻期刊版式，也不执行独立的语言风格润色，因此不应视为出版级译稿。
- `scripts/verify_translation_package.py` 只负责最终包的若干机械检查，不负责自动翻译、自动排版或自动判断所有内容是否完整。
- 文档中图像、表格、公式和页面布局是否合格，必须通过最终 DOCX 渲染后的逐页检查确认。
- 英文 PDF 副本是否未被修改，可通过脚本中的 SHA-256 哈希比较辅助确认。

---

# Academic Paper Translation

`academic-paper-translation` is a Codex skill for turning an English academic paper PDF into a complete Chinese-only Word document, an English-Chinese bilingual Word document, and an unchanged byte-identical copy of the original English PDF. Before full translation, it gives a rough time range based on sampled paper content, the current device and operating environment, and visible model settings, then asks the user to choose fine or fast mode.

It is intended for full-paper academic translation deliverables. It is not intended for short excerpt translation, ordinary non-academic prose translation, and it is not a standalone command-line automatic translation program.

## Problem Solved

Academic paper translation is not only about translating the main text. Important structured content can easily be omitted or damaged, including figures, tables, equations, captions, footnotes, references, declarations, appendices, and supplementary-data notices.

This skill provides two complete-paper workflows for different goals. Fine mode keeps the existing full inventory, polishing pass, and detailed page review for core references. Fast mode uses the simplest black-and-white layout and fewer translation/layout iterations for literature exploration. Both modes retain the established deliverables and substantive paper content.

## Main Features

- Require a pre-translation choice among fine, fast, and custom modes; full translation does not start before the user answers.
- Provide a lightweight time estimate using page count, sampled layout complexity, operating system, readily available CPU/memory information, and visible model/reasoning settings.
- Fine mode uses a full inventory, terminology normalization, a separate polishing pass, and detailed content/layout review; it offers higher quality at higher time and token cost.
- Fast mode uses a plain single-column black-and-white Word style, one translation pass, and only necessary layout repair; it is faster and uses fewer tokens, with quality intended for exploratory reading.
- Create a Chinese-only `.docx` containing the complete Chinese translation of the English paper.
- Create an English-Chinese bilingual `.docx` with each English unit kept adjacent to its Chinese translation for comparison.
- Archive the original English PDF by saving an unchanged copy.
- Build a source inventory covering page count, title, authors, abstract, keywords, section headings, figures, tables, equations, captions, footnotes, references, acknowledgements, declarations, appendices, and supplementary-data notices.
- Maintain one-to-one coverage checks using `references/completeness-checklist.md`.
- Preserve academic details such as numbers, units, statistical symbols, sample sizes, uncertainty, qualifications, in-text citations, and reference entries.
- Preserve visual information by keeping figures complete, readable, and undistorted, including panels, axes, tick labels, legends, scale bars, compass or north arrows, borders, and annotations where present.
- Support final package verification with `scripts/verify_translation_package.py`, which checks whether the archived English PDF matches the source PDF hash, counts images, tables, and equations in DOCX files, and detects common placeholder text.

## Installation

Place this directory in the Codex skills folder, for example:

```text
$CODEX_HOME/skills/academic-paper-translation
```

The skill directory should contain at least:

```text
academic-paper-translation/
├── SKILL.md
├── agents/openai.yaml
├── references/completeness-checklist.md
├── references/local-artifact-versioning.md
├── references/translation-modes.md
└── scripts/verify_translation_package.py
```

Paper translation with this package also requires PDF handling capability and Word document creation/rendering capability in the Codex environment. The verification script depends on Python and uses `pypdf` to read PDF page counts.

## Usage

Provide a complete English academic paper PDF in Codex and invoke the skill explicitly, for example:

```text
Use $academic-paper-translation to estimate the time, ask me to choose fine or fast mode, then translate this English academic paper.
```

The skill first performs a lightweight preflight and briefly reports page count, complexity, environment/model notes, and a time range for both modes in the current conversation language. It then offers these choices and waits for an answer before full translation:

- `A. Fine translation`: recommended for core references; higher quality with more time and token use.
- `B. Fast translation`: recommended for literature exploration; the simplest black-and-white layout with less time and token use, but no publication-level polishing target.
- `C. Custom`: specify deliverables, formatting, or quality/latency priorities.

Default deliverables:

1. Chinese translation `.docx`
2. English-Chinese bilingual `.docx`
3. Byte-identical copy of the original English PDF

If local artifacts need to be saved, follow the built-in `references/local-artifact-versioning.md` rules: create a new non-overwriting version folder under the current project's `任务成果` directory and place the deliverables there.

### Recommended Workflow

1. Read only page count, metadata, and a small sample of representative pages; inspect readily available device/system and model information.
2. Give rough fine- and fast-mode time ranges, then wait for the user's selection.
3. In fine mode, use `references/completeness-checklist.md`, a full source inventory, a separate polishing pass, and complete content/layout iteration.
4. In fast mode, use a lightweight coverage ledger, one batched translation pass, and a simple black-and-white single-column layout without reproducing the journal design.
5. In both modes, create Chinese and bilingual Word documents, archive the original English PDF, and render/inspect every page; fast mode iterates only for completeness and readability defects.
6. Use the verification script to assist final-package and source-PDF hash checks.

### Verification Script Example

```bash
python scripts/verify_translation_package.py \
  --source-pdf path/to/source.pdf \
  --original-copy path/to/original_copy.pdf \
  --docx path/to/chinese.docx \
  --docx path/to/bilingual.docx \
  --expected-pdf-pages 12 \
  --expected-images 8 \
  --expected-tables 3 \
  --expected-equations 5 \
  --report path/to/verification_report.json
```

The `--expected-pdf-pages`, `--expected-images`, `--expected-tables`, and `--expected-equations` values should come from the source inventory created before translation. Script results are only auxiliary evidence and do not replace manual page-by-page visual inspection.

## Input and Output Example

### Input

```text
source.pdf
```

The input should be a complete English academic paper PDF.

Example interaction after lightweight preflight:

```text
The paper is about 18 pages with mixed layout complexity. With the current device and model settings, the rough estimate is:
A. Fine translation: about 2.5-4.5 hours
B. Fast translation: about 45-90 minutes
C. Custom
Choose one mode. Network load, OCR quality, and complex layout repairs can change this range.
```

These times only demonstrate the output format. The actual estimate changes with the current paper and environment.

### Output

```text
任务成果/
└── 学术论文翻译_yyyyMMddHHmm_001_初版完整翻译_codex/
    ├── chinese.docx
    ├── bilingual.docx
    ├── original_copy.pdf
    └── verification_report.json
```

Actual filenames may be adjusted based on the paper title or user request, but the default deliverable types remain a Chinese Word document, an English-Chinese bilingual Word document, and the original English PDF copy. `verification_report.json` is created only when the verification script is run with `--report`.

## Real Limitations

- This skill describes the workflow and acceptance criteria Codex should follow for complete academic paper translation deliverables.
- The preflight time range is a low-cost rough estimate, not a completion-time guarantee. Scan quality, network load, difficult equations/tables, and layout repairs can change actual duration.
- Fast mode still requires complete, readable content, but it does not reproduce the journal layout or run a separate language-style polishing pass and should not be treated as publication-ready work.
- `scripts/verify_translation_package.py` only performs several mechanical checks for the final package. It does not automatically translate, automatically typeset, or automatically determine complete content coverage.
- Figure, table, equation, and page layout quality must be confirmed by inspecting the rendered final DOCX pages.
- Whether the archived English PDF is unchanged can be assisted by the script's SHA-256 hash comparison.
