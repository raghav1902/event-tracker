
# Event Discovery & Tracking Tool

## Overview

This project is a working prototype of an **event discovery and tracking system**.
The goal is to collect city-based event information, store it in a structured format, and keep it updated over time with support for deduplication and automation.

The tool is designed to simulate a real operational workflow where event data is ingested, processed, and maintained in a central sheet for further analysis or use.

---

## Problem Statement

Event platforms frequently update their listings, making it difficult to maintain an up-to-date dataset of events.
This tool demonstrates how such data can be:

* Collected periodically
* Stored in a structured format
* Updated without creating duplicates
* Extended to mark expired or outdated events

---

## Key Features

* City-based event tracking
* Configurable data ingestion layer
* Google Sheets used as a lightweight database
* Hash-based deduplication of events
* Designed for repeated and scheduled execution
* Clean separation of scraping/ingestion and storage logic

---

## Tech Stack

* **Language:** Python 3
* **Storage:** Google Sheets
* **Libraries:**

  * `requests`
  * `gspread`
  * `oauth2client`

---

## Project Structure

```
event-tracker/
├── scraper.py              # Main ingestion and update logic
├── sheets.py               # Google Sheets interaction
├── config.py               # Configuration and constants
├── events_sample.json      # Sample event data (input source)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files (credentials, cache)
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/event-tracker.git
cd event-tracker
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Google Sheets Setup

1. Create a new Google Sheet named:

   ```
   event_tracker
   ```
2. Rename the first tab to:

   ```
   events_master
   ```
3. Add the following headers in row 1:

   ```
   event_id | name | date | venue | city | status | last_seen | url
   ```

---

### 4. Google API Credentials

1. Create a Service Account in Google Cloud Console
2. Enable:

   * Google Sheets API
   * Google Drive API
3. Download the service account key (JSON)
4. Rename it to:

   ```
   service_account.json
   ```
5. Place it in the project root directory
   (This file is ignored by Git and should not be committed)

---

### 5. Run the Tool

```bash
python scraper.py
```

After execution, event records will be inserted into the Google Sheet.

---

## Data Ingestion Approach

Direct scraping of major event platforms can be unreliable due to rate limits and anti-bot protections.
To keep the prototype stable and reproducible, the system uses a **configurable ingestion layer**.

For this implementation:

* Event data is loaded from a local JSON file
* The same processing, deduplication, and update logic applies regardless of source
* The ingestion layer can later be replaced with official APIs or partner feeds


## Deduplication Logic

Each event is assigned a unique `event_id` generated using:

* Event name
* Date
* Venue
* City

This ensures that:

* Repeated runs do not insert duplicate events
* Existing events can be updated safely


## Future Enhancements

* Replace sample data with official APIs or licensed data sources
* Add automated scheduling (cron / GitHub Actions)
* Implement expiry detection for past events
* Support multiple cities and platforms


## Conclusion

This project demonstrates a practical approach to event tracking with an emphasis on data reliability, automation readiness, and clean system design.
It focuses on building a maintainable pipeline rather than relying on brittle scraping techniques.

