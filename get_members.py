import csv
from config import*
from telethon import TelegramClient, sync


client = TelegramClient(None, api_id, api_hash)
client.start()

#client.connect()
# if not client.is_user_authorized():
#    client.send_code_request(phone)
#    client.sign_in(phone, input('Enter the code: '))




def get_channels():
    # get all the channels that I can access
    channels = {d.entity.username: d.entity
            for d in client.get_dialogs()
            if d.is_channel}
    for i,channel_name in enumerate(channels.keys()):
        try:print(f"{i} ::: {channel_name}")
        except:pass

    channel_id = int(input("Please select a number :: "))

    channel_name = list(channels.keys())[channel_id]
    channel = channels[channel_name]
    print(f"\n\nYou have selected:: {channel_name}")

    print("\n\nGetting the members of this channel\n")

    try:
        with open(f'{channel_name}.csv', mode='w+') as csv_file:
            fieldnames = ['username','id','access_hash','name']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            
            # get all the users and print them
            for user in client.get_participants(channel):
                name = f"{user.first_name} {user.last_name}"
                writer.writerow({'username': user.username,'id':user.id,'access_hash':user.access_hash,'name':name})
                #print(user.username,user.id,user.access_hash,name)
            return(f"Users from ({channel_name}) have been copied successfully")
    except Exception as e:
		    print(f"An error occurred because:: {e}")
		    get_channels()
		    
try:
    get_channels()
except Exception as e:
    print(e)
		     

