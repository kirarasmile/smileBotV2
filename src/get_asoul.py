import requests
import json
from aiocqhttp import MessageSegment

async def get_asoul(bot, event):
    try:
        url = 'https://asoulcnki.asia/v1/api/check'
        text_dict = {'text': event.message}
        text_str = json.dumps(text_dict)
        res = requests.post(url, data=text_str)
        res_data = json.loads(res.text)
        # print(res.text)
        rate = res_data['data']['rate']
        if rate == 1:
            await bot.send(event, message='枝网查重100%，纯纯滴小作文小偷！')
        elif rate > 0.7:
            # reply_url = res_data['data']['related'][0]['reply_url']
            reply_rate = res_data['data']['related'][0]['rate']
            await bot.send(event, message='检测到小作文，一眼丁真枝网报告：\n' \
                                            + '小作文重复率：' + str(rate) + '\n' \
                                            + '从评论复制占比：' + str(reply_rate))
    except Exception as e:
        await bot.send(event, '枝网查重寄啦 \n'+str(e))