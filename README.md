# Academic Paper Translation

`academic-paper-translation` 是一个 Codex 技能，用于把英文**学术论文 PDF**制作成完整的中文译文版和中英对照版 Word 文档，并保留一份与原文件字节一致的英文 PDF 副本。

它适用于完整论文级别的翻译交付，不适用于短段落摘译、普通非学术文本翻译，也不是独立的命令行自动翻译程序。

## 解决什么问题

英文论文翻译常见的问题不是只把正文翻成中文，而是容易遗漏或破坏论文中的结构化内容，例如图、表、公式、题注、脚注、参考文献、声明、附录和补充材料提示。

本技能提供一套面向完整论文交付的工作流程，要求在翻译前建立源文件清单，在翻译和排版后进行覆盖性核对，并通过渲染检查确认最终 Word 文档中没有内容缺失、图像裁切、表格断裂、公式错误或页面重叠等问题。

## 主要功能

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
└── scripts/verify_translation_package.py
```

使用该技能完成论文翻译时，还需要 Codex 环境中可用的 PDF 处理能力和 Word 文档生成/渲染能力。校验脚本依赖 Python，并使用 `pypdf` 读取 PDF 页数。

## 使用方法

在 Codex 中提供一篇完整的英文论文 PDF，并明确调用该技能，例如：

```text
Use $academic-paper-translation to translate this English academic paper into complete Chinese and bilingual editions and archive the unchanged original.
```

默认交付物包括：

1. 中文译文版 `.docx`
2. 中英对照版 `.docx`
3. 与源文件字节一致的英文 PDF 副本

如果需要将结果保存为本地成果，应遵守本技能内置的 `references/local-artifact-versioning.md`：在当前项目的 `任务成果` 目录下创建新的、不覆盖旧版本的版本子目录，并把本次交付物放入其中。

### 推荐工作流程

1. 提取 PDF 文本并渲染每一页。
2. 建立源文件清单，记录页数、章节、图表、公式、脚注、参考文献和所有结尾材料。
3. 按 `references/completeness-checklist.md` 维护一对一覆盖核对。
4. 完成忠实翻译，统一术语和缩略语。
5. 重建中文版和中英对照版 Word 文档。
6. 渲染两个 DOCX 并逐页检查页面、图表、公式和长表格。
7. 使用校验脚本辅助检查最终包。

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
- `scripts/verify_translation_package.py` 只负责最终包的若干机械检查，不负责自动翻译、自动排版或自动判断所有内容是否完整。
- 文档中图像、表格、公式和页面布局是否合格，必须通过最终 DOCX 渲染后的逐页检查确认。
- 英文 PDF 副本是否未被修改，可通过脚本中的 SHA-256 哈希比较辅助确认。

---

# Academic Paper Translation

`academic-paper-translation` is a Codex skill for turning an English academic paper PDF into a complete Chinese-only Word document, an English-Chinese bilingual Word document, and an unchanged byte-identical copy of the original English PDF.

It is intended for full-paper academic translation deliverables. It is not intended for short excerpt translation, ordinary non-academic prose translation, and it is not a standalone command-line automatic translation program.

## Problem Solved

Academic paper translation is not only about translating the main text. Important structured content can easily be omitted or damaged, including figures, tables, equations, captions, footnotes, references, declarations, appendices, and supplementary-data notices.

This skill defines a workflow for complete paper-level delivery: build a source inventory before translation, maintain a coverage check after translation and assembly, and verify rendered Word pages so the final documents do not lose content, crop figures, break tables, corrupt equations, or overlap page elements.

## Main Features

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
└── scripts/verify_translation_package.py
```

Paper translation with this package also requires PDF handling capability and Word document creation/rendering capability in the Codex environment. The verification script depends on Python and uses `pypdf` to read PDF page counts.

## Usage

Provide a complete English academic paper PDF in Codex and invoke the skill explicitly, for example:

```text
Use $academic-paper-translation to translate this English academic paper into complete Chinese and bilingual editions and archive the unchanged original.
```

Default deliverables:

1. Chinese translation `.docx`
2. English-Chinese bilingual `.docx`
3. Byte-identical copy of the original English PDF

If local artifacts need to be saved, follow the built-in `references/local-artifact-versioning.md` rules: create a new non-overwriting version folder under the current project's `任务成果` directory and place the deliverables there.

### Recommended Workflow

1. Extract PDF text and render every page.
2. Build a source inventory covering pages, sections, figures, tables, equations, footnotes, references, and all end matter.
3. Maintain a one-to-one coverage check using `references/completeness-checklist.md`.
4. Translate faithfully and keep terminology and abbreviations consistent.
5. Reconstruct the Chinese-only and English-Chinese bilingual Word documents.
6. Render both DOCX files and inspect pages, figures, equations, and long tables.
7. Use the verification script as an auxiliary final-package check.

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
- `scripts/verify_translation_package.py` only performs several mechanical checks for the final package. It does not automatically translate, automatically typeset, or automatically determine complete content coverage.
- Figure, table, equation, and page layout quality must be confirmed by inspecting the rendered final DOCX pages.
- Whether the archived English PDF is unchanged can be assisted by the script's SHA-256 hash comparison.
