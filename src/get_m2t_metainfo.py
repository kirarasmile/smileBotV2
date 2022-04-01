import os
async def getmetainfo(bot, event):
    magnet = event.message
    nodejs = os.popen('node m2t.js ' + magnet)
    name = nodejs.read()
    nodejs.close()
    await bot.send(event, message=name)
