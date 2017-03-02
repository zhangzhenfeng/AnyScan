## AnyScan

```
AnyScan一款正在开发的自动化渗透测试工具，能够将我们日常的一些重复、简单的工作搬到web界面里
让我们有更多的精力去做更加有技术性的工作。bbb
```

### 系统支持

```
Windows、Linux可自行选择，依赖包可根据系统类型自己下载
```

### 依赖软件
> [+] SQLMapAPI<br />
> [+] NMap<br />
> [+] Django 1.10.5 (1, 10, 5, u'final', 0)<br />
> [+] Python2.7<br />
> [+] MySQL5.5以上<br />
### Python库
> [+] paramiko<br />

### 安装步骤
> [+] 创建数据 anyscan <br />
> [+] 下载安装[Django](http://note.youdao.com/)<br />
> [+] 下载安装SQLMap源码Python版 [SQLMap](http://sqlmap.org/)<br />
> [+] 下载nmap安装 [NMap](https://nmap.org/)<br />
> [+] pip install paramiko <br />
> [+] 进入SQLMap源码目录，执行
> ```
> python sqlmapapi.py -s -H 127.0.0.1 -p 8889
> ```
> [+] 修改项目中的setting.py的数据库连接信息
>
> [+] 进入下载的AnyScan项目目录执行一下命令同步数据库，或者将项目根目录的sql文件导入anyscan数据库
> ```
> python manage.py makemigrations
> python manage.py migrate
> ```
> [+] 执行命令
> ```
> python manage.py runserver
> ```
> [+] 访问 [http://127.0.0.1:8000/AnyScanUI/index/](http://note.youdao.com/)