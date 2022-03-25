import requests, re
import urllib.parse
async def searchanime(bot, event):  # 搜索番剧截图
    anicount = 0
    pattern = re.compile(r'url=(.*?)]', re.I)
    img = re.findall(pattern,event.message)
    animeimg = img[0]
    data = requests.get("https://api.trace.moe/search?url={}".format(urllib.parse.quote_plus(animeimg))).json()
    print(data)
    datalen = len(data['result'])
    for i in range(0, datalen):
        if data['result'][i]['similarity'] > 0.90:
            anicount += 1
            time = str(data['result'][i]['from']/60)
            title = data['result'][i]['filename']
            similarity = str(data['result'][i]['similarity'])
            await bot.send(event, "番剧：" + title +  "\n" + "时间戳：" + time + "\n" + "准确率：" + similarity)
        else:
            pass
    if anicount == 0:
        await bot.send(event,"搜不到，爬")