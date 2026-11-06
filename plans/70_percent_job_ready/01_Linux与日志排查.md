# 模块 1：Linux 与日志排查

目标：达到测试岗位“能登录服务器、找文件、看日志、查进程和端口、收集证据”的程度。无需学习内核编程、复杂 Shell、系统运维架构。

建议环境：WSL/Ubuntu 或真实 Linux。Git Bash 只适合最初的路径和文件命令，进程、服务、权限和端口部分应在真正的 Linux 环境完成。

## 一、必须掌握的理论

### 1. 路径与目录

- `/`：根目录；`~`：当前用户主目录；`.`：当前目录；`..`：上一级目录。
- 绝对路径从 `/` 开始；相对路径从当前位置开始。
- 常见目录：`/etc` 配置、`/var/log` 日志、`/home` 用户文件、`/tmp` 临时文件、`/usr` 应用和库。

常用命令：

```bash
pwd
ls
ls -lah
cd /path
cd ..
cd ~
```

### 2. 文件与目录操作

```bash
mkdir test-lab
touch app.log
cp source.txt backup.txt
mv old.txt new.txt
rm file.txt
rm -r directory
find . -name "*.log"
```

删除前必须先用 `pwd`、`ls` 和明确路径确认目标。测试岗位最危险的不是不会删除，而是在错误目录执行删除。

### 3. 查看文本和日志

```bash
cat app.log
less app.log
head -n 20 app.log
tail -n 50 app.log
tail -f app.log
grep "ERROR" app.log
grep -n -i "timeout" app.log
grep -C 3 "order_id=1001" app.log
```

- `tail -f` 用于实时追踪新增日志。
- `grep -n` 显示行号，`-i` 忽略大小写，`-C 3` 显示命中行前后各三行。
- 排障不是只搜 `ERROR`，还要按时间、请求 ID、用户 ID、订单号串起上下文。

### 4. 管道与重定向

```bash
grep "ERROR" app.log | tail -n 20
command > output.txt
command >> output.txt
command 2> error.txt
```

- `|` 把前一个命令的输出交给后一个命令。
- `>` 覆盖文件，`>>` 追加文件；使用 `>` 前必须确认不会覆盖重要内容。

### 5. 进程和服务

```bash
ps -ef
ps -ef | grep python
top
kill PID
kill -9 PID
systemctl status service-name
journalctl -u service-name --since "10 minutes ago"
```

- 普通 `kill` 先请求进程正常退出；`kill -9` 是强制终止，只在普通终止无效且确认影响后使用。
- `systemctl` 和 `journalctl` 需要使用 systemd 的 Linux 环境，Git Bash 不支持。

### 6. 端口与网络

```bash
ss -lntp
ss -lntp | grep 8000
curl -i http://127.0.0.1:8000/health
curl -v http://127.0.0.1:8000/health
ping -c 4 example.com
```

排查顺序：域名是否解析 → 网络是否可达 → 端口是否监听 → HTTP 是否有响应 → 响应是否符合预期。

### 7. 权限

`ls -l` 的权限分为所有者、所属组、其他用户三组，每组含读 `r`、写 `w`、执行 `x`。

```bash
chmod u+x run.sh
chmod 640 config.yaml
chown user:group file
```

测试岗位需要看懂权限问题，不要求背所有数字组合。不要随意使用 `chmod 777` 掩盖问题。

### 8. 压缩与传输

```bash
tar -czf logs.tar.gz logs/
tar -xzf logs.tar.gz
scp logs.tar.gz user@host:/tmp/
```

传输日志前先确认是否包含账号、Token、手机号等敏感信息。

## 二、理论验收题

1. `/`、`~`、`.`、`..` 分别表示什么？
2. 绝对路径与相对路径有什么区别？各举一个例子。
3. 为什么执行文件操作前要先运行 `pwd`？
4. `ls -lah` 比 `ls` 多提供什么信息？
5. `cat`、`less`、`tail -f` 分别适合什么场景？
6. 如何查找当前目录及子目录内所有 `.log` 文件？
7. 如何找出日志中包含 `ERROR` 的行并显示行号？
8. 如何查看订单号 `1001` 命中行的上下文？
9. `>` 与 `>>` 的区别是什么？哪个可能覆盖文件？
10. 管道 `|` 的作用是什么？
11. 如何查找 Python 进程？为什么 `grep` 自己也可能出现在结果中？
12. 普通 `kill` 与 `kill -9` 有什么区别？
13. 服务访问失败时，进程、端口和 HTTP 三层分别怎么检查？
14. `404` 与“端口没有监听”有什么本质区别？
15. `rwxr-x---` 表示哪些用户拥有哪些权限？
16. 为什么不应该遇到权限问题就直接 `chmod 777`？
17. 如何把 `logs/` 打包成 `logs.tar.gz`？
18. 为什么日志传给他人前要做脱敏检查？

## 三、实操验收

在 Linux 环境中完成并保存命令与输出：

1. 创建 `~/qa-linux-lab/logs`。
2. 创建 `app.log`，写入至少 10 行包含 INFO、WARN、ERROR、时间和 request_id 的模拟日志。
3. 使用 `grep` 找出 ERROR，并显示行号与前后两行。
4. 使用管道只显示最后两条 ERROR。
5. 启动一个本地 HTTP 服务，确认其进程和监听端口。
6. 使用 `curl -i` 访问正常路径和不存在路径，比较状态码。
7. 停止服务，再次检查端口并说明差异。
8. 将日志目录打包为 `logs.tar.gz`。

## 四、验收项目：服务无法访问排障记录

场景：开发说“服务已经启动”，但浏览器访问失败。

必须产出 `linux_service_incident.md`，包含：

- 现象和时间。
- 使用过的命令及关键输出。
- 进程是否存在。
- 端口是否监听。
- `curl` 得到的是连接失败、4xx 还是 5xx。
- 日志中的关键证据。
- 根因、临时处理、长期建议。

通过标准：别人只看记录就能复现你的排查顺序；结论必须由证据支持，不能只写“重启后好了”。
