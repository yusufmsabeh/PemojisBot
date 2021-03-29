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
        print(message.author.id)
        lower_message = str(message.content).lower()
        print(lower_message)
        list_words = str(message.content).split()
        user_id = str(message.author.id)
        old_id_2=str(message.author)[-4:]
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

        if lower_message.startswith('paddme'):

            if user_id in db.keys():
                await message.channel.send("You are aready added")
            else:
                # checkin_moved(message)
                db[user_id] = ""
                db[f"in{user_id}"] = 0
                await message.channel.send(
                    "congratulations You have been added successfully")

        elif lower_message.startswith("phelp"):
            embed = discord.Embed(
                title="Help command",
                description=
                "This the new version of pemojis \n Here you have your own list and you can add, del and edit on it\n**List of commands** \nType plist: to see the emojis and GIF and if you want to post an emoji just type the code (the message will be deleted)EX:p0 \nType padd:to add a new emoji \nType pdel: to delete an emoji\nType pedit to edit the values from the list (name and link) \nDon't forget to create your own list by typing **paddme**\n**__And also you can check your friend's list and post from it__**",
                color=0x7ce0c2)
            await message.channel.send(embed=embed)

    #***************************Moveme fun**********************
        # elif lower_message.startswith("pmoveme"):
        #   if message.author.id in moved_members:
        #     await message.channel.send("You are aready moved")
        #   else:
        #     user_id_new = message.author.id
        #     old_user_id=str(message.author)[-4:]
        #     value=db[old_user_id]
        #     index_no=db[f"in{old_user_id}"]
        #     del db[old_user_id]
        #     del db[f"in{old_user_id}"]
        #     db[user_id_new]=value
        #     db[f"in{user_id_new}"]=index_no
        #     moved_members.append(user_id_new)
        #     await message.channel.send("if you are wondering what this command does it moves the data that you added to a another key")


    #******************************* Post fun ***********************************
        elif len(list_words) <= 2 and list_words[0][1:].isdigit()  and lower_message.startswith('p') and not list_words[0].lower() in list_of_comds :
          if len(list_words)==1:
            user_id=message.author.id
          elif len(list_words)==2:
            user_id= list_words[1][3:-1]
          else:
            await message.channel.send("plist mention(to show someone's list) or just plist(to show your own list) ")
            return
          
          if not (user_id in db.keys()):
                await message.channel.send(
                    "You are not added yet\nType paddme and try again")
            
          else:
            print("iam in mf")
            value = db[user_id].split("*")
            the_code =list_words[0].lower()
            print(value)
            i = 0
            found = False
            for n in value:
              print("the n " + n)
              if the_code in n:
                found = True
                break
              else:
                i += 1
            if not found:
              return
            else:
              print(value)
              block_value = value[i]
              print("the value " + block_value)
              start_link = block_value.index("[")
              end_link = block_value.index("]")
              start_code = block_value.index("{")
              end_code = block_value.index("}")
              code = block_value[start_code + 1:end_code].strip()
              link = block_value[start_link + 1:end_link]
              await message.channel.send(message.author.mention + ":" +code)
              await message.channel.send(link)
              await message.delete()

    # ****************padd method****************

        elif lower_message.startswith('padd'):
            print("you son of bth i am in")
            if not (user_id in db.keys()):
                await message.channel.send(
                    "You are not added yet\nType paddme and try again")
            else:
                # checkin_moved(message)
                print("in the padd fun")
                if '(' in message.content and ')' in message.content and '[' in message.content and ']' in message.content:
                    message_one = message.content
                    start_of_name = message_one.find("(")
                    end_of_name = message_one.find(")")
                    start_of_link = message_one.find("[")
                    end_of_link = message_one.find("]")
                    the_name = message_one[start_of_name +
                                           1:end_of_name].strip()
                    the_link = message_one[start_of_link +
                                           1:end_of_link].strip()
                    the_index = db[f"in{user_id}"]
                    the_code = f"p{the_index}"
                    temp_value = db[user_id]
                    new_value = f"{{{the_code}}} ({the_name}) [{the_link}]"
                    final_value = f"{temp_value}*{new_value}"
                    print(final_value)
                    db[user_id] = final_value

                    db[f"in{user_id}"] = the_index + 1
                    await message.channel.send("added successfully")
                else:
                    embed = discord.Embed(
                        title="padd command",
                        description=
                        "To add a new emoji or GIF please type\npadd (name) [link]\n type with () and []",
                        color=0x5ce0c2)
                    await message.channel.send(embed=embed)

    #************plist*******************

        elif lower_message.startswith('plist'):
          if len(list_words)==1:
            user_id=message.author.id
          elif len (list_words)==2:
            print("elif ")
            user_id=list_words[1][3:-1]
          else:
            await message.channel.send("plist mention(to show someone's list) or just plist(to show your own list) ")
            return
          if not (user_id in db.keys()):
            await message.channel.send("You are not added yet\nType paddme and try again")
          else:
            print(user_id)
            to_print = ""
            value = db[user_id].split("*")
            print(db[user_id])
            print(value)
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
                print(to_print)
            embed = discord.Embed(title="The list of emojis:",description=(f"{to_print}"),color=0x5ce0c2)
            await message.channel.send(embed=embed)


#**********************************Pdel fun************************************************

        elif lower_message.startswith('pdel'):
            if not (user_id in db.keys()):
              
                await message.channel.send(
                    "You are not added yet\nType paddme and try again")
              
            else:
               
                if len(list_words) == 2:
                    print("iam in")
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
                        print(new_one)
                        db[user_id] = new_one
                        await message.channel.send("deleted successfully")

                    else:
                        await message.channel.send(
                            "The emoji does not exist or aready deleted")
                else:
                    await message.channel.send("invalid value")

        #******************pedit command****************************

        elif lower_message.startswith('pedit'):
            print("pedit command")
            if not (user_id in db.keys()):
              
                await message.channel.send(
                    "You are not added yet\nType paddme and try again")
              
            elif len(list_words) >= 4:
                
                print("entred")
                if list_words[2].lower() == 'name':
                    print("entred 2")
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
                        await message.channel.send("The emoji does not exist")
                        print("helloo")
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
                        print(type(list_words[3]))
                        edited_value=""
                        for n in list_words[3:]:
                          edited_value+=n+" "
                        new_value = "{" + the_code2 + "} " + "(" + str(edited_value) + ") " + "[" + the_link2 + "]"
                        list_of_values[i] = new_value
                        new_one = ""
                        for n in list_of_values:
                            new_one += "*" + n
                        db[user_id] = new_one
                elif list_words[2].lower() == 'link':
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
                        await message.channel.send("The emoji does not exist")
                    else:
                        print(i)
                        old_value = list_of_values[i]
                        start_code = n.index('{')
                        end_code = n.index('}')
                        start_name = n.index('(')
                        end_name = n.index(')')
                        start_link = n.index('[')
                        end_link = n.index(']')
                        the_code2 = old_value[start_code + 1:end_code].strip()
                        the_name2 = old_value[start_name + 1:end_name].strip()
                        the_link2 = old_value[start_link + 1:end_link].strip()
                        print(type(list_words[3]))
                        print(list_words)
                        new_value = "{" + the_code2 + "} " + "(" + the_name2 + ") " + "[" + list_words[3:] + "]"
                        list_of_values[i] = new_value
                        new_one = ""
                        for n in list_of_values:
                            new_one += "*" + n
                        db[user_id] = new_one
                else:
                    await message.channel.send(
                        'Invalid value\nType pedit for more information')
            else:
                embed = discord.Embed(
                    title="pedit command",
                    description=
                    "To edit an emoji please type\npedit {the code of emoji} {name or link} {new value}\nwithout {} new value must be just one word",
                    color=0x5ce0c2)
                await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('Token'))
