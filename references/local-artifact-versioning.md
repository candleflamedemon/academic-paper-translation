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

## Non-Overwrite Rules

- Check the full target path before creating the version folder.
- If a candidate folder already exists, keep the task name and update summary, increment the version number, and check again.
- Do not delete, clear, rename, reuse, or overwrite any existing version folder under `任务成果`.
- Create a new version folder every time local artifacts are saved, even when the contents are similar to an earlier version.

## Completion Check

Before finishing, confirm that all current deliverables are inside the new version folder, the update summary accurately describes this version, the folder name follows the convention, previous versions were not modified, and the user is told the full path to the new artifact folder.
