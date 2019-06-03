const Discord = require('discord.js');

const app = new Discord.Client();

 

app.on('ready', () => {

    console.log('접속 중 입니다!');

});

 

app.on('message', message => {

    if (message.content === 'ping') {

       message.reply('pong');

       }

});

 

// THIS  MUST  BE  THIS  WAY

BOT_TOKEN = "NTM4MzE2NTIzNTcyNDI4ODAz.XPKR5w.P3AB2-rn6DnFqIoDkzFrAwUqOQg"


app.login(process.env.BOT_TOKEN);//BOT_TOKEN is the Client Secret
