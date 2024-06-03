# 项目简介

* 本项目是基于[AnkiKong大佬开源的项目](https://github.com/AnkiKong/picacomic)编写的,仅供技术研究使用,请勿用于其他用途,有问题可以提issue
* 可以fork这个项目,根据[api文档](https://www.apifox.cn/apidoc/shared-44da213e-98f7-4587-a75e-db998ed067ad/doc-1034189)自行开发功能
* 麻烦给个star支持一下:heart:



新增了环境变量 `PACKAGE_TYPE`, 参数为 True 和 False
设置为True时, 会根据漫画名称压缩成zip包, 以供 Komga 等漫画库 使用, 也会删除comics文件夹 ( 避免docker容器占用过多硬盘 )

```python
# main.py
if os.environ.get("PACKAGE_TYPE", "False") == "True":
    # 打包成zip文件, 并删除旧数据
    zip_subfolders('./comics', './output')
    shutil.rmtree('./comics')
```

新增了环境变量 `REQUEST_PROXY`, 这样下载图片时允许使用代理了
```python
# client.py
proxy = os.environ.get("REQUEST_PROXY")
if proxy:
    proxies = {'http': proxy, 'https': proxy}
else:
    proxies = None
response = self.__s.request(method=method, url=url, verify=False, proxies=proxies, **kwargs)
return response
```

新增了环境变量 `BARK_URL`, bark消息通知
  允许打包完成 or 下载完成发送自定义消息, 例: `https://api.day.app/{your_keys}/picacg下载成功`
```python
# main.py
if os.environ.get("BARK_URL"):
    # 发送消息通知
    request.get(os.environ.get("BARK_URL"))
```

# git actions

*  fork本仓库
*  新增Actions secrets

| secret          | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| PICA_SECRET_KEY | [AnkiKong提供的secret_key](https://zhuanlan.zhihu.com/p/547321040) |
| PICA_ACCOUNT    | 哔咔登录的账号                                               |
| PICA_PASSWORD   | 哔咔登录的密码                                               |
| EMAIL_ACCOUNT   | 接收漫画的邮箱                                               |
| BARK_URL        | 允许打包完成 or 下载完成发送自定义消息 例: `https://api.day.app/{your_keys}/picacg下载成功` |
|                 |                                                              |
| GIT_TOKEN       | [参考这篇文章](http://t.zoukankan.com/joe235-p-15152380.html),只勾选repo的权限,Expiration设置为No Expiration |

<img src="https://raw.githubusercontent.com/lx1169732264/Images/master/Actions%20secrets.png" width = "700" height = "350" alt="图片名称" align=center />



* 打开fork项目的workFlow开关

<img src="https://raw.githubusercontent.com/lx1169732264/Images/master/enableWorkFlow.png" width = "700" height = "350" alt="图片名称" align=center />

* 点击pica_crawler_actions.yml,编辑git actions. 写了注释的配置项,都可以根据需求改动

<img src="https://raw.githubusercontent.com/lx1169732264/Images/master/gitActions.png" width = "700" height = "350" alt="图片名称" align=center />


* 手动触发一次,测试下能不能跑通

<img src="https://raw.githubusercontent.com/lx1169732264/Images/master/runWorkFlow.png" width = "500" height = "200" alt="图片名称" align=center />


**成功运行的截图:**   
<img src="https://raw.githubusercontent.com/lx1169732264/Images/master/%E6%88%90%E5%8A%9F%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE.png" width = "700" height = "350" alt="图片名称" align=center />

* 成功运行后,可以在这里下载到漫画的压缩包. 如果配置了邮箱推送功能,还可以查收邮件里的附件

<img src="https://raw.githubusercontent.com/lx1169732264/Images/master/pica-Artifacts.png" width = "700" height = "350" alt="图片名称" align=center />



# 部分漫画不会被下载的原因
排行榜/订阅的漫画会受到以下过滤逻辑的影响,**收藏夹则不会**(如果下载到本地后文件丢失了,可以通过放入收藏夹把它全量下载下来)


### 过滤重复下载

downloaded.txt文件记录了已下载的漫画id, run_time_history.txt文件记录了每次运行的时间.   
**排行榜上已下载过的漫画会触发增量下载,跳过曾下载过的章节**,其余所有情况都是全量下载所有章节.      
每次运行代码后,都会通过git actions的指令提交代码,保存本次的运行结果.`GIT_TOKEN`配置错误将导致提交代码失败,这会导致漫画被重复下载和推送         



### 过滤分区

支持通过分区自定义下载逻辑. 

git actions配置文件的``CATEGORIES``配置项可以配置0~n个哔咔的分区, 配置为空则代表不过滤  

``CATEGORIES_RULE``可以配置为 INCLUDE: 包含任意一个分区就下载  EXCLUDE: 包含任意一个分区就不下载

> 部分漫画只打上了'短篇'/'长篇'这样单个分区,在配置为``INCLUDE``时,建议把比较常见的分区给填上,不然容易匹配不到漫画


### 订阅的时间范围
对于订阅的漫画,如果 当天 - 订阅漫画的上传日 > `SUBSCRIBE_DAYS`,这本漫画将不再被下载

# CHANGELOG

| 日期       | 说明        |
| ---------- | ----------- |
| 2023/01/06 | git actions |



