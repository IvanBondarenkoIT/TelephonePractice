from telethon.sync import TelegramClient
from datetime import datetime, timedelta

import config

# Replace these values with your own API ID and hash
api_id = config.YOUR_API_ID
api_hash = config.YOUR_API_HASH

# Replace 'phone_number' with your own phone number
phone_number = config.YOUR_PHONE_NUMBER
two_fa_password = config.YOUR_PASSWORD

# Define the start and end dates for the period you want to fetch files from
start_date = datetime(2024, 2, 1)
end_date = datetime(2024, 2, 29)

# Create a new TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)


async def fetch_files():
    # Connect the client
    await client.start(phone=phone_number, password=two_fa_password)

    # List to store file paths
    file_paths = []
    # Iterate over the messages in the group within the specified date range
    # my_test_group
    async for message in client.iter_messages('my_test_group', offset_date=start_date, reverse=True):
        # Check if the message is within the specified date range
        if start_date <= message.date <= end_date:
            # Check if the message contains any media
            if message.media:
                # Download the media file and store the path
                file_path = await message.download_media()
                print(file_path)
                file_paths.append(file_path)

            # Check if the message is a text message
            if message.text:
                # Print the text of the message
                print(message.text)

    # Disconnect the client
    await client.disconnect()

    # Print the file paths
    print("File paths:")
    for path in file_paths:
        print(path)

# Run the fetch_files coroutine
with client:
    client.loop.run_until_complete(fetch_files())
    print()
