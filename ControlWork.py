import os
import ctypes
from datetime import datetime, timedelta
import time

def hide_console():
    """Hide console (only for Windows)"""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def show_console():
    """Show console"""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

def log_activity(log_file, activity):
    """Logging ou actions in file"""
    with open(log_file, 'a') as file:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{current_time} - {activity}\n")

def main():
    try:
        # get work time programm and number of notifications
        hours = float(input("Enter how much time the program needs to run: "))
        interval_minutes = int(input("Enter the notification interval (in minutes): "))

        # converting work time in seconds
        total_runtime = timedelta(hours=hours)
        total_runtime_seconds = total_runtime.total_seconds()

        # converting interval in seconds
        interval_seconds = interval_minutes * 60 # В секундах

        # get the working time
        start_time = datetime.now()
        end_time = start_time + total_runtime

        # Path to your log file(default path where your program is located)
        log_file = 'activity_log.txt'

        print("Programm is started. if you wanna stop just enter 'stop' in console")

        elapsed_time = 0
        while elapsed_time < total_runtime_seconds: # compare with total_runtime_seconds
            # hide the console
            hide_console()

            # wait given interval
            time.sleep(interval_seconds) 

            show_console() 
            os.system("cls") # clear console

            # logging activites
            activity = input(f"Enter what you did in {interval_minutes} minutes (if you want stop enter 'stop'): ")
            if activity.lower() == "stop":
                print("Programm was stoped")
                break 
            log_activity(log_file, activity)

            # update time
            elapsed_time = (datetime.now() - start_time).total_seconds()

    except Exception as e:
        print(f"Something wrongа: {e}")

if __name__ == "__main__": 
    main()