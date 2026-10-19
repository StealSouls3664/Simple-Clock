import tkinter as tk
from datetime import datetime
import time

def update_clock():
    now = datetime.now()
    time_12hr = now.strftime("%I:%M:%S.%f")[:-3]
    am_pm = now.strftime("%p")
    current_time = f"{time_12hr} {am_pm}"
    clock_label.config(text=current_time)
    clock_label.after(100, update_clock)

root = tk.Tk()
root.title("Clock")

try:
    clock_label = tk.Label(
        root,
        font=("Fleur De Leah", 36, "bold"),
        bg="#667980",
        fg="gold",
        padx=20,
        pady=20
    )
except:
    clock_label = tk.Label(
        root,
        font=("Script", 36, "bold"),
        bg="black",
        fg="gold",
        padx=20,
        pady=20
    )

print("If you see this message, please make sure the file type is .pyw and you are double clicking it.")
time.sleep(1.5)

clock_label.pack()

update_clock()
root.mainloop()
