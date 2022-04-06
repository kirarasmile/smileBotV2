import os,re
async def serverstatus(bot, event):
    pattern_s = re.compile(r'服务器状态(.*)', re.I)
    server = re.findall(pattern_s,event.message)
    try:
        if server[0] == 'MC':
            nodejs = os.popen('node server_status.js')
            name = nodejs.read()
            nodejs.close()
            await bot.send(event,name)
        elif server[0] == '':
            nodejs = os.popen('node server_status.js')
            name = nodejs.read()
            nodejs.close()
            await bot.send(event,name)
        else:
            await bot.send(event,'暂不支持该服务器查询')
    except Exception as e:
        await bot.send(event, 'server_status error \n'+str(e))
    return 0