
# Telegram URL Fetcher

This Python script extracts URLs from messages in a specified Telegram channel and writes the URLs into an Excel file.

## Requirements

To run the script, you will need the following:
- Python 3.x
- A Telegram account
- Telegram API credentials (API ID and API hash)
- The following Python libraries:
  - `telethon`
  - `pandas`
  - `openpyxl`
  - `re` (part of the Python Standard Library)

## Setup

### 1. Install Python Packages

Before running the script, make sure to install the required packages. You can do so by running the following commands:

```bash
pip install telethon pandas openpyxl
```

### 2. Telegram API Setup

1. Go to [my.telegram.org](https://my.telegram.org/) and log in with your Telegram account.
2. Create a new application under the "API development tools" section.
3. You will receive your **API ID** and **API hash**. Keep these credentials safe as you'll need them to run the script.

### 3. Script Configuration

In the script, replace the placeholder values with your actual API credentials and phone number:

```python
api_id = 'YOUR_API_ID'  # Replace with your API ID
api_hash = 'YOUR_API_HASH'  # Replace with your API hash
phone = 'YOUR_PHONE_NUMBER'  # Replace with your phone number
```

Also, specify the channel name from which you want to extract URLs:

```python
channel_name = 'your_channel_name'  # Replace with the channel's username or ID
```

### 4. Running the Script

Once you've set up your environment, you can run the script by executing the following command in your terminal:

```bash
python fetch.py
```

### 5. Script Flow

1. The script connects to Telegram using the `telethon` library.
2. It fetches a specified number of messages from a channel.
3. Using a regular expression, it extracts all URLs found in the messages.
4. The extracted URLs, along with message metadata (Message ID, Date, Sender ID), are saved into an Excel file (`telegram_urls.xlsx`).

## Script Breakdown

- **fetch_urls_from_messages**: This function fetches messages from a specified Telegram channel and extracts URLs using a regular expression.
- **write_to_excel**: This function writes the extracted URLs and message metadata into an Excel file.

## Example Output

The Excel file (`telegram_urls.xlsx`) will have the following columns:
- **Message ID**: The unique ID of the message where the URL was found.
- **Date**: The timestamp of the message.
- **Sender ID**: The ID of the sender who sent the message.
- **URL**: The URL extracted from the message.

## Limitations

- The script fetches up to a specified limit of messages (default is 100). You can change this limit by modifying the `limit` argument in the `fetch_urls_from_messages` function.
- The script assumes the channel is public or you have access to the channel via your Telegram account.

