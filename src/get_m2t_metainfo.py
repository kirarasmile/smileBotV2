import os
async def getmetainfo(bot, event):
    try:
        magnet = event.message
        nodejs = os.popen('node m2t.js ' + magnet)
        name = nodejs.read()
        nodejs.close()
        await bot.send(event, message=name)
    except Exception as e:
        await bot.send(event, 'm2t error \n'+str(e))
