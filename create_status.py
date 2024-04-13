print("Hello! It's program to create status bot.")

print("Step 1: Enter prefix")
prefix = input("Prefix: ")

print("Step 2: Enter Guild ID where bot(s) located")
while True:
    guildid = input("ID: ")
    try:
        guildid = int(guildid)
    except:
        print("It's seems like you entered not an integer value.\nNOTE: Integer = any number like 1, 2, 3, etc")
        continue

    break

print("Step 3: Enter Bot(s) ID(s)")
bots = []
while True:
    bot = input("ID: ")

    if bot.lower() == "done":
        print("Finishing step...")
        break

    try:
        bot = int(bot)
    except:
        print("It's seems like you entered a not an integer value.\nNOTE: Integer = any number like 1, 2, 3, etc")
        continue

    bots.append(int(bot))
    print("Well! You can add more IDs or type 'Done' for next step")

print("Step 4: Enter Channel ID where located status message BY BOT.")
while True:
    channelid = input("ID: ")


    try:
        channelid = int(channelid)
    except:
        print("It's seems like you entered not an integer value.\nNOTE: Integer = any number like 1, 2, 3, etc")
        continue

    break

print("Step 5: Enter Status Message ID sended BY BOT. If it's not exists, skip this step")
print("NOTE: You can use 'generate_ids.py' to generate ID")
while True:
    messageid = input("ID: ")
    if messageid == "":
        messageid = "replace it manually"
        break


    try:
        messageid = int(messageid)
    except:
        print("It's seems like you entered not an integer value.\nNOTE: Integer = any number like 1, 2, 3, etc")
        continue

    break

print("Step 6: Now you need to enter bot token. You can get it here: https://discord.com/developers/applications")
token = input("Token: ")

print("Step 7: Building...")
if messageid == "replace it manually":
    input(f"\nNOTE: On line {'33 and 34' if channelid == 'replace it manually' else '34'} located text 'replace it manually'. Status doesn't update if this values keep in file. You need to replace it after building\nNOTE 2: 33 line - channel ID where located message with bot(s) status\n34 line - message ID with bot(s) status. You can send message using command {prefix}send\n\n[ENTER]")

f = open("bases/status.txt", "r").read()
code = f.replace("{{prefix}}", str(prefix))
code = code.replace("{{gid}}", str(guildid))
code = code.replace("{{ids}}", str(bots))
code = code.replace("{{cid}}", str(channelid))
code = code.replace("{{mid}}", str(messageid))
code = code.replace("{{token}}", str(token))

bot = open("builds/status.py", "+a")
bot.write(code)
bot.close()

print(f"Done! I created a file with name status.py in 'builds' directory.")
input("[ENTER]")