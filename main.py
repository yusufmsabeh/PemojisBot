import discord
import os
import requests
import json
from replit import db

from keep_alive import keep_alive

client = discord.Client()

# deleting method
# keys=db.keys()
# for n in keys:
#  del db[n]

# printing method
# keys = db.keys()
# for n in keys:
#   print(n)
#   print(db[n])



  
list_of_comds=["plist","paddme","phelp","padd","pedit","pdel"]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="Posting emojis\nType phelp\nmade by:YOUMS#6740")
    await client.change_presence(status=discord.Status.online,
                                 activity=activity)

    
    #******************On message fun*********************
@client.event
async def on_message(message):

    if message.author == client.user:
        return
    else:
       
        lower_message = str(message.content).lower()
        
        list_words = str(message.content).split()
        user_id = str(message.author.id)
        
        
        
        
        # if user_id in db.keys():
        #   values=db.values()
        #   for n in  values:
        #     if lower_message in n:
        
        # list_of_values=db[user_id].split('*')
        # list_of_codes=[]
        # for n in range(len(list_of_values)):
        #   if list_of_values[n]=='':
        #     continue
        # else:
        #   start_code = list_of_values[n].index('{')
        #   end_code = list_of_values[n].index('}')
        #   the_code=list_of_values[n][start_code+1:end_code]
        
        


        #***************************paddme fun**********************
        # This command to create an empty list in database for the user 
        

        if lower_message.startswith('paddme'):

            if user_id in db.keys():                                                                                                                    # If the user is aready added
                embed = discord.Embed(title="Attention",description="You are aready added",color=0xFF5733)
                embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
                await message.channel.send(embed=embed)


            else:                                                                                                                                        
                db[user_id] = ""                                                                                                                        # Create an empty list
                db[f"in{user_id}"] = 0                                                                                                                  # this number will increase if they add a new emoji ,                                                                                                                                           this number for the code
                embed = discord.Embed(title="congratulations",description="You have been added successfully",color=0x3bb54a)
                embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826535666275450900/check.png")
                await message.channel.send(embed=embed)
                
        #************************* phelp fun ************************
        # Printing help message
        elif lower_message.startswith("phelp"):                                                                                                        
            embed=discord.Embed(title="Help command",color=0xb3e59f)
            embed.add_field(name="plist",value="to see the emojis and GIF and if you want to post an emoji just type the code (the message will be deleted)EX:p0",inline=False)
            embed.add_field(name="padd",value="to add a new emoji",inline=True)
            embed.add_field(name="pdel",value="to delete an emoji",inline=True)
            embed.add_field(name="pinvite",value="To recaive an invite ",inline=True)
            embed.add_field(name="pedit",value="to edit the values from the list (name and link)",inline=False)
            
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/827112353057210438/faq.png")
            embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
            embed.set_footer(text="Don't forget to create your own list by typing paddme")
            await message.channel.send(embed=embed)

    
    #******************************* Post fun ***********************************
    # This command will post the emoji if the emoji not found will do nothing
        elif len(list_words) <= 2 and (list_words[0][1:].isdigit())  and lower_message.startswith('p') and not list_words[0].lower() in list_of_comds :
          if len(list_words)==1:
            
            msg=""
          elif len(list_words)==2:                                                        
            if '!' in list_words[1]:                                                                                                                 # Here we fix a problem the problem is when mention someone from phone will 
              user_id= list_words[1][3:-1]                                                                                                           #delete ! form mention 
            else:  
              user_id= list_words[1][2:-1]
            
            msg=f"<@{str(user_id)}>"
          
          
          if not (user_id in db.keys()):                                                                                                             #If the user not added
            men="<@"+str(user_id)+">"
            embed = discord.Embed(title="User not found",description=f"{men} are not added yet\nType paddme and try again",color=0xFF5733)
            embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
            await message.channel.send(embed=embed)
            
            
          else:
            
            value = db[user_id].split("*")
            the_code =list_words[0].lower()
            
            i = 0
            found = False
            for n in value:
              if the_code in n:
                found = True
                break
              else:
                i += 1
            if not found:
              return
            else:
              block_value = value[i]
              start_link = block_value.index("[")
              end_link = block_value.index("]")
              start_code = block_value.index("{")
              end_code = block_value.index("}")
              code = block_value[start_code + 1:end_code].strip()
              link = block_value[start_link + 1:end_link]
              
              # await message.channel.send(message.author.mention + ":" +code+"")
              await message.channel.send(f"{message.author.mention}:{code}  {msg}")
              await message.channel.send(link)
              # embed = discord.Embed(title=code,color=0x2f3136)
              # embed.add_field(url=link)
              # embed.set_footer(text=f"Requested by {message.author.display_name}",icon_url=message.author.avatar_url)
              # await message.channel.send(embed=embed)
              await message.delete()

    # ****************padd method****************

        elif lower_message.startswith('padd'):
            if not (user_id in db.keys()):
              men="<@"+str(user_id)+">"
              embed = discord.Embed(title="User not found",description=f"{men} are not added yet\nType paddme and try again",color=0xFF5733)
              embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
              embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
              await message.channel.send(embed=embed)
            else:
                if '-' in lower_message :
                    index_name=lower_message.find('-')
                    index_link = lower_message.find('-',index_name+1)
                    the_name=lower_message[index_name+1:index_link].strip()
                    the_link =lower_message[index_link+1:].strip()
                    the_index = db[f"in{user_id}"]
                    the_code = f"p{the_index}"
                    new_value = f"*{{{the_code}}} ({the_name}) [{the_link}]"
                    db[user_id] =db[user_id]+new_value
                    db[f"in{user_id}"] = the_index + 1
                    
                    embed = discord.Embed(title="Added successfully",description=f"The emoji has been added successfully\nType {the_code}",color=0x3bb54a)
                    embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826535666275450900/check.png")
                    await message.channel.send(embed=embed)
                else:
                  embed = discord.Embed(title=" something went wrong",description="To add a new emoji or GIF please type\npadd -the name -the link",color=0xFF5733)
                  embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
                  await message.channel.send(embed=embed)

    #************plist*******************

        elif lower_message.startswith('plist'):
          if len(list_words)==1:
            
            user_id=message.author.id
          elif len (list_words)==2:
            if '!' in list_words[1]: 
              user_id=list_words[1][3:-1]
            else:
              user_id=list_words[1][2:-1]
           
          else:
            embed = discord.Embed(title="Attention",description="plist mention (to show someone's list)\njust plist(to show your own list)",color=0xFF5733)
            embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
            await message.channel.send(embed=embed)

            return
          if not (user_id in db.keys()):
           
            men="<@"+str(user_id)+">"
            embed = discord.Embed(title=f"User not found ",description=f"{men} are not added yet\nType paddme and try again",color=0xFF5733)
            embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
            await message.channel.send(embed=embed)
          else:
            men="<@"+str(user_id)+">"
            to_print = ""
            value = db[user_id].split("*")
            for n in value:
              if len(n) <= 1:
                continue
              else:
                start_code = n.index('{')
                end_code = n.index('}')
                start_name = n.index('(')
                end_name = n.index(')')
                start_link = n.index('[')
                end_link = n.index(']')
                to_print += (f"{n[start_code+1:end_code]}=======>{n[start_name+1:end_name]}\n")
                
            embed = discord.Embed(description=(f"**{men} list**\n{to_print}"),color=0xa568f3)
            
            embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826546249389179020/checklist.png")
            await message.channel.send(embed=embed)


#**********************************Pdel fun************************************************

        elif lower_message.startswith('pdel'):
            if not (user_id in db.keys()):
              
              men="<@"+str(user_id)+">"
              embed = discord.Embed(title="User not found",description=f"{men} are not added yet\nType paddme and try again",color=0xFF5733)
              embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
              embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
              await message.channel.send(embed=embed)
              
            else:
               
                if len(list_words) == 2:
                    values = db[user_id].split('*')
                    code_to_del = list_words[1].lower()
                    index = 0
                    found = False
                    for n in values:
                        if code_to_del in n:
                            index = values.index(n)
                            found = True
                            break
                        else:
                            continue
                    if found:

                        new_one = ""
                        index_2 = 0
                        for n in values:
                            if index_2 != index:
                                new_one += "*" + n
                            index_2 += 1
                       
                        db[user_id] = new_one
                        embed = discord.Embed(title="deleted successfully",description=f"The emoji has been deleted successfully",color=0x3bb54a)
                        embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826535666275450900/check.png")
                        await message.channel.send(embed=embed)

                    else:
                      embed = discord.Embed(title="Attention",description="The emoji does not exist or aready deleted",color=0xFF5733)
                      embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
                      await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title=" something went wrong",description="To delete  an emoji or GIF \nType pdel the code\nEX: pdel p3",color=0xFF5733)
                    embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
                    await message.channel.send(embed=embed)
        #*****************************pinvte*************************
        elif lower_message.startswith('pinvite'):
          embed=discord.Embed(title="Invite links",description="[Invite me to your server](https://discord.com/api/oauth2/authorize?client_id=821037249108901918&permissions=10240&scope=bot)\n[Join our server](https://discord.gg/aANasZ8Tbr)",color=0x428dff)
          
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826928353264926800/game.png")
          await message.author.send(embed=embed)
          emoji = '\N{THUMBS UP SIGN}'
          await message.add_reaction(emoji)
        #************************how many***************************
        elif lower_message.startswith('phmy'):
          
          activeservers = client.guilds
          num =0
          for n in activeservers:
            num+=1
            print(n.name)
          print(num)


        #******************pedit command****************************

        elif lower_message.startswith('pedit'):
            if not (user_id in db.keys()):

              men="<@"+str(user_id)+">"
              embed = discord.Embed(title="User not found",description=f"{men} are not added yet\nType paddme and try again",color=0xFF5733)
              embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
              embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
              await message.channel.send(embed=embed)
                
              
            elif len(list_words) >= 4:
                
                
                if list_words[2].lower() == 'name' or list_words[2].lower()=='link':
                    list_of_values = db[user_id].split('*')
                    i = 0
                    found = False
                    for n in list_of_values:
                        if (n.find(list_words[1]) == -1):
                            i += 1

                        else:
                            found = True
                            break
                    if not found:
                      embed = discord.Embed(title="Not found",description="The emoji does not exist or get deleted",color=0xFF5733)
                      embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                      embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
                      await message.channel.send(embed=embed)
                    else:

                        old_value = list_of_values[i]
                        start_code = old_value.index('{')
                        end_code = old_value.index('}')
                        start_name = old_value.index('(')
                        end_name = old_value.index(')')
                        start_link = old_value.index('[')
                        end_link = old_value.index(']')
                        the_code2 = old_value[start_code + 1:end_code].strip()
                        the_name2 = old_value[start_name + 1:end_name].strip()
                        the_link2 = old_value[start_link + 1:end_link].strip()
                        edited_value=""
                        for n in list_words[3:]:
                          edited_value+=n+" "
                        if list_words[2].lower()=='name':
                          
                          new_value = "{" + the_code2 + "} " + "(" + edited_value.strip() + ") " + "[" + the_link2 + "]"
                          list_of_values[i] = new_value
                          new_one = ""
                          for n in list_of_values:
                              new_one += "*" + n
                          db[user_id] = new_one
                          embed = discord.Embed(title="Edited successfully",description=f" emoji's name has been edited successfully",color=0x3bb54a)
                          embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826535666275450900/check.png")
                          await message.channel.send(embed=embed)
                        elif list_words[2].lower()=='link':
                          new_value = "{" + the_code2 + "} " + "(" + the_name2 + ") " + "[" +edited_value.strip() + "]"
                          list_of_values[i] = new_value
                          new_one = ""
                          for n in list_of_values:
                            new_one += "*" + n
                          db[user_id] = new_one
                          embed = discord.Embed(title="Edited successfully",description=f" emoji's link has been edited successfully",color=0x3bb54a)
                          embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826535666275450900/check.png")
                          await message.channel.send(embed=embed)
                        else:
                          embed = discord.Embed(title="Something went wrong",description="Invalid value\nType pedit for more information",color=0xFF5733)
                          embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
                          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826021805911179284/attention.png")
                          await message.channel.send(embed=embed)
                 
            else:
              embed = discord.Embed(title="pedit command",description="To edit an emoji please type\npedit {the code of emoji} {name or link} {new value}\nwithout {}",color=0xFF5733)
              embed.set_author(name=message.author.display_name , icon_url=message.author.avatar_url)
              embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/821673459716587551/826854639517302825/information.png")
              await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('Token'))
