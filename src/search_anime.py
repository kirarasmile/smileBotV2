import requests, re
import urllib.parse
import config
from saucenao_api import SauceNao
async def searchanime(bot, event):  # 搜索番剧截图
    anicount = 0
    pattern = re.compile(r'url=(.*?)]', re.I)
    img = re.findall(pattern,event.message)
    animeimg = img[0]

# anime
    data_anime = requests.get("https://api.trace.moe/search?url={}".format(urllib.parse.quote_plus(animeimg))).json()
    try:
        if data_anime['result'][0]['similarity'] > 0.90:
            # anicount += 1
            best_anime = data_anime['result'][0]
            pic_anime = '[CQ:image,file=' + img + ']'
            time_anime = str(best_anime['from']/60)
            title_anime = best_anime['filename']
            similarity_anime = str(best_anime['similarity'])
            await bot.send(event, message = pic_anime + "\n"+ \
                                            "番剧：" + title_anime +  "\n" + \
                                            "时间戳：" + time_anime + "\n" + \
                                            "准确率：" + similarity_anime + "\n" + \
                                            "link：https://api.trace.moe/search?url=" +str(animeimg))
        else:
            await bot.send(event,"anime搜不到，爬")
    except:
        await bot.send(event,"anime搜不到，爬")

# saucenao
    sauce = SauceNao(api_key = config.saucenao_token,db=999)
    data_saucenao = sauce.from_url(animeimg)
    try:
        if data_saucenao[0].similarity > 0.90:
            best_saucenao = data_saucenao[0]
            pic_saucenao = '[CQ:image,file=' + url + ']'
            title_saucenao = best_saucenao.title
            author_saucenao = best_saucenao.author
            similarity_saucenao = best_saucenao.similarity
            picurl_saucenao = best_saucenao.urls
            await bot.send(event, message = pic_saucenao + "\n"+ \
                                                    "图片名：" + title_saucenao +  "\n" + \
                                                    "作者：" + author_saucenao + "\n" + \
                                                    "准确率：" + similarity_saucenao + "\n" + \
                                                    "link：" +picurl_saucenao)
        else:
            await bot.send(event,"saucenao搜不到，爬")
    except:
        await bot.send(event,"saucenao搜不到，爬")