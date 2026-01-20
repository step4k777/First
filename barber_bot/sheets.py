import gspread
from google.oauth2.service_account import Credentials
from config import GOOGLE_CREDS_FILE, SPREADSHEET_ID

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(GOOGLE_CREDS_FILE, scopes=scopes)
client = gspread.authorize(creds)

def get_barbers():
    """Возвращает список барберов из листа 'barbers'"""
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("barbers")  # правильный лист
    records = sheet.get_all_records()
    # вернем только имена барберов
    return [row["Барбер"] for row in records]

def get_services():
    """Возвращает список услуг из листа 'services'"""
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("services")  # используем open_by_key
    records = sheet.get_all_records()
    return records 

def get_busy_times(date: str, barber: str):
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("schedule")
    records = sheet.get_all_records()

    busy = []
    for row in records:
        if row["Дата"] == date and row["Барбер"] == barber:
            busy.append(row["время"])

    return busy

def add_booking(date, time, barber, service, phone):
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("schedule")
    sheet.append_row([date, time, barber, service, phone])

def get_records():
    """Все существующие записи"""
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("schedule") 
    return sheet.get_all_records()

def add_record(data: dict):
    """Добавить новую запись"""
    sheet = client.open_by_key(SPREADSHEET_ID).worksheet("schedule")
    sheet.append_row([
        data["date"],
        data["time"],
        data["barber"],
        data["service"],
        data["name"],
        data["phone"]
    ])