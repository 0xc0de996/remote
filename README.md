# 远程观看桌面工具

client可在server端无感知的情况远程观看server的电脑桌面

## 前提

1. server和client处于同一局域网且能够ping通，若处于同一局域网但ping不同则需要关闭防火墙
 
2. server和client安装好[python](www.python.org)，并将python目录添加到环境变量中

3. server端和client执行`pip install -r requirements.txt`

## server使用步骤

**启动：** server端执行`pythonw server.py {ip}
{port}`，其中ip为client能ping通的地址，port为开放的端口号，端口号不能被其他进程占用

**退出：** 在任务管理器里杀死python进程

## client使用步骤

**启动：** client端执行`python client.py {ip} {port}`，其中ip为server的地址，port为开放的端口号

**退出：** 按q退出

