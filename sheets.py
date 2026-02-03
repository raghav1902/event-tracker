# sheets.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDS_FILE = os.path.join(BASE_DIR, "service_account.json")

def get_sheet(sheet_name, worksheet_name):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        CREDS_FILE, scope
    )

    client = gspread.authorize(creds)
    return client.open(sheet_name).worksheet(worksheet_name)


def load_existing_event_ids(sheet):
    records = sheet.get_all_records()
    return {row["event_id"] for row in records}


def insert_events(sheet, events):
    if not events:
        return

    rows = []
    for e in events:
        rows.append([
            e["event_id"],
            e["name"],
            e["date"],
            e["venue"],
            e["city"],
            e["status"],
            e["last_seen"],
            e["url"]
        ])

    sheet.append_rows(rows, value_input_option="RAW")
