import re, requests, time
from aiocqhttp import MessageSegment
async def changebilibili(bot, event):
    data = event.message.replace('\\', '')
    data = data.replace('/', '')
    try:
        if 'www.bilibili.comvideo' in data:
            pattern_b = re.compile(r'www.bilibili.comvideo(.*)\?|www.bilibili.comvideo(.*)', re.I)
            bid_long = re.findall(pattern_b,data)
            for i in bid_long[0]:
                if i:
                    bid = i
        elif 'b23.tv' in data:
            # pattern_b = re.compile(r'b23.tv/(.*)/\?spm_id|b23.tv/(.*)', re.I)
            pattern_b = re.compile(r'b23.tv(.*)\?|b23.tv(.*)', re.I)
            bid_short = re.findall(pattern_b,data)
            for i in bid_short[0]:
                if i:
                    bid_short = i
            data_short = requests.get('https://b23.tv/'+bid_short)
            pattern_short = re.compile(r'https://www.bilibili.com/video/(.*?)/">', re.I)
            try:
                if bid_short.text:
                    bid = re.findall(pattern_short,data_short.text)[0]
                else:
                    time.sleep(4)
                    bid = re.findall(pattern_short,data_short.text)[0]
            except Exception as e:
                await bot.send(event, '无法解析该短链接 \n'+str(e))
        if bid:
            try:
                link = "http://api.bilibili.com/x/web-interface/view?bvid=" + bid
                data = requests.get(link).json()
                # picurl = '[CQ:image,file=' + data['data']['pic'] + ']'
                picurl = MessageSegment.image(data['data']['pic'])
                title = data['data']['title']
                aid = 'av' + str(data['data']['aid'])
                owner = data['data']['owner']['name']
                view = data['data']['stat']['view']
                damaku = data['data']['stat']['danmaku']
                reply = data['data']['stat']['reply']
                await bot.send(event, message = picurl + "\n"+ title  + "\n" + "av号：" + aid +  "\n" + "作者：" + owner + "\n" + "播放量：" + str(view) + "  " + "弹幕：" + str(damaku) + "  " + "评论：" + str(reply))
            except Exception as e:
                await bot.send(event, 'b2p_in \n'+str(e))
    except Exception as e:
                        await bot.send(event, 'b2p_out \n'+str(e))
    return 0