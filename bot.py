import discord,funwaabot,requests,discord.ext.commands
c=discord.ext.commands.Bot(command_prefix='.')
@c.command(pass_context=True)
async def cringe(context):await context.message.channel.send("http://funwaa.com/Admin/images_category/"+requests.get("http://funwaa.com/Engmore_selected.aspx?imgnm=0").text.split("Admin/images_category/")[1].split('"')[0])
@c.event
async def on_command_error(a,b):pass
c.run(funwaabot.token)
