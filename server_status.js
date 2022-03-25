// Gamedig，详情请见Gamedig项目https://github.com/gamedig/node-gamedig
const Gamedig = require('gamedig');
Gamedig.query({
    type: 'minecraft',
    host: 'mc.example'
}).then((state) => {
    console.log('|------------------------------')
    console.log('|-version:',state.raw.vanilla.raw.version.name);
    console.log('|------------------------------')
    // console.log('|-server link:',state.raw.vanilla.connect);
    // console.log('|------------------------------')
    console.log('|-max players =',state.maxplayers);
    console.log('|------------------------------')
    console.log('|-players list:')
    for(j=0; j<state.players.length; j++){
        console.log('|  -',state.players[j].name)
    }
    console.log('|------------------------------')
}).catch((error) => {
    console.log("Server is offline");
});