from tkinter import *
import datetime
import time
import winsound
from threading import *
 
root = Tk()
 
root.geometry("400x300")

def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    while alarm_playing:
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        if current_time == set_alarm_time:
            print("Time to Wake up")
            winsound.PlaySound("alarm_clock.wav", winsound.SND_FILENAME)

root.mainloop()