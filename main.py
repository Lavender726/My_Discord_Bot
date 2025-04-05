# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
import random
import os
from discord.ext import commands
from bot_logic import gen_pass
import requests
from model import get_class, get_class2, get_class3
from detect_objects import detect
from logic_poke import Pokemon

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

@bot.command()
async def classification(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./CV/{file_name}"))
    if get_class2(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./CV/{file_name}") == 'non_car_crashes\n' or get_class3(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./CV/{file_name}") <= 0.9:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            #file_url = attachment.url IF URL
            await attachment.save(f"./CV/{file_name}")
            await ctx.send(detect(input_image=f"./CV/{file_name}", output_image=f"./CV/{file_name}", model_path="yolov3.pt"))
            # await ctx.send(tampilkan(output_image=f"./CV/{file_name}"))
            with open(f'CV/{file_name}', 'rb') as f:
            # with open(f'meme/enemies-meme.jpg', 'rb') as f:
            # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
                picture = discord.File(f)
            await ctx.send(file=picture)        
    if not ctx.message.attachments:
        await ctx.send("You forgot to upload the images :(")

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

# exponent two numbers
@bot.command()
async def exp(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left ** right)
    
# dividing two numbers
@bot.command()
async def divide(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)

# Lets get started
@bot.command()
async def lets_get_started(ctx):
    await ctx.send("""
    You are seeing this message because you needed help getting started. \n
    This will updated every new command is added! \n
    Math help: \n
    $add with a space between 2 numbers to get a sum.
    $subtract with a space between 2 numbers to get a difference.
    $multiply with a space between 2 numbers to get a product.
    $divide with a space between 2 numbers to get a quotient. \n
    Repetition: \n
    $repeat and I will repeat messages (simple enough right?)
    Password generation:
    $password and I will generate you 10 passwords full of characters! \n
    Other: \n
    $coinflip and you get a head or a tail! (Remember, it's completely random!) 
    $flower and you get a description of a random flower! (This one is not really random, you have a higher change to get 
    more known flowers than less known flowers. But who knows, you might learn soemething new!)
    $dice. It's a dice and random. 
    $mem to show our custome meme.\n
    API: \n
    $duck shows a random duck picture from the web.
    $dog shows a random dog picture from the web.
    $go is pokemon go.\n
    Games: \n
    $tictactoe @player
    $place row column \n
    File management: \n
    $local_drive to show all the files under local.
    $showfile to show a certain file.
    $save file <10MB (for now) \n
    Classify: \n
    $classification upload the file to ask the AI if it's classified as traffic, no traffic, or car crash.\n
    Text: \n
    $write to overwrite.
    $append to add something new.
    $read to see.""")

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

#show local drive    
@bot.command()
async def local_drive(ctx):
    try:
      folder_path = "./files"  # Replace with the actual folder path
      files = os.listdir(folder_path)
      file_list = "\n".join(files)
      await ctx.send(f"Files in the files folder:\n{file_list}")
    except FileNotFoundError:
      await ctx.send("Folder not found.")

#show local file
@bot.command()
async def showfile(ctx, filename):
  """Sends a file as an attachment."""
  folder_path = "./files/"
  file_path = os.path.join(folder_path, filename)
  try:
    await ctx.send(file=discord.File(file_path))
  except FileNotFoundError:
    await ctx.send(f"File '{filename}' not found.")  

# upload file to local computer
@bot.command()
async def save(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            # file_url = attachment.url  IF URL
            await attachment.save(f"./files/{file_name}")
            await ctx.send(f"Saved {file_name}")
    else:
        await ctx.send("You forgot to upload the file(s) :(")        

# The '$go' command
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Getting the name of the message's author
    # Check whether the user already has a Pokémon. If not, then...
    # if author not in Pokemon.pokemons.keys():
    pokemon = Pokemon(author)  # Creating a new Pokémon
    await ctx.send(await pokemon.info())  # Sending information about the Pokémon
    image_url = await pokemon.show_img()  # Getting the URL of the Pokémon image
    if image_url:
        embed = discord.Embed()  # Creating an embed message
        embed.set_image(url=image_url)  # Setting up the Pokémon's image
        await ctx.send(embed=embed)  # Sending an embedded message with an image
    else:
        await ctx.send("Failed to upload an image of the pokémon.")

 #tictactoe game
# Game state variables
current_player = None
board = [[' ' for _ in range(3)] for _ in range(3)]  # 3x3 Tic-Tac-Toe board
player1 = None  # Store player1 to keep track of turns
player2 = None  # Store player2 to keep track of turns
@bot.command()
async def tictactoe(ctx, opponent: discord.Member):
    """Starts a Tic-Tac-Toe game with another player as second player."""
    global current_player, board, player1, player2
    if current_player is not None:
        await ctx.send("A game is already in progress.")
        return
    player1 = ctx.author
    player2 = opponent
    current_player = player1  # Start with player1
    board = [[' ' for _ in range(3)] for _ in range(3)]
    await ctx.send(
        f"{ctx.author.mention} (1st player) has challenged {opponent.mention} (2nd player)to a game of Tic-Tac-Toe!"
    )
    await display_board(ctx)

@bot.command()
async def place(ctx, x: int, y: int):
    """Places your mark (X or O) on the board. Example: !place 1 2"""
    global current_player, board, player1, player2
    if current_player is None:
        await ctx.send("Start a game first using !tictactoe @opponent")
        return
    if not (1 <= x <= 3 and 1 <= y <= 3):
        await ctx.send(
            "Invalid coordinates. Coordinates should be between 1 and 3.")
        return
    x -= 1
    y -= 1
    if board[x][y] != ' ':
        await ctx.send("That spot is already taken!")
        return
    
    # Determine the mark based on the current player
    mark = 'X' if current_player == player1 else 'O'
    board[x][y] = mark
    await display_board(ctx)
    if check_win(mark):
        await ctx.send(f"{current_player.mention} wins!")
        current_player = None
        player1 = None
        player2 = None
    elif check_draw():
        await ctx.send("It's a draw!")
        current_player = None
        player1 = None
        player2 = None
    else:
        # Switch to the other player
        current_player = player2 if current_player == player1 else player1
        await ctx.send(f"It's {current_player.mention}'s turn.")

async def display_board(ctx):
    """Displays the current state of the Tic-Tac-Toe board."""
    board_str = "```\n"
    for row in board:
        board_str += " | ".join(row) + "\n"
        board_str += "---------\n"
    board_str += "```"
    await ctx.send(board_str)

def check_win(mark):
    """Checks if the given mark has won the game."""
    # Check rows
    for row in board:
        if all(cell == mark for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    # Check diagonals
    if (board[0][0] == mark and board[1][1] == mark and board[2][
            2] == mark) or (board[0][2] == mark and board[1][1] == mark
                           and board[2][0] == mark):
        return True
    return False
def check_draw():
    """Checks if the game is a draw."""
    return all(cell != ' ' for row in board for cell in row)

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore
    # provide what you can help here

bot.run('INSERT_TOKEN')
