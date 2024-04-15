print("Hello! It's program to create ping bot.")

channels = []
print("Step 1: Enter channels IDs where bot will send @everyone message")
while True:
    channel = input("ID: ")

    if channel.lower() == "done":
        print("Finishing step...")
        break

    try:
        channel = int(channel)
    except:
        print("It's seems like you entered not an integer value.\nNOTE: Integer = any number like 1, 2, 3, etc")
        continue

    channels.append(int(channel))
    print("Well! You can add more channels or type 'Done' for next step")

print("Step 2: Now you need to enter bot token. You can get it here: https://discord.com/developers/applications\nNOTE: Recommended to create bot on alt account to bypass main account ban")
token = input("Token: ")

texts = ["@everyone"]
print("Step 3: Enter custom text(s) what will send to channels. @everyone already included in message")
while True:
    text = input("Text: ")

    if text.lower() == "done":
        print("Finishing step...")
        break

    texts.append("@everyone\n" + text)
    print("Well! You can add more channels or type 'Done' for next step")

print("Step 4: Building...")

f = open("bases/bot.txt", "r").read()

code = f.replace("{{channels}}", str(channels))
code = code.replace("{{token}}", str(token))
code = code.replace("{{texts}}", str(texts))

bot = open("builds/bot.py", "+a")
bot.write(code)
bot.close()

print("Done! I created a file with name bot.py in 'builds' directory. If you want to create another bot, start this program again and rename bot.py")
input("[ENTER]")