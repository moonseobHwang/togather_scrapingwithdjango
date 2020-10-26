import schedule
import time

def job():
    print("I'm working...")

schedule.every(5).seconds.do(job)

# reference other file
import sample_function
schedule.every(24).hours.do(sample_function.print_message)

while True:
    schedule.run_pending()
    time.sleep(1)

# run python3 ./job01.py    # in Terminal