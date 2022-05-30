import psutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time
from datetime import datetime, date
import python_weather
import asyncio

ram_limit_number = 44
storage_limit_number = 40

window = tk.Tk()
window.geometry("600x500")
window.title("Programm")

RAM_USED = psutil.virtual_memory()[2]
RAM_TOTAL = psutil.virtual_memory()[0] / (1024.0 ** 3)
RAM_TOTAL = round(RAM_TOTAL, 1)
RAM_USED_GB = psutil.virtual_memory()[3] / (1024.0 ** 3)
RAM_USED_GB = round(RAM_USED_GB, 1)

RAM_overflow = tk.Label(text=" ", fg='red', font=("Helvetica", 12))

def RAM_USEDD():
	RAM_USED = psutil.virtual_memory()[2]
	RAM_TOTAL = psutil.virtual_memory()[0] / (1024.0 ** 3)
	RAM_TOTAL = round(RAM_TOTAL, 1)
	RAM_USED_GB = psutil.virtual_memory()[3] / (1024.0 ** 3)
	RAM_USED_GB = round(RAM_USED_GB, 1)
	cpu_usage_lbl.configure(text=f'{RAM_USED}%   {RAM_USED_GB}/{RAM_TOTAL}Gb')
	if RAM_USED >= ram_limit_number:
		RAM_overflow.configure(text="RAM limit is exceeded!")
	else:
		RAM_overflow.configure(text=" ")
	cpu_usage_lbl.after(1000, RAM_USEDD)

lbl1 = tk.Label(
    text = "RAM usage", font=("Helvetica", 14)
    )
lbl1.pack()

cpu_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
cpu_usage_lbl = tk.Label(master=cpu_frame, text=f'{RAM_USED}%   {RAM_USED_GB}/{RAM_TOTAL}Gb', width=30, height=2, font=("Helvetica", 12))
cpu_usage_lbl.pack(side=tk.LEFT)
cpu_frame.pack()
RAM_USEDD()

RAM_overflow.pack()

blank1 = tk.Label(text=" ")
blank1.pack()

HDD_TOTAL = psutil.disk_usage('/')[0] / (1024.0 ** 3)
HDD_TOTAL = round(HDD_TOTAL, 1)
HDD_USED = psutil.disk_usage('/')[1] / (1024.0 ** 3)
HDD_USED = round(HDD_USED, 1)
HDD_PERCENT = psutil.disk_usage('/')[3]

HDD_overload = tk.Label(text=" ", fg='red', font=("Helvetica", 12))

def HDD_USEDD():
	HDD_TOTAL = psutil.disk_usage('/')[0] / (1024.0 ** 3)
	HDD_TOTAL = round(HDD_TOTAL, 1)
	HDD_USED = psutil.disk_usage('/')[1] / (1024.0 ** 3)
	HDD_USED = round(HDD_USED, 1)
	HDD_PERCENT = psutil.disk_usage('/')[3]
	str_usage_lbl.configure(text=f'{HDD_PERCENT}%   {HDD_USED}/{HDD_TOTAL} Gb')
	if HDD_PERCENT >= storage_limit_number:
		HDD_overload.configure(text="Storage limit is exceeded!")
	else:
		HDD_overload.configure(text=" ")
	str_usage_lbl.after(1000, HDD_USEDD)

lbl2 = tk.Label(
    text = "Storage usage", font=("Helvetica", 14)
    )
lbl2.pack()

str_frame = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
str_usage_lbl = tk.Label(master=str_frame, text=f'{HDD_PERCENT}%   {HDD_USED}/{HDD_TOTAL}Gb', width=30, height=2, font=("Helvetica", 12))
str_usage_lbl.pack(side=tk.LEFT)
str_frame.pack()
HDD_USEDD()

HDD_overload.pack()

def save_ram():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	today = date.today()
	current_date = today.strftime("%d/%m/%Y")
	RAM_USED = psutil.virtual_memory()[2]
	RAM_USED_str = str(RAM_USED)
	RAM_USED_GB = psutil.virtual_memory()[3] / (1024.0 ** 3)
	RAM_USED_GB = round(RAM_USED_GB, 1)
	with open('RAM_log.txt', 'a') as f:
		f.write(f"[{current_date}] {current_time} : {RAM_USED_str}%  {RAM_USED_GB} Gb\n")

def save_str():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	today = date.today()
	current_date = today.strftime("%d/%m/%Y")
	STR_USED = psutil.virtual_memory()[2]
	STR_USED_str = str(STR_USED)
	HDD_USED = psutil.disk_usage('/')[1] / (1024.0 ** 3)
	HDD_USED = round(HDD_USED, 1)
	with open('STORAGE_log.txt', 'a') as f:
		f.write(f"[{current_date}] {current_time} : {STR_USED_str}%  {HDD_USED} Gb\n")


saveRAM_btn = tk.Button(master=cpu_frame, text="save log", width=15, height=2, command = save_ram)
saveRAM_btn.pack(side=tk.RIGHT)
saveSTR_btn = tk.Button(master=str_frame, text="save log", width=15, height=2, command = save_str)
saveSTR_btn.pack(side=tk.RIGHT)

blank2 = tk.Label(text=" ")
blank2.pack()

def save_ram_limit():
	global ram_limit_number
	ram_limit_number1 = options1_entry.get()
	ram_limit_number = int(ram_limit_number1)

options_frame = tk.Frame(master=window)
options_frame.pack()

options1_label = tk.Label(master=options_frame, text="RAM message limit", font=("Helvetica", 12))
options1_label.pack(side=tk.LEFT)
options1_entry = tk.Entry(master=options_frame)
options1_entry.pack(side=tk.LEFT)
options1_btn = tk.Button(master=options_frame, text="  Save  ", command=save_ram_limit)
options1_btn.pack(side=tk.RIGHT)

blank3 = tk.Label(text=" ")
blank3.pack()

def save_storage_limit():
	global storage_limit_number
	storage_limit_number1 = options2_entry.get()
	storage_limit_number = int(storage_limit_number1)

options2_frame = tk.Frame(master=window)
options2_frame.pack()

options2_label = tk.Label(master=options2_frame, text="Storage message limit", font=("Helvetica", 12))
options2_label.pack(side=tk.LEFT)
options2_entry = tk.Entry(master=options2_frame)
options2_entry.pack(side=tk.LEFT)
options2_btn = tk.Button(master=options2_frame, text="  Save  ", command=save_storage_limit)
options2_btn.pack(side=tk.RIGHT)

async def getweather():

    client = python_weather.Client(format=python_weather.METRIC)

    weather = await client.find("Tallinn")

    global current_temp

    current_temp = weather.current.temperature

    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())

blank4 = tk.Label(text=" ")
blank4.pack()

City_lbl = tk.Label(text="Tallinn", font=("Helvetica", 12))
City_lbl.pack()

Temp_lbl = tk.Label(text=f"{current_temp}°", font=("Helvetica", 14, "bold"))
Temp_lbl.pack()

def run():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	today = date.today()
	current_date = today.strftime("%d/%m/%Y")
	with open('Programm_Log.txt', 'a') as f:
		f.write(f"[{current_date}] {current_time} : Script initiated\n")

run()
window.mainloop()