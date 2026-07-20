# git status —— 查看仓库状态

**级别**：🔴 必须会 | **每天用几十次**

## 一句话解释
随时问 Git："管家，现在什么情况？"

## 类比
你是老板，走进办公室问秘书："最近有什么事？"
秘书告诉你三件事：
1. 哪些文件改了但我还没存档（红色）
2. 哪些文件已经准备好存档了（绿色）
3. 有没有新文件我根本不认识（Untracked）

## 三种状态
| git status 显示 | 意思 | 下一步 |
|-----------------|------|--------|
| **Untracked files**（红色） | Git 不认识这些新文件 | `git add` 告诉 Git 管它们 |
| **Changes not staged for commit**（红色） | Git 认识但文件改过了，还没标记要存 | `git add` 标记这些改动 |
| **Changes to be committed**（绿色） | 已标记，下次 commit 会存 | `git commit` 存档 |

## 用法
```bash
git status
```
任何不确定的时候，先敲这个看看。
