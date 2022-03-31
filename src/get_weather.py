import requests
import json
import config

# K = C + 273.15
async def get_weather(bot, event):
    city = event.message[5:]
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=' + str(conif.weather_api))
    response = json.loads(res.text)
    await bot.send(event, message= '城市：' + city + '\n'\
                                + '当前温度：' + str(int(response['main']['temp'] - 273.15)) + '°C' + '\n'\
                                + '最高温度：' + str(int(response['main']['temp_max'] - 273.15)) + '°C' + '\n'\
                                + '最低温度：' + str(int(response['main']['temp_min'] - 273.15)) + '°C' + '\n'\
                                + '体感温度：' + str(int(response['main']['feels_like'] - 273.15)) + '°C' + '\n'\
                                + '湿度：' + str(int(response['main']['humidity'])) + '\n'\
                                + '天气状况：' + str(response['weather'][0]['main']) + '\n'\
                                + '气压状况：' + str(response['main']['pressure']) + 'hpa' + '\n')