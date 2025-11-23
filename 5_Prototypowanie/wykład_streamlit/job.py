import schedule, time
from datetime import datetime

def run_scraper():
    print(f"[{datetime.now()}] Uruchamiam scraper...")
    # tutaj Twój kod scrapera

schedule.every(24).hours.do(run_scraper)

while True:
    schedule.run_pending()
    time.sleep(60)
