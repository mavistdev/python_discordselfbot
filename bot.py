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
from googletrans import Translator
# from SimpleQIWI import *

# token = "ВАШ ТОКЕН"         # https://qiwi.com/api
# phone = "ВАШ ТЕЛЕФОН"

# api = QApi(token=token, phone=phone)

bannedGuildIDs = [612650423387553814, 815244443196194816, 919184095723020338, 613425648685547541]

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
            # print(member)
            members += 1
    # print(len(allmembers))
    # print(allmembers)
    # print(len(allmembers2))
    # print(len(allmembers3))
    # print(len(allmembers4))
    # for user in range(0, int(members)):
    #     normlen = len(allmembers[user])
    #     if member in allmembers or allmembers2 or allmembers3 or allmembers4:
    #         pass
    #     else:
    #         const = f'{member.name}#{member.discriminator}'
    #         if normlen >= 1900:
    #             if normlen >= 1900:
    #                 if normlen >= 1900:
    #                     if normlen >= 1900:
    #                         print('пиздец')
    #                     else:
    #                         allmembers4.append(const)
    #                 else:
    #                     allmembers3.append(const)
    #             else:
    #                 allmembers2.append(const)
    #         else:
    #             allmembers.append(const)

    send = bot.get_channel(1098268021732159548)    
    await send.send(f'''**Mavist | Self Bot** ***в сети***.
Пользователей на серверах сейчас - **{members}**
Made by ||**mav.**|| with *python* and love''')

    send = bot.get_channel(1098268898442367006)    
    await send.send(f'{members}')
    while True:
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=" to my thoughts."))


@bot.event
async def on_message_delete(message):
    if await getidid(message) not in bannedGuildIDs:
        # try:
        #     print(f'[DELETE] [{d}-{m}--{t}] {message.author}, Айди {message.author.id} удалил/удалили на {message.guild.name}, {message.guild.id} // {message.content}')
        # except:
        #     print(f'[DM DELETE] [{d}-{m}--{t}] {message.author}, Айди {message.author.id} удалил на {message.channel.recipient.name}, {message.channel.recipient.id} // {message.content}')
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

# @bot.event
# async def on_message(message):
#     if await getidid(message) not in bannedGuildIDs:
#         d = date.strftime("%d")
#         m = date.strftime("%m")
#         t = date.strftime("%X")
#         # try:
#         #     print(f'[DELETE] [{d}-{m}--{t}] {message.author}, Айди {message.author.id} удалил/удалили на {message.guild.name}, {message.guild.id} // {message.content}')
#         # except:
#         #     print(f'[DM DELETE] [{d}-{m}--{t}] {message.author}, Айди {message.author.id} удалил на {message.channel.recipient.name}, {message.channel.recipient.id} // {message.content}')
#         mt = await gettype(message)
#         if mt == 'server':
#             print(f'[MSG] [{d}-{m}--{t}] {message.author} отправил на {message.guild.name}, {message.guild.id} // {message.content}')
#         if mt == 'dm':
#             print(f'[DM MSG] [{d}-{m}--{t}] {message.author} отправил в {message.channel.recipient.name} // {message.content}')
#         if mt == 'group':
#             print(f'[SG MSG] [{d}-{m}--{t}] {message.author} отправил на {message.channel.name} // {message.content}')

#     else:
#         pass

# @client.event
# async def on_guild_channel_delete(channel):
#   c = client.get_channel(1016375426911842335)
#   await c.send(f'''удален канал {channel.name}, {channel.id}''', tts=False)

# @client.event
# async def on_guild_channel_create(channel):
#   c = client.get_channel(1016375368216744036)
#   await c.send(f'''создан канал {channel.name}, {channel.id}''', tts=False)

# @client.event
# async def on_guild_channel_update(before, after):
#   c = client.get_channel(1016376284642803813)
#   await c.send(f'''обновлен канал 
#     До - {before} 
#     После - {after}''', tts=False)

# @client.event
# async def on_guild_channel_pins_update(channel, last_pin):
#   link = await channel.create_invite(max_age = 0, max_uses = 0)
#   c = client.get_channel(1027186793411514458)
#   await c.send(f'''Печатает в
#     {link}''', tts=False)
#   c = client.get_channel(1016377546851504229)
#   await c.send(f'''обновлен канал 
#     Канал - {channel} 
#     Последний пин - {last_pin}''', tts=False)

# @client.event
# async def on_private_channel_update(before, after):
#   c = client.get_channel(1016377611066294332)
#   await c.send(f'''обновлен приватный канал 
#     До - {before} 
#     После - {after}''', tts=False)

# @client.event
# async def on_private_channel_pins_update(before, after):
#   c = client.get_channel(1016377697674481696)
#   await c.send(f'''обновлен Приватный канал 
#     Канал - {channel} 
#     Последний пин - {last_pin}''', tts=False)

# @bot.event
# async def on_typing(channel, user, when):
#     try:
#         link = await channel.create_invite(max_age = 0, max_uses = 0)
#         print(f'Печатает Канал - {channel} Юзер - {user} Время - {when} ---- {link}')
#     except:
#         print(f'Печатает Канал - {channel} Юзер - {user} Время - {when}')

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
    await ctx.message.delete()
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
    await ctx.message.delete()
    await member.kick(reason=reason)
    await ctx.send(f'Успешно кикнут {member} по причине {reason}')

@bot.command()
async def mrename(ctx,*, arg):
    await ctx.message.delete()
    await ctx.guild.edit(name=arg)

# @bot.command()
# async def balance(ctx):
#     await ctx.send(api.balance)
    
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
        await ctx.send(f'Сгенерированный пароль из {arg} символов - {password}')

# @bot.command()
# async def translate(ctx, lang, *, text):
    # if lang.lower() == 'ru':
    #     tr = translator.translate(text, src='en', dest='ru')
    #     ctx.send(tr.text)
    # elif lang.lower() == 'en':
    #     tr = translator.translate(text, src='ru', dest='en')
    #     ctx.send(tr.text)
    # translator = Translator()
    # result = translator.translate(text, src='fi', dest='fr')

    # print(result.src)
    # print(result.dest)
    # print(result.text)

bot.run(token)
