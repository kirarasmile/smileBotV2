// 磁力链提取元数据中的标题，项目地址https://github.com/Tsuk1ko/magnet2torrent-js
const { writeFileSync } = require('fs');
const Magnet2torrent = require('magnet2torrent-js');
var args = process.argv.splice(2)

// 可以自定义trackers
const trackers = [
    'udp://tracker.opentrackr.org:1337/announce',
    'udp://open.tracker.cl:1337/announce',
    'udp://9.rarbg.com:2810/announce',
    'http://pow7.com:80/announce',
    'udp://tracker.openbittorrent.com:6969/announce',
    'http://tracker.openbittorrent.com:80/announce',
    'udp://opentracker.i2p.rocks:6969/announce',
    'https://opentracker.i2p.rocks:443/announce',
    'udp://www.torrent.eu.org:451/announce',
    'udp://tracker.torrent.eu.org:451/announce',
    'udp://open.stealth.si:80/announce',
    'udp://exodus.desync.com:6969/announce',
    'udp://ipv4.tracker.harry.lu:80/announce',
    'udp://opentor.org:2710/announce',
    'udp://tracker.tiny-vps.com:6969/announce',
    'udp://tracker.moeking.me:6969/announce',
    'udp://explodie.org:6969/announce',
    'udp://tracker.dler.org:6969/announce',
    'udp://vibe.sleepyinternetfun.xyz:1738/announce',
    'udp://tracker1.bt.moack.co.kr:80/announce'
]

const m2t = new Magnet2torrent({ 
    trackers,
    addTrackersToTorrent: true,
    timeout: 20 
});
 
m2t.getTorrent(args[0]).then(torrent => {
    // writeFileSync(`${torrent.name}.torrent`, torrent.toTorrentFile());
    console.log('The torrent name:',torrent.name);
}).catch(e => {
    // Timeout or error occured
    console.log('timeout or check your magnet pls');
    // console.error(e);
});