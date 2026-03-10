import time
import schedule
from main import run_ai_system


def start_scheduler():

    print("AI Scheduler Started")

    # Har 1 ghante me client search
    schedule.every(1).hours.do(run_ai_system)

    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    start_scheduler()
