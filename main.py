from discord.ext import commands
import config 
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
from datetime import datetime , timedelta


os.chdir('C:/Users/abe/Desktop')

words=['damn','green']



intents = discord.Intents.default()
intent = discord.Intents(messages=True, message_content=True, guilds=True)
bot = commands.Bot(intents=intents,command_prefix='.')


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')

       
bot.add_cog(Greetings(bot))



@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
count=0
@bot.event
async def on_message(msg): 
    for word in words:
        if word in msg.content.lower():
            await msg.delete()
            global count
            count+=1
            print(count)
            if count==3:
            # await msg.channel.set_permissions(msg.author, read_messages=True,send_messages=False)
                await msg.author.send("Please don't swear")
                now=datetime.now().astimezone()
                later=now+timedelta(minutes=2)
                await msg.channel.send(f':white_check_mark: **User <@{msg.author}> time out until {later}')
            if count==5:   
                await msg.channel.send(f':white_check_mark: **User <@{msg.author}> was muted!**')
                now=datetime.now().astimezone()
                later=now+timedelta(minutes=59)
                await msg.author.timeout(later, reason=None)
                print(f'User {msg.author} was muted!')
                await msg.author.send("you will be kicked ")
            elif count == 10:
               await msg.author.send("last warning")
            elif count==11:
                await msg.guild.ban(msg.author, reason="spam")
                await msg.channel.send(f'{msg.author} banned' )
    await bot.process_commands(msg)
bot.run(TOKEN)
