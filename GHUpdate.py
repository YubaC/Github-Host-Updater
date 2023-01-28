# 负责从raw.hellogithub.com/hosts获取HOST文件并更新到本地
# 流程为：先备份当前HOST文件，（备份到C:\Windows\System32\drivers\etc\hostsBackup\日期+时间）
# 然后从raw.hellogithub.com/hosts获取HOST文件
# 最后将获取到的HOST文件写入到本地HOST文件中
# 写入的位置为C:\Windows\System32\drivers\etc\hosts

import urllib.request
import os
import time

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 获取当前时间
def getNowTime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

# 备份当前HOST文件
def backupHost():
    print(getNowTime() + ' 开始备份当前HOST文件')
    hostPath = 'C:\Windows\System32\drivers\etc\hosts'
    # backupPath = 'C:\Windows\System32\drivers\etc\hosts.bak'
    backupDir = 'C:\Windows\System32\drivers\etc\hostsBackup\\'
    backupPath = os.path.join(backupDir, getNowTime().replace(':', '-').replace(' ', '_'))
    # 创建备份文件夹
    if not os.path.exists(backupDir):
        os.makedirs(backupDir)
    # 备份当前HOST文件
    if os.path.exists(hostPath):
        with open(hostPath, 'r', encoding="utf-8") as f:
            text = f.read()
            f.close()
        with open(backupPath, 'w', encoding="utf-8") as f:
            f.write(text)
            f.close()
        print(getNowTime() + ' 备份当前HOST文件成功')
    else:
        print(getNowTime() + ' 备份当前HOST文件失败，原因：当前HOST文件不存在')
    # **********以下为使用os.rename()方法备份HOST文件，已弃用**********
    # if os.path.exists(hostPath):
    #     if os.path.exists(backupPath):
    #         os.remove(backupPath)
    #     os.rename(hostPath, backupPath)
    #     print(getNowTime() + ' 备份当前HOST文件成功')
    # else:
    #     print(getNowTime() + ' 备份当前HOST文件失败，原因：当前HOST文件不存在')

# 获取HOST文件
def getHost():
    print(getNowTime() + ' 开始获取HOST文件')
    # url = 'https://raw.githubusercontent.com/racaljk/hosts/master/hosts'
    # url = 'https://raw.hellogithub.com/hosts'
    # 读取hostOrigion.txt文件，获取url
    with open('hostOrigion.txt', 'r', encoding="utf-8") as f:
        url = f.read()
        f.close()
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    print(getNowTime() + ' 获取HOST文件成功')
    return text

# 写入HOST文件
def writeHost(text):
    print(getNowTime() + ' 开始写入HOST文件')
    hostPath = 'C:\Windows\System32\drivers\etc\HOSTS'
    # hostPath = 'HOSTS'
    # 读取当前HOST文件，寻找开始和结束注释
    # 开始注释为：# BEGIN GitHub Host Start
    # 结束注释为：# END GitHub Host End
    with open(hostPath, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        f.close()
    
    # 从当前HOST文件中找到开始和结束注释的位置
    # 如果没有找到开始注释，则在文件末尾添加如下内容：
    # # Please DO NOT DELETE THESE LINES, or you will lose the hosts update from GitHub
    # # BEGIN GitHub Host Start
    # 获取到的Host文件
    # # END GitHub Host End
    start = 0
    end = 0
    for i in range(len(lines)):
        if lines[i].find('# GitHub Host Start') != -1:
            start = i
        if lines[i].find('# GitHub Host End') != -1:
            end = i
    if start == 0:
        lines.append('\n\n# Please DO NOT DELETE THESE LINES, or you will lose the hosts update from GitHub\n')
        lines.append('# GitHub Host Start\n')
        lines.append(text + '\n')
        lines.append('# GitHub Host End')
    else:
        lines[start + 1: end] = text
    # 写入HOST文件
    with open(hostPath, 'w', encoding="utf-8") as f:
        f.writelines(lines)
        f.close()
    print(getNowTime() + ' 写入HOST文件成功')
    # **********以下为直接写入HOST文件，已弃用**********
    # with open(hostPath, 'w') as f:
    #     f.write(text)
    # print(getNowTime() + ' 写入HOST文件成功')

# 主函数
def main():
    backupHost()
    text = getHost()
    writeHost(text)

if __name__ == '__main__':
    # 获取windows管理员权限
    if not is_admin():
        print('没有管理员权限，请重新运行程序并以管理员身份运行')
        sys.exit()
    print(is_admin())
    main()