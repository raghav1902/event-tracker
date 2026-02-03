# scraper.py

import json
import hashlib
from datetime import datetime

from config import INPUT_FILE, SHEET_NAME, WORKSHEET_NAME
from sheets import get_sheet, load_existing_event_ids, insert_events


def generate_event_id(name, date, venue, city):
    raw = f"{name}{date}{venue}{city}"
    return hashlib.md5(raw.encode()).hexdigest()


def fetch_events_from_file():
    print("Loading events from local data source...")

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    events = []

    for item in data.get("events", []):
        event_id = generate_event_id(
            item["name"],
            item["date"],
            item["venue"],
            item["city"]
        )

        events.append({
            "event_id": event_id,
            "name": item["name"],
            "date": item["date"],
            "venue": item["venue"],
            "city": item["city"],
            "status": "upcoming",
            "last_seen": datetime.today().strftime("%Y-%m-%d"),
            "url": item["url"]
        })

    print(f"Loaded {len(events)} events")
    return events


def main():
    sheet = get_sheet(SHEET_NAME, WORKSHEET_NAME)
    existing_ids = load_existing_event_ids(sheet)

    events = fetch_events_from_file()
    new_events = [e for e in events if e["event_id"] not in existing_ids]

    insert_events(sheet, new_events)
    print(f"Inserted {len(new_events)} new events")


if __name__ == "__main__":
    main()
