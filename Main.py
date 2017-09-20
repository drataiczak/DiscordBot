import discord
import dnd
import asyncio

################################################################################
# Commands the bot accepts:
#   !help
#   !members
#   !gen-character <Player Name> <Campaign Name>
#   !character-sheet <Player Name> <Campaign Name>
#   !status <Player> - DM Only
#   !roll <Die Type> <Die Count>
#   !secret-roll <Die Type> <Die Count>
#   !map <City [optional]>
#   !npc <Name> - Gives info on certain NPC
#   !attack <Type> <Weapon>
#   !time - Prints total time played and last session time

# Tyler's Wants:
#   - Shop manager - Lists items/costs
#   - Inventory manager for character-sheet (Add/Drop)
#   - Combat management - HP deduction/saving rolls/etc
#   - Action point management - trip & knife, feint & knife, etc
#   - Days passed - Auto manages food
################################################################################
token = 'MzU2Njg3NzY4ODc0OTA5Njk2.DJfK7A.wP-d8W77T48EcoVfui3X6r2i_x0'
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as', client.user.name)
    print('client.user:', client.user)
    print(client.user.name, 'is part of the server(s):')
    for server in client.servers:
        print(f'\t{server}')
        for channel in client.get_all_channels():
            print('\t\tChannel:', channel)
    print('--------------------')

@client.event
async def on_message(msg):
    if msg.content.lower().startswith('!help'):
        await client.send_message(msg.channel, 'Help me!')
    if msg.content.lower().startswith('!members'):
        for member in client.get_all_members():
            await client.send_message(msg.channel, member)

client.run(token)
