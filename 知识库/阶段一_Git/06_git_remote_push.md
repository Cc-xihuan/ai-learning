# git remote add + git push —— 推送到 GitHub

**级别**：🔴 必须会 | **面试官看你的代码就要靠这个**

## 一句话解释
把本地仓库的代码"推"到 GitHub 上，别人就能看到了。

## 类比
你在自己电脑上写日记（commit），不等于别人能看到。
`git push` = 拍照发朋友圈，大家才能看到。

## 整个流程
```
你电脑                                     GitHub
------                                     ------
写代码 → git add（进购物车）→ git commit（存档）→ git push（上传）
```

## 首次推送（新项目）
```bash
# 1. 告诉 Git：远程仓库地址是什么（一辈子一次）
git remote add origin https://github.com/你的用户名/仓库名.git

# 2. 把主分支改名为 main
git branch -M main

# 3. 推送
git push -u origin main
```

## 之后每次推送
```bash
git push
# 就这三个单词，因为 -u 已经绑定了默认远程仓库
```

## 什么时候用？
- 每次写完代码、commit 之后
- 养成习惯：下班前 push 一次
