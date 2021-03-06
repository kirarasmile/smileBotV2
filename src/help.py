import requests
import json
import config
from aiocqhttp import MessageSegment

# K = C + 273.15
async def get_help(bot, event):
    img = MessageSegment.image('https://s3.bmp.ovh/imgs/2022/04/02/1ceb5fc0f33672bf.jpg')
    await bot.send(event, message=  img
                                + '帮助列表：\n'\
                                + '搜索番剧截图：直接私聊图片即可；\n'\
                                + '磁力链接识别：直接发送磁力链接，注意格式，在群内发送bot会自动私聊；\n'\
                                + '获取天气：/天气 城市拼音，注意空格，举例：/天气 guangzhou。\n'\
                                + '获取番剧更新列表：发送 /番剧；\n'\
                                + 'B站链接转换成图文：直接发送link；\n'\
                                + '服务器状态查询：服务器状态+对应服务器名。'
                                 )
    return 0