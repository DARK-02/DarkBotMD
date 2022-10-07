/**
   * Create By Dika Ardnt.
   * Contact Me on wa.me/6288292024190
   * Follow https://github.com/DikaArdnt
*/

const fs = require('fs')
const chalk = require('chalk')

// Website Api
global.APIs = {
	zenz: 'https://zenzapis.xyz',
}

// Apikey Website Api
global.APIKeys = {
	'https://zenzapis.xyz': '177c10ab45',
}

// Other
global.owner = ['6281327441039', '6282230819722']
global.bsu = ['6281327441039']
global.premium = ['6281327441039']
global.pembeli = ['6281327441039', '6283111532238']
global.packname = 'DarkBotMD'
global.author = 'Mr_Dark'
global.sessionName = 'session'
global.prefa = ['','!','.','🐦','🐤','🗿']
global.sp = '⭔'
global.mess = {
    success: '✓ Success',
    admin: 'Fitur Khusus Admin Group!',
    botAdmin: 'Bot Harus Menjadi Admin Terlebih Dahulu!',
    owner: 'Fitur Khusus Owner Bot',
    group: 'Fitur Digunakan Hanya Untuk Group!',
    private: 'Fitur Digunakan Hanya Untuk Private Chat!',
    bot: 'Fitur Khusus Pengguna Nomor Bot',
    wait: 'Loading...',
    pembeli: "*Fitur premium user only *⚠️\nbeli premium dengan harga *15k* via pulsa, atau *11k* via ovo\ncontact: 081327441039 ✅",
    endLimit: 'Limit Harian Anda Telah Habis, Limit Akan Direset Setiap Jam 12, atau beli premium dengan harga *15k* via pulsa, atau *11k* via ovo',
}
global.limitawal = {
    premium: "Infinity",
    free: 1
}
global.thumb = fs.readFileSync('./lib/logo.jpg')

let file = require.resolve(__filename)
fs.watchFile(file, () => {
	fs.unwatchFile(file)
	console.log(chalk.redBright(`Update'${__filename}'`))
	delete require.cache[file]
	require(file)
})
