# smile自用机器人 V2
## 使用到的项目
* [node-gamedig](https://github.com/gamedig/node-gamedig)
* [magnet2torrent-js](https://github.com/Tsuk1ko/magnet2torrent-js)
* [aiocqhttp](https://github.com/nonebot/aiocqhttp)
* [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
## 功能
* 磁力链简单验车（查看磁力链资源名） 
* B站链接转换（还没做小程序的转换，懒）
* 游戏服务器状态查询（使用的GameDig）
* 天气查询 
> weather_api.py 
+ +  请前往 [openweathermap](https://openweathermap.org/api) 申请API TOKEN
```python 
python3 weather_api.py --position city_name
```
* 番剧日报 
> bangumi_api.py
```python 
python3 bangumi_api.py
```

## 食用
* npm install
* pip install -r requirements.txt
* 启动你的go-cqhttp，反向WS端口需于bot端口一致
* 推荐使用uvicorn启动bot，没有可以自己装
    * uvicorn --host 0.0.0.0 --port 5700 bot:bot.asgi
* 具体bot操作可以自己阅读bot.py
* 在Q群内高频发url或图片容易触发风控，但是不影响私聊，望周知
## Docker compose版本
* 构建镜像 
* ```docker build -t smilebot . ```
* 初次登陆/使用
* ```docker compose up -d && docker attach --sig-proxy=false smilebot```
* 后续使用
* ```docker compose up -d```
## todo
* 完善B站小程序的链接转换
* 完善食用文档
* 增加config文件控制参数
* 新增功能（或许
* 摆烂（x
