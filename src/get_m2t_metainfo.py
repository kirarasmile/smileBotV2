import os
async def getmetainfo(bot, event):
    magnet = event.message
    nodejs = os.popen('node m2t.js ' + magnet)
    name = nodejs.read()
    nodejs.close()
    await bot.api.send_private_msg(user_id=event.user_id, message=name)
