import re, requests
async def changebilibili(bot, event):
    if 'com.tencent.miniapp_01' in event.message:
        await bot.send(event, "还不会处理小程序，告辞")
    else:
        if 'bilibili.com' in event.message:
            pattern_b = re.compile(r'www.bilibili.com/video/(.*)/\?spm_id|www.bilibili.com/video/(.*)', re.I)
            b_info = re.findall(pattern_b,event.message)
        else:
            pattern_b = re.compile(r'b23.tv/(.*)/\?spm_id|b23.tv/(.*)', re.I)
            b_info = re.findall(pattern_b,event.message)
        if b_info:
            for i in range(0,2):
                if b_info[0][i]:
                    try:
                        link = "http://api.bilibili.com/x/web-interface/view?bvid=" + b_info[0][i]
                        data = requests.get(link).json()
                        picurl = '[CQ:image,file=' + data['data']['pic'] + ']'
                        title = data['data']['title']
                        aid = 'av' + str(data['data']['aid'])
                        owner = data['data']['owner']['name']
                        view = data['data']['stat']['view']
                        damaku = data['data']['stat']['danmaku']
                        reply = data['data']['stat']['reply']
                        await bot.send(event, message = picurl + "\n"+ title  + "\n" + "av号:" + aid +  "\n" + "作者：" + owner + "\n" + "播放量：" + str(view) + "  " + "弹幕：" + str(damaku) + "  " + "评论：" + str(reply))
                    except:
                        print("寄")