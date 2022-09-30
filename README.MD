# smile自用机器人 V2
## 使用到的项目
* [node-gamedig](https://github.com/gamedig/node-gamedig)
* [magnet2torrent-js](https://github.com/Tsuk1ko/magnet2torrent-js)
* [aiocqhttp](https://github.com/nonebot/aiocqhttp)
* [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
* [ngosang/trackerslist](https://github.com/ngosang/trackerslist)
* [枝网小作文](https://asoulcnki.asia/)
## 功能
* 磁力链简单验车（查看磁力链资源名） 
* B站链接转换
* 搜图（私聊，暂时支持saucenao&tracemoe）
* 游戏服务器状态查询（使用的GameDig）
* 天气查询
* 番剧日报 
* 枝网小作文查重

## 食用
* npm install 
* pip install -r requirements.txt
* 启动你的go-cqhttp，反向WS端口需于bot端口一致
* 推荐使用uvicorn启动bot，没有可以自己装
    * uvicorn --host 0.0.0.0 --port 5700 bot:bot.asgi
* 需要更换trackers源请自行在m2t.js更换
* 具体bot操作可以使用/helpme，私聊和群聊均可
* 天气模块请前往 [openweathermap](https://openweathermap.org/api) 申请API TOKEN,并填入config.py内
* 服务器查询需要自行配置且在bot.py中取消注释启用
* 在Q群内高频发url或图片容易触发风控，但是不影响私聊，望周知
## Docker compose版本
* 构建镜像 
* ```docker build -t docker_bot_projects```
* 初次登陆/使用
* ```docker compose up -d && docker attach --sig-proxy=false docker_bot_projects```
* 后续使用
* ```docker compose up -d```
## todo
* 完善食用文档
* 新增功能（或许
* 摆烂（x
