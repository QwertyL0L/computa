import asyncio
from discord.ext import commands
import discord
import os
import webbrowser as wb
from discord import FFmpegPCMAudio
import pyautogui
from gtts import gTTS
import sys
import time

activity = discord.Activity(type=discord.ActivityType.watching, name="Wextra's PC||Computa Help")

bot = commands.Bot(command_prefix="Computa ",activity = activity,case_insensitive=True,intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged In As {bot.user.name}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def rickroll(ctx):
    wb.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    await ctx.reply("***Opened a rickroll***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def msgbox(ctx, * ,text: str):
    await ctx.reply("***Opened a messagebox***")
    pyautogui.alert(text=str(text), title=f'MessageBox from {ctx.author.display_name}', button='OK')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cmdprompt(ctx):
    await ctx.reply("***Opened Command Prompt***")
    os.startfile("cmd.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def calc(ctx):
    await ctx.reply("***Opened calculator***")
    os.startfile("calc.exe")

@bot.command() 
@commands.cooldown(1, 10, commands.BucketType.user)
async def youtube(ctx):
    wb.open_new("https://www.youtube.com")
    await ctx.reply("***Opened Youtube.com***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def roblox(ctx):
    wb.open_new("www.roblox.com")
    await ctx.reply("***Opened roblox.com***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def uselessfacts(ctx):
    wb.open_new("https://uselessfacts.jsph.pl/random.html")
    await ctx.reply("***Opened Useless Facts API***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def google(ctx, *, text: str):
    wb.open_new(f"https://www.google.com/search?q={text}")
    await ctx.reply("***Opened Google Search***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def translate(ctx, lang1: str, lang2: str, *, text: str):
    wb.open_new(f"https://translate.google.com/?sl={lang1}&tl={lang2}&text={text}&op=translate")
    await ctx.reply("***Opened Google Translate***")
  
@bot.command(pass_context = True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def speak(ctx, *, text: str):
    language = 'en'
    myobj = gTTS(text=f'{text}', lang=language, slow=False)
    myobj.save("tts.mp3")
    source = FFmpegPCMAudio('tts.mp3')
    channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    player = voice.play(source)
    await ctx.reply("playing audio...")
    while voice.is_playing(): #Checks if voice is playing
        await asyncio.sleep(1) #While it's playing it sleeps for 1 second
    else:
        await asyncio.sleep(1) #If it's not playing it waits 15 seconds
    while voice.is_playing(): #and checks once again if the bot is not playing
        break #if it's playing it breaks
    else:
        await voice.disconnect() #if not it disconnects

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def poosay(ctx):
    await ctx.reply(f"***{ctx.author.mention} poosay***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ytsearch(ctx,*,text: str):
    wb.open_new(f"https://www.youtube.com/results?search_query={text}")
    await ctx.reply("***Opened Youtube Search***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def error(ctx, * ,text: str):
    await ctx.reply("***Opened an Error Window***")
    pyautogui.alert(text=str(text), title=f'Error 404', button='OK')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def lunarclient(ctx):
    await ctx.reply("***Opened Lunar Client***")
    os.startfile("C:/Users/paris/Desktop/Lunar Client.lnk")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def autoclicker(ctx):
    await ctx.reply("***Opened AutoClicker***")
    os.startfile("C:/Users/paris/Downloads/AutoClicker.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def edgewindow(ctx):
    await ctx.reply("***Opened new Edge window***")
    pyautogui.hotkey("ctrl","n")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def history(ctx):
    await ctx.reply("***Opened Search History***")
    pyautogui.hotkey("ctrl","h")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def snake(ctx):
    wb.open_new(f"https://www.google.com/search?q=snake+google")
    await ctx.reply("***Opened Google Snake***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def notepad(ctx, * , text: str):
    await ctx.reply("***Opened NotePad***")
    pyautogui.press('win')
    pyautogui.typewrite('notepad')
    time.sleep(.3)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(f'{text}')

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def tab(ctx):
    await ctx.reply("***Opened New Tab***")
    pyautogui.hotkey("ctrl","t")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def devtools(ctx):
    await ctx.reply("***Opened Dev Tools***")
    pyautogui.hotkey("ctrl","shift","i")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def minecraft(ctx):
    await ctx.reply("***Opened Minecraft Launcher***")
    os.startfile("C:/Users/paris/Downloads/Minecraft Installer.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def screenshot(ctx):
    im1 = pyautogui.screenshot()
    im2 = pyautogui.screenshot('my_screenshot.png')
    file = discord.File("my_screenshot.png")
    await ctx.send(file=file, content=f"{ctx.author.mention}'s Screenshot of Wextra's PC")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def robloxsearch(ctx,ID: str):
    wb.open_new(f"https://web.roblox.com/users/{ID}/profile")
    await ctx.reply("***Opened Roblox Search***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def maps(ctx, * ,address: str):
    wb.open_new(f"https://www.google.com/maps/dir///{address}")
    await ctx.reply("***Opened Google Maps***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def url(ctx, text: str):
    wb.open_new(str(text))
    await ctx.reply("***Opened a URL***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def vup(ctx):
    await ctx.reply("***Turned Up Volume***")
    pyautogui.hotkey("volumeup")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def vdown(ctx):
    await ctx.reply("***Turned Down Volume***")
    pyautogui.hotkey("volumedown")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def downloads(ctx):
    await ctx.reply("***Opened Downloads***")
    pyautogui.hotkey("ctrl","j")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bup(ctx):
    await ctx.reply("***Turned Up Brightness***")
    pyautogui.hotkey("f3")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bdown(ctx):
    await ctx.reply("***Turned Down Brightness***")
    pyautogui.hotkey("f2")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def taskmanager(ctx):
    await ctx.reply("***Opened Task Manager***")
    os.startfile("taskmgr.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def robloxlauncher(ctx):
    await ctx.reply("***Opened Roblox Launcher***")
    os.startfile("RobloxPlayerLauncher.exe")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def bcalc(ctx, * , firstnumber: str, secondnumber: str):
    await ctx.reply("***Opened Broswer Calculator***")
    wb.open_new(f"https://www.google.com/search?q={firstnumber}+{secondnumber}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def close(ctx):
    await ctx.reply("***Closed the current window***")
    pyautogui.hotkey('alt',"f4")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hotkey(ctx,*,s1: str, s2: str):
    await ctx.reply(f"***Successfully Clicked {s1} + {s2}***")
    pyautogui.hotkey(f"{s1}",f"{s2}")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def userecho(ctx, text: str):
    pyautogui.typewrite(f'{text}')
    pyautogui.hotkey("enter")
    await ctx.reply(f"***Made Wextra Send {text}***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def hotkeyhold(ctx, * ,s1: str, s2: str):
    with pyautogui.hold('win'):
        pyautogui.press([f'{s1}', f'{s2}'])
    await ctx.reply(f"***Successfully Clicked {s1} + {s2}***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ngrams(ctx, * , text: str):
    wb.open_new(f"https://books.google.com/ngrams/graph?content={text}")
    await ctx.reply("***Opened Google Ngrams***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def timer(ctx):
    await ctx.reply("***Opened Timer***")
    os.startfile("timer.exe")

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def restart(ctx):
    id = str(ctx.author.id)
    if id == '898358037239201812': # YOUR DISCORD ID HERE
        await ctx.reply('Restarting...')
        restart_bot()
    else:
        await ctx.send("You dont have sufficient permmisions to perform this action!")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def ytvideo(ctx, id: str):
    wb.open_new(f"https://www.youtube.com/watch?v={id}")
    await ctx.reply("***Opened A Youtube Video***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def r34(ctx, *, tag: str):
    wb.open_new(f"https://rule34.xxx/index.php?page=post&s=list&tags={tag}")
    await ctx.reply(f"***Searched {tag} on rule34.xxx***")

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def pornhub(ctx, *, query: str):
    wb.open_new(f"https://www.pornhub.com/video/search?search={query}")
    await ctx.reply(f"***Searched {query} On pornhub.com***")

@bot.command()
async def help1(ctx):
    embed = discord.Embed(color=0x0BA8B4, title="App Commands", url="https://cdn.discordapp.com/attachments/1004119942750273688/1007765870166167552/help.txt")
    embed.add_field(name="autoclicker", value="opens autoclicker", inline=False)
    embed.add_field(name="cmdprompt", value="opens command prompt", inline=False)
    embed.add_field(name="devtools", value="opens devtools", inline=False)
    embed.add_field(name="error", value="opens a error window", inline=False)
    embed.add_field(name="minecraft", value="opens minecraft", inline=False)
    embed.add_field(name="roblox launcher", value="opens roblox launcher", inline=False)
    embed.add_field(name="lunarclient", value="opens lunarclient", inline=False)
    embed.add_field(name="calc", value="opens calculator", inline=False)
    embed.add_field(name="timer", value="opens timer", inline=False)
    embed.set_footer(text="Page 1/4")
    embed.set_footer(text="Type Computa help2 for second page")
    embed.set_footer(text=".txt format: https://cdn.discordapp.com/attachments/1004119942750273688/1007765870166167552/help.txt")
    await ctx.send(embed=embed)

@bot.command()
async def help2(ctx):
    embed = discord.Embed(color=0x0BA8B4, title="PC Commands", url="https://cdn.discordapp.com/attachments/1004119942750273688/1007765870166167552/help.txt")
    embed.add_field(name="vup", value="turn up pc volume", inline=False)
    embed.add_field(name="vdown", value="turn down pc volume", inline=False)
    embed.add_field(name="bup", value="turn up brightness", inline=False)
    embed.add_field(name="bdown", value="turn down brightness", inline=False)
    embed.add_field(name="msgbox", value="opens msgbox", inline=False)
    embed.add_field(name="screenshot", value="take a screenshot of pc", inline=False)
    embed.add_field(name="hotkeyhold", value="presses hotkey while holding windowskey", inline=False)
    embed.set_footer(text="Page 2/4")
    embed.set_footer(text="Type Computa help3 for third page")
    embed.set_footer(text=".txt format: https://cdn.discordapp.com/attachments/1004119942750273688/1007765870166167552/help.txt")
    await ctx.send(embed=embed)

@bot.command()
async def help3(ctx):
    embed = discord.Embed(color=0x0BA8B4, title="Broswer Commands", url="https://cdn.discordapp.com/attachments/1004119942750273688/1007765870166167552/help.txt")
    embed.add_field(name="maps", value="opens google maps", inline=False)
    embed.add_field(name="edgewindow", value="opens new broswer window", inline=False)
    embed.add_field(name="roblox", value="opens roblox.com", inline=False)
    embed.add_field(name="robloxsearch", value="search any roblox user with their ID", inline=False)
    embed.add_field(name="snake", value="opens google snake", inline=False)
    embed.add_field(name="tab", value="opens new tab", inline=False)
    embed.add_field(name="translate", value="opens google translate", inline=False)
    embed.add_field(name="url", value="opens any url", inline=False)
    embed.add_field(name="ytsearch", value="search youtube for videos", inline=False)
    embed.add_field(name="uselessfacts", value="opens useless facts api website", inline=False)
    embed.add_field(name="devtools", value="opens devtools", inline=False)
    embed.add_field(name="bcalc", value="opens calculator in broswer", inline=False)
    embed.add_field(name="ngrams", value="opens google ngrams", inline=False)
    embed.add_field(name="downloads", value="checks browser downloads", inline=False)
    embed.set_footer(text="Page 3/4")
    embed.set_footer(text="Type Computa help4 for fourth page")
    await ctx.send(embed=embed)

@bot.command()
async def help4(ctx):
    embed = discord.Embed(color=0x0BA8B4, title="Trolling Commands", url="https://cdn.discordapp.com/attachments/1004119942750273688/1007765870166167552/help.txt")
    embed.add_field(name="poosay", value="calls you a poosay", inline=False)
    embed.add_field(name="rickroll", value="opens a rickroll", inline=False)
    embed.add_field(name="history", value="opens broswer history", inline=False)
    embed.add_field(name="close", value="closes active window", inline=False)
    embed.add_field(name="hotkey", value="presses hotkey", inline=False)
    embed.add_field(name="userecho", value="make wextra type anything", inline=False)
    embed.set_footer(text="Page 4/4")
    embed.set_footer(text="END OF PAGE")
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
     if isinstance(error, commands.CommandNotFound): 
         await ctx.reply("Invalid Command. Type **Computa help** to see all commands")
         if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Slow down! Try again in **{round(error.retry_after)}s.**")

bot.run("TOKEN HERE")
