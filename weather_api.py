import requests
import json 
import sys, getopt

def arg_run(argv):
    
    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, 'p:', ['position='])  # 短与长选项模式
        for opt, arg in opts:
            if opt in ['-p', '--position']:
                weather_api(arg)
    except:
        print("arg error")

def weather_api(city):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&APPID=XXXXXXXXXXXXXXXXXXXXX')
    response = json.loads(res.text)
    # print(response)
    print('天气概况------->')
    print('温度')
    print(int(response['main']['temp'] - 273.15))
    print('--------------')
    print('最睾温度')
    print(int(response['main']['temp_max'] - 273.15))
    print('--------------')
    print('最deep温度')
    print(int(response['main']['temp_min'] - 273.15))
    print('--------------')
    print('体感温度')
    print(int(response['main']['feels_like'] - 273.15))
    print('--------------')
    print('shit度')
    print(int(response['main']['humidity']))
    print('--------------')
    print('天气状况')
    print(response['weather'][0]['main'])
    print('--------------')
    print('气压状况')
    print(str(response['main']['pressure']) + 'hpa')
    print('--------------')
if __name__ == '__main__':
    arg_run(sys.argv[1:])

# K = C + 273.15