const Discord = require('discord.js');

const client = new Discord.Client();

 

client.on('ready', () => {

    console.log('I am ready!');

});

 

client.on('message', message => {

    if (message.content === 'ping') {

       message.reply('pong');

       }

});

 

// THIS  MUST  BE  THIS  WAY

BOT_TOKEN = "NTM4MzE2NTIzNTcyNDI4ODAz.XPKR5w.P3AB2-rn6DnFqIoDkzFrAwUqOQg"


client.login(process.env.BOT_TOKEN);//BOT_TOKEN is the Client Secret
