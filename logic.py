import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# Области доступа
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Укажите путь к файлу с OAuth 2.0 учетными данными
CLIENT_SECRET_FILE = "credentials.json"

# Функция для получения учетных данных
def get_credentials():
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if creds and creds.valid:
            return creds
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open("token.json", "w") as token:
                token.write(creds.to_json())
            return creds
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())
    return creds

# Получаем учетные данные
creds = get_credentials()

# Подключаемся к Google Sheets API
service = build("sheets", "v4", credentials=creds)

# ID таблицы (замените на ваш ID)
SPREADSHEET_ID = "1mq1OgHD3RwuKlelbUPkqgicjCoFAV683bkzHyt-tQ1s"


def read_cell(cell_range):
    result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=cell_range).execute()
    value = result.get("values", [])
    return value

def read():
    # Чтение диапазона ячеек (например, A1:C10)
    c1 = []
    range_values = read_cell("A2:A17")
    for i in range_values:
        c1.append(i[0])
    c2 = []
    range_values = read_cell("C2:C17")
    for i in range_values:
        c2.append(i[0])
    c3 = []
    range_values = read_cell("E2:E17")
    for i in range_values:
        c3.append(i[0])
    c4 = []
    range_values = read_cell("G2:G17")
    for i in range_values:
        c4.append(i[0])

    return c1, c2, c3, c4