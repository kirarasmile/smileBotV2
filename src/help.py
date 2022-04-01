import requests
import json
import config

# K = C + 273.15
async def get_help(bot, event):
    await bot.send(event, message= '帮助列表：\n'\
                                + '搜索番剧截图：直接私聊图片即可；\n'\
                                + '磁力链接识别：直接发送磁力链接，注意格式；\n'\
                                + '获取天气：/天气 城市拼音，注意空格，举例：/天气 guangzhou。\n'\
                                + '获取番剧更新列表：发送 /番剧；\n'\
                                + 'B站链接转换成图文：直接发送link；\n'\
                                + '服务器状态查询：服务器状态+对应服务器名。'
                                 )