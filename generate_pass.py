import random
def gen_pass(pass_length):
    sandi = ""
    for i in range(pass_length):
        elements = "=-`[]\;',./abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

        sandi = sandi+random.choice(elements)
    return sandi

gen_pass(10)

# coinflip
def coinflip():
    num = random.randint(1,2)
    if num == 1:
        return "1"
    if num == 2:
        return "2"

# rolling dice
# def dice(ctx):
#     nums = random.randint(1,6)
#     if nums == 1:
#         await ctx.send('It is 1!')
#     elif nums == 2:
#         await ctx.send('It is 2!')
#     elif nums == 3:
#         await ctx.send('It is 3!')
#     elif nums == 4:
#         await ctx.send('It is 4!')
#     elif nums == 5:
#         await ctx.send('It is 5!')
#     elif nums == 6:
#         await ctx.send('It is 6!')
