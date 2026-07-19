# MULTITHREADING --> USED TO PERFORM MULTIPLE TASK CONCURRENTLY (MULTITHREADING) .... GOOD FOR I/O BOUND TASKS LIKE READING FILTERS OR FETCHING DATA FROM APIs THREADING ... THREAD (TARGET=MY_FUNCTION)

import threading
import time

def walk_dog():
    time.sleep(9)
    print("you finished walking the dog")

def take_out_trash():
    time.sleep(3)
    print("you take out trash")

def get_mail():
    time.sleep(5)
    print("you get the mail")

# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("udayan singh")