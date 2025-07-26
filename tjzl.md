本工具是一个将洛谷上题目下载到本地并转换为 HTML 格式的软件。

本工具目前处于测试阶段，**仅在 Linux 上进行过测试**。bug 反馈优先于 GitHub 上提 issue，其次可于讨论帖中联系我。

本工具**使用 GPL 协议开源**，在进行二创时注意 GPL 协议的条款。本文章使用 CC BY-NC-SA 4.0 许可证。

## 1. 下载与安装
建议通过 [GitHub](https://github.com/kongfx/lptp) 下载。如无法访问 GitHub，请使用[镜像站](https://kkgithub.com/kongfx/lptp)。

Linux 用户请直接克隆本仓库：
```shell
$ git clone https://github.com/kongfx/lptp.git # 或 kkgithub.com
```
以下操作均默认 Linux Shell 执行（bash-style，`$` 代表提示符）。

使用 `venv`：
```shell
$ python -m venv .venv # 创建
$ . .venv/bin/activate # 加入 venv
```
加入 `venv` 后提示符前将多出 `(.venv)` 提示。接下来安装依赖：
```shell
(.venv) $ pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
```
## 2. 首次使用
首次使用时先登录。验证码将于输入密码后自动弹出。
```shell
(.venv) $ python main.py --login luogu
欢迎使用洛谷题目导出系统。在第一次使用时请先登录您的洛谷账号。
如果您的账号设置了 2FA，请您在登录后手动修改 cookies.json 中的 __client_id。
请输入 UID、用户名或电子邮箱：<uid>
密码（不会显示）：
获取验证码中...
输入验证码：<验证码>
登录成功。
```
## 3. 使用教程
基本语法：
```plain
执行: main.py [-h] [-q] [--login] [-o OUTPUT] pid

参数:
  pid                           题目编号；

选项:
  -h, --help                    显示帮助；
  -q, --quiet                   静默输出；
  --login                       登录；
  -o OUTPUT, --output OUTPUT    指定输出文件，不存在时为题号。
```
用法举例：
```shell
$ python main.py P1001
```
会将 [A+B Problem](https://luogu.com.cn/problem/P1001) 下载并保存为 `P1001.html`。
## 4. 效果
