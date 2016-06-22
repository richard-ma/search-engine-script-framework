# Google Crawler

## 安装

### Windows下安装

#### 安装python2.7

如果已经安装了python则可跳过此步骤。

请到这个链接下载：[Python Windows](https://www.python.org/downloads/release/python-2711/)

注意根据自己系统选择32位和64位版本。

#### 设置环境变量

##### 打开我的电脑->属性

![打开我的电脑->属性](./images/1.jpg)

##### 选择高级系统设置

![选择高级系统设置](./images/2.jpg)

##### 高级选项卡->环境变量

![高级选项卡->环境变量](./images/3.jpg)

##### 系统变量栏->Path

![系统变量栏->Path](./images/4.jpg)

##### 将C:\Python27\;C:\Python27\Scripts;加入变量值

![将C:\Python27\;C:\Python27\Scripts;加入变量值](./images/5.jpg)

### CentOS下安装

#### 安装pip

* yum install epel-release
* yum install python-pip
* yum install python-devel libffi-devel openssl-devel gcc unzip

### 升级pip并安装requests库

* pip install --upgrade pip
* pip install requests
* pip install pyopenssl ndg-httpsclient pyasn1

![升级pip并安装requests库](./images/pip.jpg)

## 使用

### 图形化界面

#### Windows

* 在`keywords`文件中每行一条关键字
* 可直接双击`search.bat`文件进行搜索
* 可直接双击`schedule.bat`文件进行定时执行

#### CentOS

* 在`keywords`文件中每行一条关键字
* `./search.sh`即可开始搜索
* `./schedule.sh`后面加三个时间即可定时运行，例如`./schedule.sh 12:00 13:00 14:00`

### 工作目录

先cd到程序所在目录（这里程序所在目录为D:\Projects\search_engine\)

### 命令格式

[python] search (search_engine) (keyword)

例如搜索关键字shoes:

[python] search googleshopping shoes

### 搜索过程截图

![搜索过程截图](./images/search.jpg)
