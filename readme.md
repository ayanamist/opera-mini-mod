上传客户端
==========
Google App Engine
-----------------
**用这个服务端需要手机root**
进入GAE目录后，修改app.yaml里的your-id为申请到的。然后上传。

修改手机hosts文件，把your-id.appspot.com域名指向www.g.cn的任意一个IP，重启手机（否则hosts不生效）

mobile.twitter.com仍然不能用，因为Opera Mini服务器会把访问它的客户端IP带过去，Twitter那边检测到是GAE的请求，就会提示Rate Limit Exceeded。

这种方法获取到的url是http://your-id.appspot.com/ 下面备用。

DotCloud
--------
进入dotcloud目录，上传代码。

这种方法在上传后会自动显示获取到的url。

*************************************
修改Opera Mini
==============
用apktools打开apk文件

进入smali目录，打开aq.smali（或ap.smali） b.2.smali g.smali

替换所有http://为上面获取到的url，双斜线后面带内容都都不用动

替换所有socket://为socket://you_cant_use让socket连接无效化

用apktools打包回apk，再用autosigner签名

已经装过Opera Mini的，用Titanium Backup备份后卸载（因为签名不匹配不能覆盖安装）。

安装刚才修改好的apk文件。启动后即可使用。之前安装过Opera Mini的可以用Titanium Backup把Data给恢复过去，书签什么的就不会丢了。

注意选项里的连接，只能用HTTP，不能用HTTP/Socket（因为Socket被屏蔽了），影响主要是ajax支持变差了。
