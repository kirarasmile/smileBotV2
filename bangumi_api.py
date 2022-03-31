import json
import requests
import datetime

def request_get(url):
    return requests.get(url)


def bangumi_tv(url):
    res = request_get('url')
    weekday = datetime.datetime.today().weekday()
    date_time = json.loads(res.text)[weekday]['weekday']
    item_name = json.loads(res.text)[weekday]['items']

    print('# 新番放送表 ' + date_time['cn'] + ' >>>>>>>>>')
    for i in range(len(item_name)):
        print(item_name[i]['name'] + '|' + item_name[i]['name_cn'])
    
    
if __name__ == '__main__':
    bangumi_tv('https://api.bgm.tv/calendar')
