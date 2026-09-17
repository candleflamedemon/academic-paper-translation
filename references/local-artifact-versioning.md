# Local Artifact Versioning

Use this reference only when the translation task needs to save generated deliverables, exports, or copies as local project artifacts. Pure conversation or tasks that do not create local files do not need an artifact directory.

## Save Location

1. Treat the workspace root for the current task as the project root.
2. Use a `任务成果` folder under that project root. Create it only if it does not already exist.
3. For every artifact save, create a new version subfolder under `任务成果`.
4. Put newly generated deliverables, exported files, and artifact copies in that version subfolder. If the user explicitly asks to modify an existing project file in place, modify that existing file at its original path.

## Folder Naming

Use this format:

```text
任务名称简介_yyyyMMddHHmm_任务迭代版本号_版本更新简介_codex
```

- `任务名称简介`: a short Chinese task name. Remove Windows-illegal filename characters, trailing spaces, and trailing periods. Replace underscores with hyphens.
- `yyyyMMddHHmm`: the local machine time when preparing to save final artifacts, using a 12-digit year-month-day-hour-minute format.
- `任务迭代版本号`: at least three digits. Start a new task at `001`. For an explicit continuation, scan matching prior folders ending in `_codex`, take the largest version number, and add one.
- `版本更新简介`: a short, specific Chinese summary of what this version adds or changes. Do not leave it blank or use vague labels such as only `更新`, `优化`, or `修改`.
- `codex`: fixed suffix.

## Deliverable File Naming

Before writing the translation package, identify the English paper title displayed in the paper itself and translate it faithfully into natural Chinese. If embedded PDF metadata conflicts with the displayed title, prefer the displayed title. Use the resulting `中文标题译文` as the shared filename stem for the package:

```text
<中文标题译文>_中文译文版.docx
<中文标题译文>_中英对照版.docx
<中文标题译文>_英文原文.pdf
<中文标题译文>_校验报告.json   # only when a report is generated
```

- Use a title translation, not a topic summary or an invented replacement title.
- Remove control characters and replace filename-illegal characters such as `< > : " / \\ | ? *` with natural Chinese punctuation, a space, or a hyphen. Collapse repeated whitespace and trim trailing spaces and periods.
- Prefer the complete translated title. If the title exceeds 80 characters or the absolute output path risks the platform path limit, shorten it to a clear, distinctive 40–60-character Chinese title while preserving the paper's main subject and differentiating terms. Use the same shortened stem for every file in the package.
- Keep the edition suffixes exactly as shown so files remain distinguishable in search results and file explorers.
- An explicit user-supplied filename or naming scheme takes precedence. Otherwise, generic names such as `chinese.docx`, `bilingual.docx`, and `original_copy.pdf` are not acceptable defaults.
- Renaming the archived PDF is allowed because its byte content remains unchanged; the later hash check must still match it to the source PDF.

## Non-Overwrite Rules

- Check the full target path before creating the version folder.
- If a candidate folder already exists, keep the task name and update summary, increment the version number, and check again.
- Do not delete, clear, rename, reuse, or overwrite any existing version folder under `任务成果`.
- Create a new version folder every time local artifacts are saved, even when the contents are similar to an earlier version.

## Completion Check

Before finishing, confirm that all current deliverables are inside the new version folder, the update summary accurately describes this version, the folder name follows the convention, previous versions were not modified, and the user is told the full path to the new artifact folder.
