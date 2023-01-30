# Github Host Updater

~~GitHub出了问题？那当然是右上45°敲打它直到它恢复正常啊~~

<img width="300px" src="icon.svg" alt="Icon">

## 概述

一个用于自动更新GitHub的HOST的小工具，可以在一定程度上解决GitHub连接不上、卡顿的问题，只需在需要的时候运行一次即可。

**使用该工具前需要手动删除原HOSTS文件内您手动添加的与GitHub相关的设置项。** 如果您之前没有修改过HOSTS文件请忽略这句话。

## 运行

直接克隆仓库或下载Release。全部解压后双击`updateHOST.bat`以运行程序。

本程序无需安装。

## 一些细节

每次更改HOSTS文件前，程序都会把当前的HOSTS文件备份到`C:\Windows\System32\drivers\etc\hostsBackup\`文件夹下，并重命名为`年-月-日_时-分-秒`。

HOSTS源文件来自于[https://raw.hellogithub.com/hosts](https://raw.hellogithub.com/hosts)。

您也可以自己修改HOSTS源文件，只要修改`hostOrigion.txt`（Release为`scripts\hostOrigion.txt`）内的链接即可。

首次运行后将会在HOSTS文件内部添加如下的段落：

```
# Please DO NOT DELETE THESE LINES, or you will lose the hosts update from GitHub
# GitHub Host Start
...
# GitHub Host End
```

之后每次运行工具只会修改`...`处的内容，而不会修改HOSTS文件的其它部分。
