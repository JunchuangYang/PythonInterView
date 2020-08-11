# Linux命令大全

![](https://www.linuxprobe.com/wp-content/uploads/2019/09/1-19.jpg)

作者：是瑶瑶公主吖

https://www.nowcoder.com/discuss/463682?source_id=profile_create&channel=1013

来源：牛客网

## Linux 常用命令

### 文件管理

| 命令    | 含义                         | 备注                                                         |
| ------- | ---------------------------- | ------------------------------------------------------------ |
| cat     | 连接文件并打印到标准输出设备 | -n 从 1 开始对输出编号、-b 类似 -n 但对空白行不编号          |
| chgrp   | 变更文件或目录的所属群组     | -f 不显示错误信息、-R 递归处理                               |
| chmod   | 更改文件权限                 | ugoa 分别表示拥有者、同组、其他人、所有人； rwx 分布表示可读、写、执行 |
| chown   | 更改文件拥有者               | 一般只有系统管理者 root 才有此权限                           |
| cmp     | 比较两个文件是否有差异       | -l 标出所有不同处                                            |
| file    | 辨识文件类型                 | -f 指定文件名、-v 显示版本信息                               |
| find    | 在指定目录下查找文件         | -type 指定文件类型、-name 指定文件名                         |
| ln      | 为文件在其它位置建立同步链接 | -s 软连接、-v 显示处理过程、-b 覆盖                          |
| less    | 查看文件                     | 查看前不会加载整个文件                                       |
| more    | 查看文件                     | 以页的形式显示，按空格显示下一页，b 显示上一页               |
| mv      | 为文件和目录改名或移动       | -i 询问覆盖、-f 不询问                                       |
| rm      | 删除文件或目录               | -i 删除前询问、-r 递归删除                                   |
| touch   | 修改文件或者目录的时间属性   | -a 改变读取时间、-m 改变修改时间                             |
| which   | 查找文件                     | -w 指定输出宽度、-V 显示版本信息                             |
| whereis | 查找文件                     | 只能查找二进制文件、源代码和 man 手册，一般文件的定位需要用 locate |
| cp      | 复制文件或目录               | -f 覆盖不提示、-i 覆盖提示、-l 不复制文件只生成链接          |
| read    | 从标准输入读取数值           | -n 指定输入长度、-p 指定提示信息                             |

------

### 文档编辑

| 命令  | 含义                 | 备注                                            |
| ----- | -------------------- | ----------------------------------------------- |
| ed    | 最简单的文本编辑程序 | 一次只能编辑一行                                |
| egrep | 在文件内查找字符串   | 与 grep -E 效果类似                             |
| grep  | 查找文件中的字符串   | -a 不忽略二进制、-A 显示行数、-i 忽略大小写     |
| look  | 查询单词             | -f 忽略字符大小写                               |
| sort  | 对文本文件内容排序   | -b 忽视空格、-c 检查是否已排序、-m 合并排序文件 |

------

### 文件传输

| 命令 | 含义                         | 备注                                |
| ---- | ---------------------------- | ----------------------------------- |
| ftp  | 文件传输                     | -v 显示执行过程、-n 不使用自动登录  |
| bye  | 中断 ftp                     |                                     |
| uuto | 将文件传送到远端的 UUCP 主机 | Unix-to-Unix Copy(UNIX至UNIX的拷贝) |

------

### 磁盘管理

| 命令  | 含义                     | 备注                                                         |
| ----- | ------------------------ | ------------------------------------------------------------ |
| cd    | 切换当前工作目录         | `~` 根目录、`.`  当前目录，`..` 上层目录。                   |
| df    | 显示文件系统磁盘使用情况 |                                                              |
| mkdir | 创建目录                 | -p 确保目录存在，不存在就创建                                |
| tree  | 以树状图列出目录内容     | -a 显示所有文件和目录、-d 显示目录名称而非内容               |
| rmdir | 删除空目录               | -p 如果删除子目录后成为空目录，一并删除                      |
| ls    | 显示工作目录下的内容     | -a 显示所有文件及目录、-l 显示文件权限，大小和拥有者等信息、-r 递归显示。 |

------

### 网络通讯

| 命令      | 含义                                  | 备注                                                         |
| --------- | ------------------------------------- | ------------------------------------------------------------ |
| telnet    | 远端登录                              | -a 尝试自动登录、-d 启动排错模式、-K 不自动登录              |
| netconfig | 设置网络环境                          |                                                              |
| nc        | 设置路由器                            | -g 设置网关、-G 设置来源路由器、-l 使用监听模式、-u 使用 UDP 协议 |
| httpd     | Apache 的 HTTP 服务器程序             | -d 指定服务器根目录、-f 指定配置文件                         |
| ifconfig  | 显示或设置网络设备                    | add 设置 IP 地址、del 删除 IP 地址、up 启动指定网络设备      |
| netstat   | 显示网络状态                          | -a 显示所有 socket、-c 持续列出网络状态、-t 显示 TCP 状况、-u 显示 UDP 状况 |
| ping      | 使用 ICMP，若远端主机无问题会得到回应 | -i 指定间隔秒数、-R 记录路由过程、-t 设置 TTL 大小           |
| tty       | 显示终端机连接标准输入设备的文件名称  | -s 不显示信息，只回传状态代码、-v 显示版本                   |
| write     | 传信息给其它使用者                    |                                                              |

------

### 系统管理

| 命令     | 含义                   | 备注                                            |
| -------- | ---------------------- | ----------------------------------------------- |
| adduser  | 新增使用者账号         | -e 指定使用期限                                 |
| date     | 显示或设定系统日期     | -s 设定时间、-v 显示版本                        |
| exit     | 退出目前的 shell 终端  |                                                 |
| sleep    | 将目前动作延迟一段时间 |                                                 |
| kill     | 删除执行中的程序或工作 | 1 重新加载进程、9 杀死进程、15 正常停止进程     |
| ps       | 显示当前进程的状态     | -A 列出所有进程、-u 指定用户、-w 加宽显示       |
| whois    | 查找并显示用户信息     |                                                 |
| whoami   | 显示自身用户名称       | 相当于 id -un 命令                              |
| who      | 显示系统中在线的使用者 | -q 只显示登入系统的账号名称和总人数             |
| shutdown | 关机                   | -r 重新启动、-c 取消关机、-n 立即关机           |
| top      | 实时显示进程状态       | -n 设置更新次数、-d 设置更新时间、-p 指定进程号 |

------

### 系统设置

| 命令   | 含义                     | 备注                                          |
| ------ | ------------------------ | --------------------------------------------- |
| clear  | 清除屏幕                 | -e 指定使用期限                               |
| rpm    | 管理套件                 | -a 查询所有套件、-d 只列出文本文件            |
| passwd | 更改使用者密码           | -d 删除密码、-l 停止账号使用、-S 显示密码信息 |
| time   | 测量指令消耗的时间和资源 | -o 将输出写入指定文档                         |

------

### 备份压缩

| 命令        | 含义                       | 备注                                                  |
| ----------- | -------------------------- | ----------------------------------------------------- |
| zip/unzip   | 压缩文件/解压缩            | 兼容类unix与windows，可以压缩多个文件或目录           |
| gzip/gunzip | 压缩文件/解压缩 gzip 文件  | 压缩单个文件，压缩率相对低，cpu开销低                 |
| tar         | 将多个文件打包成一个并压缩 | -z 调用 gzip 压缩、-j 调用 xz 压缩、-x 解压           |
| xz/unxz     | 压缩/解压缩 xz 文件        | 压缩单个文件，压缩率高，时间相对长，解压快，cpu开销高 |

**系统信息** 
arch 显示机器的处理器架构
uname -m 显示机器的处理器架构
uname -r 显示正在使用的内核版本 
dmidecode -q 显示硬件系统部件 - (SMBIOS / DMI) 
hdparm -i /dev/hda 罗列一个磁盘的架构特性 
hdparm -tT /dev/sda 在磁盘上执行测试性读取操作 
cat /proc/cpuinfo 显示CPU info的信息 
cat /proc/interrupts 显示中断 
cat /proc/meminfo 校验内存使用 
cat /proc/swaps 显示哪些swap被使用 
cat /proc/version 显示内核的版本 
cat /proc/net/dev 显示网络适配器及统计 
cat /proc/mounts 显示已加载的文件系统 
lspci -tv 罗列 PCI 设备 
lsusb -tv 显示 USB 设备 
date 显示系统日期 
cal 2007 显示2007年的日历表 
date 041217002007.00 设置日期和时间 - 月日时分年.秒 
clock -w 将时间修改保存到 BIOS 



**关机 (系统的关机、重启以及登出 )** 
shutdown -h now 关闭系统
init 0 关闭系统
telinit 0 关闭系统
shutdown -h hours:minutes & 按预定时间关闭系统 
shutdown -c 取消按预定时间关闭系统 
shutdown -r now 重启
reboot 重启
logout 注销 



**文件和目录** 
cd /home 进入 '/ home' 目录' 
cd .. 返回上一级目录 
cd ../.. 返回上两级目录 
cd 进入个人的主目录 
cd ~user1 进入个人的主目录 
cd - 返回上次所在的目录 
pwd 显示工作路径 
ls 查看目录中的文件 
ls -F 查看目录中的文件 
ls -l 显示文件和目录的详细资料 
ls -a 显示隐藏文件 
ls *[0-9]* 显示包含数字的文件名和目录名 
tree 显示文件和目录由根目录开始的树形结构
lstree 显示文件和目录由根目录开始的树形结构
mkdir dir1 创建一个叫做 'dir1' 的目录' 
mkdir dir1 dir2 同时创建两个目录 
mkdir -p /tmp/dir1/dir2 创建一个目录树 
rm -f file1 删除一个叫做 'file1' 的文件' 
rmdir dir1 删除一个叫做 'dir1' 的目录' 
rm -rf dir1 删除一个叫做 'dir1' 的目录并同时删除其内容 
rm -rf dir1 dir2 同时删除两个目录及它们的内容 
mv dir1 new_dir 重命名/移动 一个目录 
cp file1 file2 复制一个文件 
cp dir/* . 复制一个目录下的所有文件到当前工作目录 
cp -a /tmp/dir1 . 复制一个目录到当前工作目录 
cp -a dir1 dir2 复制一个目录 

cp -r dir1 dir2 复制一个目录及子目录
ln -s file1 lnk1 创建一个指向文件或目录的软链接 
ln file1 lnk1 创建一个指向文件或目录的物理链接 
touch -t 0712250000 file1 修改一个文件或目录的时间戳 - (YYMMDDhhmm) 



**文件搜索** 
find / -name file1 从 '/' 开始进入根文件系统搜索文件和目录 
find / -user user1 搜索属于用户 'user1' 的文件和目录 
find /home/user1 -name \*.bin 在目录 '/ home/user1' 中搜索带有'.bin' 结尾的文件 
find /usr/bin -type f -atime +100 搜索在过去100天内未被使用过的执行文件 
find /usr/bin -type f -mtime -10 搜索在10天内被创建或者修改过的文件 
find / -name \*.rpm -exec chmod 755 '{}' \; 搜索以 '.rpm' 结尾的文件并定义其权限 
find / -xdev -name \*.rpm 搜索以 '.rpm' 结尾的文件，忽略光驱、捷盘等可移动设备 
locate \*.ps 寻找以 '.ps' 结尾的文件 - 先运行 'updatedb' 命令 
whereis halt 显示一个二进制文件、源码或man的位置 
which halt 显示一个二进制文件或可执行文件的完整路径 



**挂载一个文件系统** 
mount /dev/hda2 /mnt/hda2 挂载一个叫做hda2的盘 - 确定目录 '/ mnt/hda2' 已经存在 
umount /dev/hda2 卸载一个叫做hda2的盘 - 先从挂载点 '/ mnt/hda2' 退出 
fuser -km /mnt/hda2 当设备繁忙时强制卸载 
umount -n /mnt/hda2 运行卸载操作而不写入 /etc/mtab 文件- 当文件为只读或当磁盘写满时非常有用 
mount /dev/fd0 /mnt/floppy 挂载一个软盘 
mount /dev/cdrom /mnt/cdrom 挂载一个cdrom或dvdrom 
mount /dev/hdc /mnt/cdrecorder 挂载一个cdrw或dvdrom 
mount /dev/hdb /mnt/cdrecorder 挂载一个cdrw或dvdrom 
mount -o loop file.iso /mnt/cdrom 挂载一个文件或ISO镜像文件 
mount -t vfat /dev/hda5 /mnt/hda5 挂载一个Windows FAT32文件系统 
mount /dev/sda1 /mnt/usbdisk 挂载一个usb 捷盘或闪存设备 
mount -t smbfs -o username=user,password=pass //WinClient/share /mnt/share 挂载一个windows网络共享 



**磁盘空间** 
df -h 显示已经挂载的分区列表 
ls -lSr |more 以尺寸大小排列文件和目录 
du -sh dir1 估算目录 'dir1' 已经使用的磁盘空间' 
du -sk * | sort -rn 以容量大小为依据依次显示文件和目录的大小 
rpm -q -a --qf '%10{SIZE}t%{NAME}n' | sort -k1,1n 以大小为依据依次显示已安装的rpm包所使用的空间 (fedora, redhat类系统) 
dpkg-query -W -f='${Installed-Size;10}t${Package}n' | sort -k1,1n 以大小为依据显示已安装的deb包所使用的空间 (ubuntu, debian类系统) 



**用户和群组** 
groupadd group_name 创建一个新用户组 
groupdel group_name 删除一个用户组 
groupmod -n new_group_name old_group_name 重命名一个用户组 
useradd -c "Name Surname " -g admin -d /home/user1 -s /bin/bash user1 创建一个属于 "admin" 用户组的用户 
useradd user1 创建一个新用户 
userdel -r user1 删除一个用户 ( '-r' 排除主目录) 
usermod -c "User FTP" -g system -d /ftp/user1 -s /bin/nologin user1 修改用户属性 
passwd 修改口令 
passwd user1 修改一个用户的口令 (只允许root执行) 
chage -E 2005-12-31 user1 设置用户口令的失效期限 
pwck 检查 '/etc/passwd' 的文件格式和语法修正以及存在的用户 
grpck 检查 '/etc/passwd' 的文件格式和语法修正以及存在的群组 
newgrp group_name 登陆进一个新的群组以改变新创建文件的预设群组 



**文件的权限 - 使用 "+" 设置权限，使用 "-" 用于取消** 
ls -lh 显示权限 
ls /tmp | pr -T5 -W$COLUMNS 将终端划分成5栏显示 
chmod ugo+rwx directory1 设置目录的所有人(u)、群组(g)以及其他人(o)以读（r ）、写(w)和执行(x)的权限 
chmod go-rwx directory1 删除群组(g)与其他人(o)对目录的读写执行权限 
chown user1 file1 改变一个文件的所有人属性 
chown -R user1 directory1 改变一个目录的所有人属性并同时改变改目录下所有文件的属性 
chgrp group1 file1 改变文件的群组 
chown user1:group1 file1 改变一个文件的所有人和群组属性 
find / -perm -u+s 罗列一个系统中所有使用了SUID控制的文件 
chmod u+s /bin/file1 设置一个二进制文件的 SUID 位 - 运行该文件的用户也被赋予和所有者同样的权限 
chmod u-s /bin/file1 禁用一个二进制文件的 SUID位 
chmod g+s /home/public 设置一个目录的SGID 位 - 类似SUID ，不过这是针对目录的 
chmod g-s /home/public 禁用一个目录的 SGID 位 
chmod o+t /home/public 设置一个文件的 STIKY 位 - 只允许合法所有人删除文件 
chmod o-t /home/public 禁用一个目录的 STIKY 位 



**文件的特殊属性 - 使用 "+" 设置权限，使用 "-" 用于取消** 
chattr +a file1 只允许以追加方式读写文件 
chattr +c file1 允许这个文件能被内核自动压缩/解压 
chattr +d file1 在进行文件系统备份时，dump程序将忽略这个文件 
chattr +i file1 设置成不可变的文件，不能被删除、修改、重命名或者链接 
chattr +s file1 允许一个文件被安全地删除 
chattr +S file1 一旦应用程序对这个文件执行了写操作，使系统立刻把修改的结果写到磁盘 
chattr +u file1 若文件被删除，系统会允许你在以后恢复这个被删除的文件 
lsattr 显示特殊的属性 



**打包和压缩文件** 
bunzip2 file1.bz2 解压一个叫做 'file1.bz2'的文件 
bzip2 file1 压缩一个叫做 'file1' 的文件 
gunzip file1.gz 解压一个叫做 'file1.gz'的文件 
gzip file1 压缩一个叫做 'file1'的文件 
gzip -9 file1 最大程度压缩 
rar a file1.rar test_file 创建一个叫做 'file1.rar' 的包 
rar a file1.rar file1 file2 dir1 同时压缩 'file1', 'file2' 以及目录 'dir1' 
rar x file1.rar 解压rar包 
unrar x file1.rar 解压rar包 
tar -cvf archive.tar file1 创建一个非压缩的 tarball 
tar -cvf archive.tar file1 file2 dir1 创建一个包含了 'file1', 'file2' 以及 'dir1'的档案文件 
tar -tf archive.tar 显示一个包中的内容 
tar -xvf archive.tar 释放一个包 
tar -xvf archive.tar -C /tmp 将压缩包释放到 /tmp目录下 
tar -cvfj archive.tar.bz2 dir1 创建一个bzip2格式的压缩包 
tar -jxvf archive.tar.bz2 解压一个bzip2格式的压缩包 
tar -cvfz archive.tar.gz dir1 创建一个gzip格式的压缩包 
tar -zxvf archive.tar.gz 解压一个gzip格式的压缩包 
zip file1.zip file1 创建一个zip格式的压缩包 
zip -r file1.zip file1 file2 dir1 将几个文件和目录同时压缩成一个zip格式的压缩包 
unzip file1.zip 解压一个zip格式压缩包 



**查看文件内容** 
cat file1 从第一个字节开始正向查看文件的内容 
tac file1 从最后一行开始反向查看一个文件的内容 
more file1 查看一个长文件的内容 
less file1 类似于 'more' 命令，但是它允许在文件中和正向操作一样的反向操作 
head -2 file1 查看一个文件的前两行 
tail -2 file1 查看一个文件的最后两行 
tail -f /var/log/messages 实时查看被添加到一个文件中的内容 



**文本处理** 

```
cat file1 file2 ... | command <> file1_in.txt_or_file1_out.txt general syntax for text manipulation using PIPE, STDIN and STDOUT 
cat file1 | command( sed, grep, awk, grep, etc...) > result.txt 合并一个文件的详细说明文本，并将简介写入一个新文件中 
cat file1 | command( sed, grep, awk, grep, etc...) >> result.txt 合并一个文件的详细说明文本，并将简介写入一个已有的文件中 
grep Aug /var/log/messages 在文件 '/var/log/messages'中查找关键词"Aug" 
grep ^Aug /var/log/messages 在文件 '/var/log/messages'中查找以"Aug"开始的词汇 
grep [0-9] /var/log/messages 选择 '/var/log/messages' 文件中所有包含数字的行 
grep Aug -R /var/log/* 在目录 '/var/log' 及随后的目录中搜索字符串"Aug" 
sed 's/stringa1/stringa2/g' example.txt 将example.txt文件中的 "string1" 替换成 "string2" 
sed '/^$/d' example.txt 从example.txt文件中删除所有空白行 
sed '/ *#/d; /^$/d' example.txt 从example.txt文件中删除所有注释和空白行 
echo 'esempio' | tr '[:lower:]' '[:upper:]' 合并上下单元格内容 
sed -e '1d' result.txt 从文件example.txt 中排除第一行 
sed -n '/stringa1/p' 查看只包含词汇 "string1"的行 
sed -e 's/ *$//' example.txt 删除每一行最后的空白字符 
sed -e 's/stringa1//g' example.txt 从文档中只删除词汇 "string1" 并保留剩余全部 
sed -n '1,5p;5q' example.txt 查看从第一行到第5行内容 
sed -n '5p;5q' example.txt 查看第5行 
sed -e 's/00*/0/g' example.txt 用单个零替换多个零 
cat -n file1 标示文件的行数 
cat example.txt | awk 'NR%2==1' 删除example.txt文件中的所有偶数行 
echo a b c | awk '{print $1}' 查看一行第一栏 
echo a b c | awk '{print $1,$3}' 查看一行的第一和第三栏 
paste file1 file2 合并两个文件或两栏的内容 
paste -d '+' file1 file2 合并两个文件或两栏的内容，中间用"+"区分 
sort file1 file2 排序两个文件的内容 
sort file1 file2 | uniq 取出两个文件的并集(重复的行只保留一份) 
sort file1 file2 | uniq -u 删除交集，留下其他的行 
sort file1 file2 | uniq -d 取出两个文件的交集(只留下同时存在于两个文件中的文件) 
comm -1 file1 file2 比较两个文件的内容只删除 'file1' 所包含的内容 
comm -2 file1 file2 比较两个文件的内容只删除 'file2' 所包含的内容 
comm -3 file1 file2 比较两个文件的内容只删除两个文件共有的部分 
```



**网络 - （以太网和WIFI无线） **

```
ifconfig eth0 显示一个以太网卡的配置 
ifup eth0 启用一个 'eth0' 网络设备 
ifdown eth0 禁用一个 'eth0' 网络设备 
ifconfig eth0 192.168.1.1 netmask 255.255.255.0 控制IP地址 
ifconfig eth0 promisc 设置 'eth0' 成混杂模式以嗅探数据包 (sniffing) 
dhclient eth0 以dhcp模式启用 'eth0' 
route -n show routing table 
route add -net 0/0 gw IP_Gateway configura default gateway 
route add -net 192.168.0.0 netmask 255.255.0.0 gw 192.168.1.1 configure static route to reach network '192.168.0.0/16' 
route del 0/0 gw IP_gateway remove static route 
echo "1" > /proc/sys/net/ipv4/ip_forward activate ip routing 
hostname show hostname of system 
host www.example.com lookup hostname to resolve name to ip address and viceversa
nslookup www.example.com lookup hostname to resolve name to ip address and viceversa
ip link show show link status of all interfaces 
mii-tool eth0 show link status of 'eth0' 
ethtool eth0 show statistics of network card 'eth0' 
netstat -tup show all active network connections and their PID 
netstat -tupl show all network services listening on the system and their PID 
tcpdump tcp port 80 show all HTTP traffic 
iwlist scan show wireless networks 
iwconfig eth1 show configuration of a wireless network card 
hostname show hostname 
host www.example.com lookup hostname to resolve name to ip address and viceversa 
nslookup www.example.com lookup hostname to resolve name to ip address and viceversa 
whois www.example.com lookup on Whois database 
```

