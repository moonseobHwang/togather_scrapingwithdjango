import schedule
import time

def job():
    print("I'm working...")

# schedule.every(5).seconds.do(job)

# reference other file
# import sample_function
# schedule.every(3).seconds.do(sample_function.print_message)
from scraping_kstartup import scraping_kstartup
# schedule.every(1).minutes.do(scraping_kstartup)
schedule.every().day.at("8:30").do(scraping_kstartup)

while True:
    schedule.run_pending()
    time.sleep(1)

# run python3 ./startup02.py    # in Terminal