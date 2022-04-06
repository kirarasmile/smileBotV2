import requests
import json
import config

# K = C + 273.15
async def get_weather(bot, event):
    try:
        city = event.message[4:]
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + str(config.weather_api))
        if res.status_code == 200:
            response = json.loads(res.text)
            # print(response)
            await bot.send(event, message= '城市：' + city + '\n'\
                                        + '当前温度：' + str(int(response['main']['temp'] - 273.15)) + '°C' + '\n'\
                                        + '最高温度：' + str(int(response['main']['temp_max'] - 273.15)) + '°C' + '\n'\
                                        + '最低温度：' + str(int(response['main']['temp_min'] - 273.15)) + '°C' + '\n'\
                                        + '体感温度：' + str(int(response['main']['feels_like'] - 273.15)) + '°C' + '\n'\
                                        + '湿度：' + str(int(response['main']['humidity'])) + '\n'\
                                        + '天气状况：' + str(response['weather'][0]['main']) + '\n'\
                                        + '气压状况：' + str(response['main']['pressure']) + 'hpa' + '\n')
        else:
            await bot.send(event, message = '无法搜索到城市天气，输入的城市拼音为：' + city +'，请检查拼音和输入格式（需要空格）')
    except Exception as e:
        await bot.send(event, 'weathert error \n'+str(e))
    return 0