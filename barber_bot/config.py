import os
from dotenv import load_dotenv

load_dotenv()

# Telegram
TOKEN = os.getenv("TOKEN")

# Google Sheets
SPREADSHEET_ID = "16bF1JAv7fI1ryovqXFYwfWhwqqi4aUtSYFEkGAdD39M"
GOOGLE_CREDS_FILE = "barber-bot.json"
