# bot.py
#  uvicorn --host 0.0.0.0 --port 5700 bot:bot.asgi
import re
from aiocqhttp import CQHttp, Event
# import config
from src.get_m2t_metainfo import getmetainfo
from src.search_anime import searchanime
from src.server_status import serverstatus
from src.get_b2p import changebilibili
from src.get_bangumi import get_bangumi
from aiocqhttp import Message, MessageSegment,api

bot = CQHttp(api_root='http://0.0.0.0:5700')


# 私聊
@bot.on_message('private')
async def _(event: Event):
    # B站link转图文
    if 'bilibili.com' in event.message:
        await changebilibili(bot, event)
    elif 'b23.tv' in event.message:
        await changebilibili(bot, event)
    # 磁力链搜索，发就行
    elif 'magnet:\?' in event.message:
        pattern_m = re.compile(r'magnet:\?xt=urn:btih:(.*)', re.I)
        magnet = re.findall(pattern_m,event.message)
        await getmetainfo(bot, event)
    # 番剧搜索，直接私聊发送图片即可
    elif 'CQ:image' in event.message:
        await searchanime(bot, event)
    elif event.message == '/番剧':
        await get_bangumi(bot, event)
    elif '/天气' in event.message:
        await get_bangumi(bot, event)
    # 服务器状态查询，指令：服务器状态+对应游戏服务器缩写
    # pattern_s = re.compile(r'服务器状态(.*)', re.I)
    # server = re.findall(pattern_s,event.message)
    # if server:
    #     await serverstatus(bot, event)


# 群聊  
@bot.on_message('group')
async def handle_msg(event):
    # B站link转图文
    if 'bilibili.com' in event.message:
        await changebilibili(bot, event)
    if 'b23.tv' in event.message:
        await changebilibili(bot, event)
    # 磁力链搜索
    pattern_m = re.compile(r'magnet:\?xt=urn:btih:(.*)', re.I)
    magnet = re.findall(pattern_m,event.message)
    if magnet:
        # 设为精华消息
        await bot.api.set_essence_msg(message_id = event.message_id)
        # 群聊转私聊，天天风控看着烦，需要开启群内允许私聊
        await getmetainfo(bot, event)


# bot.run(host='0.0.0.0', port=8080)