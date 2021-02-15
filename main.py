import discord 
import os
import requests
import json
from replit import db


from keep_alive import keep_alive
client = discord.Client()
#------------------database imp---------------------\
# db["p0"]=["<:kemo:767880276080590858>","https://cdn.discordapp.com/emojis/767880276080590858.png?v=1"]
# db["p1"]=["<:GAY:748520296784330773>","https://cdn.discordapp.com/emojis/748520296784330773.png?v=1"]

# db["p2"]=["<:PepeYikes:752247164456927326>","https://cdn.discordapp.com/emojis/752247164456927326.png?v=1"]

# db["p3"]=["<:frogg:699368022107881542>","https://cdn.discordapp.com/emojis/699368022107881542.png?v=1"]
# db["p4"]=["<:pepeok:748521269997207652>","https://cdn.discordapp.com/emojis/748521269997207652.png?v=1"]

# db["p5"]=["<:waitwhat:751211396322295879>","https://cdn.discordapp.com/emojis/751211396322295879.png?v=1"]

# db["p6"]=["<:3nnnn:698924619197054976>","https://cdn.discordapp.com/emojis/698924619197054976.png?v=1"]
# db["p7"]=["<:sadcat:728666854637436958>","https://cdn.discordapp.com/emojis/728666854637436958.png?v=1"]
# db["p8"]=["<:PepeHands:752247218768969908>","https://cdn.discordapp.com/emojis/752247218768969908.png?v=1"]
# db["p9"]=["<:cat11:745333300964491397>","https://cdn.discordapp.com/emojis/745333300964491397.png?v=1"]
# db["p10"]=["<:hmm:723260170028843048>","https://cdn.discordapp.com/emojis/723260170028843048.png?v=1"]
# db["p11"]=["<:taksim:691716815709274242>","https://cdn.discordapp.com/emojis/691716815709274242.png?v=1"]
# db["p12"]=["<:cat10:728666820214522016>","https://cdn.discordapp.com/emojis/728666820214522016.png?v=1"]
# db["p13"]=["<:monkaS:748521269108015144>","https://cdn.discordapp.com/emojis/748521269108015144.png?v=1"]
# db["p14"]=["jerry crying","https://tenor.com/view/tom-y-jerry-tom-and-jerry-meme-sad-cry-gif-18054267"]
# db["p15"]=["kareem's lover","https://cdn.discordapp.com/emojis/788620971484381244.gif?v=1"]
# db["p16"]=["someone dancing","https://cdn.discordapp.com/emojis/731412356902551562.gif?v=1"]
# db["p17"]=["sad cat with a gun","https://cdn.discordapp.com/emojis/606115088235233280.gif?v=1"]
# db["p18"]=["led 3nnnn","https://cdn.discordapp.com/emojis/667653120599523339.gif?v=1"]
# db["p19"]=["confused women","https://tenor.com/view/calculating-puzzled-math-confused-confused-look-gif-14677181"]
# db["p20"]=["pweeees","https://tenor.com/view/agnes-please-despicable-me-gif-11136000"]
# db["index"]=21
db={

  "p0":["<:kemo:767880276080590858>","https://cdn.discordapp.com/emojis/767880276080590858.png?v=1"],
  "p1":["<:GAY:748520296784330773>","https://cdn.discordapp.com/emojis/748520296784330773.png?v=1"],
  "p2":["<:PepeYikes:752247164456927326>","https://cdn.discordapp.com/emojis/752247164456927326.png?v=1"],
  "p3":["<:frogg:699368022107881542>","https://cdn.discordapp.com/emojis/699368022107881542.png?v=1"],
  "p4":["<:pepeok:748521269997207652>","https://cdn.discordapp.com/emojis/748521269997207652.png?v=1"],
  "p5":["<:waitwhat:751211396322295879>","https://cdn.discordapp.com/emojis/751211396322295879.png?v=1"],
  "p6":["<:3nnnn:698924619197054976>","https://cdn.discordapp.com/emojis/698924619197054976.png?v=1"],
  "p7":["<:sadcat:728666854637436958>","https://cdn.discordapp.com/emojis/728666854637436958.png?v=1"],
  "p8":["<:PepeHands:752247218768969908>","https://cdn.discordapp.com/emojis/752247218768969908.png?v=1"],
  "p9":["<:cat11:745333300964491397>","https://cdn.discordapp.com/emojis/745333300964491397.png?v=1"],
  "p10":["<:hmm:723260170028843048>","https://cdn.discordapp.com/emojis/723260170028843048.png?v=1"],
  "p11":["<:taksim:691716815709274242>","https://cdn.discordapp.com/emojis/691716815709274242.png?v=1"],
  "p12":["<:cat10:728666820214522016>","https://cdn.discordapp.com/emojis/728666820214522016.png?v=1"],
  "p13":["<:monkaS:748521269108015144>","https://cdn.discordapp.com/emojis/748521269108015144.png?v=1"],
  "p14":["jerry crying","https://tenor.com/view/tom-y-jerry-tom-and-jerry-meme-sad-cry-gif-18054267"],
  "p15":["kareem's lover","https://cdn.discordapp.com/emojis/788620971484381244.gif?v=1"],
  "p16":["someone dancing","https://cdn.discordapp.com/emojis/731412356902551562.gif?v=1"],
  "p17":["sad cat with a gun","https://cdn.discordapp.com/emojis/606115088235233280.gif?v=1"],
  "p18":["led 3nnnn","https://cdn.discordapp.com/emojis/667653120599523339.gif?v=1"],
  "p19":["confused women","https://tenor.com/view/calculating-puzzled-math-confused-confused-look-gif-14677181"],
  "p20":["pweeees","https://tenor.com/view/agnes-please-despicable-me-gif-11136000"],
  "index":21
}



keys_from_db=db.keys()
def banned_message(author_message):
  print("the robot in the banned_message def")
  if str(author_message.author)=='GHOST#6252':
    print(f"{author_message.author} has been banned")
    return True
  else:
    print(f"{author_message.author}he is good")
    return False

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  
  activity = discord.Game(name="Posting emojis\nmade by:YOUMS#6740")
  await client.change_presence(status=discord.Status.online, activity=activity)
# ------------------------------------------------------------------------

  @client.event
  async def on_message(message):
  
    
    
    
    lower_message=message.content.lower()
    list_words=(lower_message).split()
    print(f"{message.author}==={message.content}")
    if message.author==client.user:
      
      return 
    else:
      if lower_message.startswith('phelp'):
        if banned_message(message):
          await message.channel.send("You have been banned bitch \nstop trying")
        else:
          embed= discord.Embed(title="Help command",description="Type plist: to see the emojis and GIF and if you want to post an emoji just type the code (the message will be deleted)EX:p0 \nType padd:to add a new emoji \nType pdel: to delete an emoji\nType pnew: to see newiest features",color=0x5ce0c2)
          await message.channel.send(embed=embed)
        
      elif lower_message.startswith('plist'):
        if banned_message(message):
          await message.channel.send("You have been banned bitch \nstop trying")        
        else:
          print(f"the user {message.author} used the list cmd")
          to_print_message="the Emojis:\n"
          
          
          
         
          for n in range(len(db)-1):
            if str(n)!="index":
              name=f"p{n}"
             
              to_print_message+=(f"p{n}<<<<<<>>>>>>>{db[name][0]}\n")
            else:
              break
          embed= discord.Embed(title="The list of emojis",description=to_print_message,color=0x5ce0c2)
          await message.channel.send(embed=embed)

      elif any (words in list_words for words in keys_from_db) and len(list_words)==1 :
        if banned_message(message):
          
          await message.channel.send("You have been banned bitch \nstop trying")
        else:
         
          
          for word_from_message in list_words:
            for word_from_source_emojies in keys_from_db:
              if str(word_from_message) == str(word_from_source_emojies):
                print(f"the user {message.author} post an emoji. The emoji code {word_from_message}")
                index_of_word= list(keys_from_db).index(word_from_source_emojies)
                print(index_of_word)
                await message.channel.send(f"{(str(message.author.mention))}")
                await message.channel.send(db[word_from_source_emojies][1])
                await message.delete()
      elif lower_message.startswith('pnew'):
        if banned_message(message):
          
          await message.channel.send("You have been banned bitch \nstop trying")
        else:
          print(f"{message.author} used the pnew command ")
          embed= discord.Embed(title="What's new:",description="Type phelp to see what's new.",color=0x5ce0c2)
          await message.channel.send(embed=embed)
      elif lower_message.startswith('padd'):
        if banned_message(message):
          await message.channel.send("You have been banned bitch \nstop trying")
        else:
          if len(list_words)==3:
            index=db["index"]
            name=(f"p{index}")
            db[name]=[list_words[1],list_words[2]]
            await message.channel.send("The emoji has been added successfully")
            await message.channel.send(db[name][1])
            db["index"]+=1
          else:
            embed=discord.Embed(title="padd command",description="To add a new emoji or GIF please type\npadd name link",color=0x5ce0c2)
            await message.channel.send(embed=embed)
      elif lower_message.startswith("pdel"):
        if len(list_words)==2:
          if banned_message(message):
              await message.channel.send("You have been banned bitch \nstop trying")
          else:
            
            if list_words[1][0]=='p':
                code_number=int(list_words[1][1:])
                if code_number>(db["index"]-1):
                  await message.channel.send("The emoji's code does exist")
                  
                elif db[list_words[1]]==["None(deleted)","The emoji has been deleted"]:
                  embed= discord.Embed(title="Warning",description="emoji already deleted",color=0xFF0000)
                  await message.channel.send(embed=embed)
                  
                else:
                  db[list_words[1]]=["None(deleted)","The emoji has been deleted"]
                  await message.channel.send("The emoji has been deleted successfully")
            else:
              embed=discord.Embed(title="pdel command:",description="To delete an emoji type:\npdel and the emoji's code\nEX: pdel p1 ",color=0x5ce0c2)
              await message.channel.send(embed=embed)
        else:
          embed=discord.Embed(title="Message",description="Invalid value\nType phelp for more information")  
          await message.channel.send(embed=embed)
keep_alive()    
client.run(os.getenv('Token'))
