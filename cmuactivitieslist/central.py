import schedule
import time
from convert import *

def run():
    retrive()

schedule.every().day.at("1:00").do(run)

while True:
    schedule.run_pending()
    time.sleep(60)
