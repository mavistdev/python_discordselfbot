import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import re
import tracemalloc
import os
import requests
import random as r
import datetime
import aiofiles

bannedGuildIDs = [] # Вставь сюда айди серверов, которые не будет обрабатывать логер

tracemalloc.start()

translator = Translator()
token = ''
prefix = 'self.'
allmembers = []
allmembers2 = []
allmembers3 = []
allmembers4= []
bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.warnings = {}
date = datetime.datetime.now()

class Get():
    DoLogClassMoves = True

def gettime():
    date = datetime.datetime.now()
    d = date.strftime("%d")
    m = date.strftime("%m")
    t = date.strftime("%X")
    fin = (f'{d}-{m}--{t}')
    return fin

def writelog(text, allow = True, disallowtext = None):
    if allow:
        file = open("selflogs.txt", "a")
        file.write(f'\n {text}')
        file.close()
    else:
        file = open("selflogs.txt", "a")
        file.write(f'\n Обнаружено действие с запретом на лог. Причина - {disallowtext}')
        file.close()

async def getidid(mes):
    try:
        g_id = int(mes.guild.id)
        return g_id
    except Exception as e:
        # print(e)
        g_id = 0

    try:
        g_dm = int(mes.channel.recipient.id)
        return g_dm
    except Exception as e:
        # print(e)
        g_dm = 0

    try:
        gr = int(mes.channel.id)
        return gr
    except Exception as e:
        print(e)
        gr = 0

async def gettype(mes):
    try:
        g_id = int(mes.guild.id)
        return 'server'
    except Exception as e:
        pass

    try:
        gr = int(mes.channel.recipient.id)
        return 'dm'
    except Exception as e:
        pass

    try:
        g_dm = int(mes.channel.id)
        return 'group'
    except Exception as e:
        pass

@bot.event
async def on_ready():
    a = f'{date}, Logged in'
    writelog(a)
    print("Logged in!")
    members = 0
    for guild in bot.guilds:
        for member in guild.members:
            members += 1

#     send = bot.get_channel(1098268021732159548)    
#     await send.send(f'''**Mavist | Self Bot** ***в сети***.
# Пользователей на серверах сейчас - **{members}**
# Made by ||**mav.**|| with *python* and love''')

#     send = bot.get_channel(1098268898442367006)    
#     await send.send(f'{members}')


@bot.event
async def on_message_delete(message):
    if await getidid(message) not in bannedGuildIDs:
        mt = await gettype(message)
        if mt == 'server':
            print(f'[DELETE] [{gettime()}] {message.author} удалил/удалили на {message.guild.name}, {message.guild.id} // {message.content}')
            writelog(f'[DELETE] [{gettime()}]  // {message.author} удалил/удалили на {message.guild.name}, {message.guild.id} // {message.content}')
        if mt == 'dm':
            print(f'[DM DELETE] [{gettime()}] {message.author} удалил на {message.channel.recipient.name} // {message.content}')
            writelog(f'[DM DELETE]{gettime()}  // {message.author} удалил на {message.channel.recipient.name} // {message.content}')
        if mt == 'group':
            print(f'[SG DELETE] [{gettime()}] {message.author} удалил на {message.channel.name} // {message.content}')
            writelog(f'[SG DELETE] [{gettime()}]  // {message.author} удалил на {message.channel.name} // {message.content}')
    else:
        pass

@bot.event
async def on_message(message):
    if await getidid(message) not in bannedGuildIDs:
        d = date.strftime("%d")
        m = date.strftime("%m")
        t = date.strftime("%X")
        # try:
        #     print(f'[DELETE] [{d}-{m}--{t}] {message.author}, Айди {message.author.id} удалил/удалили на {message.guild.name}, {message.guild.id} // {message.content}')
        # except:
        #     print(f'[DM DELETE] [{d}-{m}--{t}] {message.author}, Айди {message.author.id} удалил на {message.channel.recipient.name}, {message.channel.recipient.id} // {message.content}')
        mt = await gettype(message)
        if mt == 'server':
            print(f'[MSG] [{d}-{m}--{t}] {message.author} отправил на {message.guild.name}, {message.guild.id} // {message.content}')
        if mt == 'dm':
            print(f'[DM MSG] [{d}-{m}--{t}] {message.author} отправил в {message.channel.recipient.name} // {message.content}')
        if mt == 'group':
            print(f'[SG MSG] [{d}-{m}--{t}] {message.author} отправил на {message.channel.name} // {message.content}')

    else:
        pass

@bot.event
async def on_invite_create(invite):
  print(f'Инвайт создан {invite}')
  writelog(f'[invite] [{gettime()}]  // Created an invite - {invite}')


@bot.event
async def on_member_join(member):
    print(f'''[{gettime()}] {member.name}, Айди {member.id} присоеденился к {member.guild.name}''')
    writelog(f'[member event / join] [{gettime()}]  // {member.name}, Айди {member.id} присоеденился к {member.guild.name}')
@bot.event
async def on_member_remove(member):
    print(f'[{gettime()}] {member.name}, Айди {member.id} вышел с {member.guild.name} Название сервера - {member.guild.name} Айди сервера - {member.guild.id}')
    writelog(f'[member event / leave] [{gettime()}]  // {member.name}, Айди {member.id} вышел с {member.guild.name} Название сервера - {member.guild.name} Айди сервера - {member.guild.id}')

@bot.event
async def on_guild_remove(guild):
    print(f'''[{gettime()}] Ботa кикнули или забанили в - {guild.name}, id - {guild.id}
Пользователей теперь - {len(bot.users)} || Серверов теперь - {len(bot.guilds)}''')

@bot.event
async def on_guild_join(guild):
    print(f'''[{gettime()}] Бот присоеденился в - {guild.name}, id - {guild.id}
Пользователей теперь - {len(bot.users)} || Серверов теперь - {len(bot.guilds)}''')

@bot.command()
async def randint(ctx, *, nd2):
    await ctx.send(f'Число от 0 до {nd2} - {r.randint(0, int(nd2))}')

@bot.command()
async def popit(ctx):
    await ctx.message.delete()
    await ctx.send('''||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:|| ||:green_square:||
||:orange_square:|| ||:orange_square:|| ||:orange_square:|| ||:orange_square:|| ||:orange_square:|| 
||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:|| ||:red_square:||
||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:|| ||:blue_square:|| 
||:purple_square:|| ||:purple_square:|| ||:purple_square:|| ||:purple_square:|| ||:purple_square:|| ''')

@bot.command()
async def ruspopit(ctx):
    await ctx.message.delete()
    await ctx.send('''||:white_heart:|| ||:white_heart:|| ||:white_heart:|| ||:white_heart:|| ||:white_heart:||
||:blue_heart:|| ||:blue_heart:|| ||:blue_heart:|| ||:blue_heart:|| ||:blue_heart:|| 
||:heart:|| ||:heart:|| ||:heart:|| ||:heart:|| ||:heart:||''')

@bot.command()
async def members(ctx):
    await ctx.message.delete()
    await ctx.send(allmembers)

@bot.command()
async def spam(ctx, inti, *, text):
    await ctx.message.delete()
    x = int(0)
    while x != int(inti):
        await ctx.send(f'{text}')
        x += 1

@bot.command()
async def mclear(ctx, amount = 1):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(amount))

@bot.command()
async def mkick(ctx, member: discord.Member, *, reason = None ):
    await member.kick(reason=reason)
    await ctx.send(f'Успешно кикнут {member} по причине {reason}')

@bot.command()
async def mrename(ctx,*, arg):
    await ctx.message.delete()
    await ctx.guild.edit(name=arg)
    
@bot.command()
async def remind(ctx, num, *, text):
    num = int(num)
    remind_channel = ctx.bot.get_channel(num)    
    await remind_channel.send(text)

@bot.command()
async def password(ctx, arg):
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for n in range(1):
        password =''
        for i in range(int(arg)):
            password += r.choice(chars)
        message = await ctx.send(f'Сгенерированный пароль из {arg} символов - {password}')
        await ctx.add_reaction('✔️')

bot.run(token)
