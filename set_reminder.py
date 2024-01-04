from win10toast import ToastNotifier
import threading
import time

def set_reminder(minutes):
    toaster = ToastNotifier()

    # Calculate the time for the reminder (current time + specified minutes)
    reminder_time = time.time() + (minutes * 60)

    # Wait until the reminder time is reached
    while time.time() < reminder_time:
        time.sleep(1)

    # Display a toast notification for the reminder
    toaster.show_toast("Reminder", "Time`s up!", duration=10)