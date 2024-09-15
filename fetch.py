from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
import pandas as pd
import re

# Your Telegram API credentials
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API hash
phone = 'YOUR_PHONE_NUMBER'  # Replace with your phone number

# Function to fetch messages from a channel and extract URLs
def fetch_urls_from_messages(client, channel_name, limit=100):
    channel = client.get_entity(channel_name)
    result = client(GetHistoryRequest(
        peer=channel,
        limit=limit,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    messages = result.messages
    
    # List to store extracted URLs
    urls = []
    
    # Regular expression to match URLs
    url_pattern = r'(https?://[^\s]+)'
    
    # Extract URLs from the messages
    for message in messages:
        if message.message:  # Check if the message has content
            found_urls = re.findall(url_pattern, message.message)
            if found_urls:
                for url in found_urls:
                    # Remove timezone info from datetime
                    message_date = message.date.replace(tzinfo=None)
                    urls.append([message.id, message_date, message.sender_id, url])
    
    return urls

# Write URLs to Excel
def write_to_excel(urls, filename='telegram_urls.xlsx'):
    # Create a DataFrame and write to Excel
    df = pd.DataFrame(urls, columns=['Message ID', 'Date', 'Sender ID', 'URL'])
    df.to_excel(filename, index=False)
    print(f'URLs written to {filename}')

# Main program
if __name__ == '__main__':
    # Create the Telegram client
    client = TelegramClient('session_name', api_id, api_hash)

    # Connect to Telegram
    client.connect()

    # Check if already authorized, else prompt for the code
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))

    # Specify the Telegram channel's username or ID
    channel_name = 'your_channel_name'  # Replace with the channel's username or ID

    # Fetch the URLs from the channel messages
    urls = fetch_urls_from_messages(client, channel_name, limit=100)

    # Write the extracted URLs to an Excel file
    write_to_excel(urls)

    # Disconnect the client
    client.disconnect()
