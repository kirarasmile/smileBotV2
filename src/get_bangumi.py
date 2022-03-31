import json
import requests
import datetime

async def get_bangumi(bot, event):
    res = requests.get('https://api.bgm.tv/calendar')
    weekday = datetime.datetime.today().weekday()
    date_time = json.loads(res.text)[weekday]['weekday']
    item_name = json.loads(res.text)[weekday]['items']
    item_info = ['\n' + item_name[i]['name'] + '|' + str(item_name[i]['name_cn']) for i in range(len(item_name))]
    item_info_str = ' '.join(item_info)
    await bot.send(event, message = '# 新番放送表 ' +  date_time['cn'] \
                                    + ' >>>>>>>>>'+ '\n'+ item_info_str)
