# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import random
import os
from discord.ext import commands
from bot_logic import gen_pass
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# subtracting two numbers
@bot.command()
async def subtract(ctx, left: int, right: int):
    """Subtracts two numbers together."""
    await ctx.send(left - right)

# multiplicating two numbers
@bot.command()
async def multiply(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)
    
# dividing two numbers
@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)

# Lets get started
@bot.command()
async def lets_get_started(ctx):
    await ctx.send("""
    You are seeing this message because you needed help getting started.
    This will updated every new command is added!
    Math help: 
    $add with a space between 2 numbers to get a sum.
    $subtract with a space between 2 numbers to get a difference.
    $multiply with a space between 2 numbers to get a product.
    $divide with a space between 2 numbers to get a quotient.
    Repetition:
    $repeat and I will repeat messages (simple enough right?)
    Password generation:
    $password and I will generate you 10 passwords full of characters!
    Other:
    $coinflip and you get a head or a tail! (Remember, it's completely random!) 
    $flower and you get a description of a random flower! (This one is not really random, you have a higher change to get 
    more known flowers than less known flowers. But who knows, you might learn soemething new!)
    $dice. It's a dice and random.""")

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
# password generator        
@bot.command()
async def password(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# MiniGameforFlower
@bot.command()
async def flower(ctx):
    rando = random.randint(1,20)
    if rando == 2:
        await ctx.send('''Poinsettia:
                       A flower native to Mexico that comes in many colors.''')
    elif rando == 3:
        await ctx.send('''Asiatic lily:
                       A flower with bright colors that can be up to 6 inches in diameter.''')
    elif rando == 5:
        await ctx.send('''Carnation:
                       A flower with serrated petals that comes in many colors.''')
    elif rando == 8:
        await ctx.send('''Azalea:
                       A popular flower that in China symbolizes womanhood.''')
    elif rando == 10:
        await ctx.send('''Iris:
                       A flower with a fan-like shape and six lobes that comes in many colors. 
                       Irises bloom in the spring or summer and don't have much scent.''')
    elif rando == 15:
        await ctx.send('''Bergenia:
                       A short plant with ornate flowers and leaves that change color from green to red or bronze in the cooler months. 
                       Bergenia is also known as Pigsqueak or Elephant's ears.''')
    elif rando == 16:
        await ctx.send('''Chrysanthemum:
                       A flower that blooms in late summer to fall and requires well-draining soil and full sun. 
                       Many species of chrysanthemums are native to China, where they were cultivated as early as the 15th century BC.''')
    else:
        two = random.randint(1,2)
        if two == 1:
            await ctx.send('''Daisy:
                           A popular flower that can be found on every continent except Antarctica. 
                           Daisies can come in many colors and can grow from 8 inches to 4 feet tall. 
                           They symbolize innocence, a connotation that comes from the Victorian era.''')
        elif two == 2:
            await ctx.send('''Rose:
                           A well-known flower with many varieties and fragrances. 
                           The color of the rose can have different meanings, such as white for purity, pink for love and joy, yellow for friendship, and red for intense love.''')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

@bot.command()
async def mem(ctx):
     # try by your self 2 min
    img_name = random.choice(os.listdir('Meme'))
    with open(f'Meme/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def write(ctx, *, my_string: str):
    with open('guidance.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
        
# append kalimat.txt
@bot.command()
async def append(ctx, *, my_string: str):
    with open('guidance.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)

# reading kalimat.txt
@bot.command()
async def read(ctx):
    with open('guidance.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here

bot.run('TOKEN_HERE')
