"""
Final project for Harvard's CS50P (Intro to Python Course)

Redistribution in source and binary forms, with or without modification, is not permitted.

RezVroom: The room reservaation system

Full Description at https://cs50.harvard.edu/python/2022/psets/8/seasons/

Author: Amr Ramadan
"""
from tkinter import messagebox
from tkinter import *
import re
from datetime import date
from datetime import datetime
import time
import pandas as pd
import os.path


def main():
    GUI()


def GUI():
    #setting tittle and background color
    root.title("RezVroom")
    root.config(bg="#856ff8")

    # creating label widgets
    tittle_label = Label(root, text="Welcome to RezVroom!", font=("Arial", 25), bg="red")
    name_label = Label(root, text="Please enter your name (first and last only. ex:'John Smith') ", font=("Arial", 10))
    room_label = Label(root, text="Please enter room number either 101 or 102 ", font=("Arial", 10))
    res_date_label = Label(root, text="Please enter a date in this format 'MM-DD-YYYY'", font=("Arial", 10))
    start_label = Label(root, text="Please enter starting time of the booking in 24 hr format (ex:13:00)",
                        font=("Arial", 10))
    end_label = Label(root, text="Please enter ending time of the booking in 24 hr format (ex:14:00)",
                      font=("Arial", 10))

    # creating input field widgets for the user to enter data and binding it to a function to validate
    name_entry = Entry(root, width=50)
    name_entry.bind("<Return>", lambda event: get_name(event, name_entry.get()))

    room_entry = Entry(root, width=50)
    room_entry.bind("<Return>", lambda event: get_room(event, room_entry.get()))

    res_date_entry = Entry(root, width=50)
    res_date_entry.bind("<Return>", lambda event: get_date(event, res_date_entry.get()))

    start_entry = Entry(root, width=50)
    start_entry.bind("<Return>", lambda event: get_start(event, start_entry.get()))

    end_entry = Entry(root, width=50)
    end_entry.bind("<Return>", lambda event: get_end(event, end_entry.get()))

    # creating a submit button and calling the reserve function to save the data
    submit = Button(root, text="Submit", font=("Arial", 25),
                    command=lambda: reserve(name_entry.get(), room_entry.get(), res_date_entry.get(), start_entry.get(),
                                            end_entry.get()))


    # putting everything on the window
    tittle_label.grid(row=0, column=3, padx=30, pady=30)
    name_label.grid(row=2, column=3)
    name_entry.grid(row=3, column=3, pady=10)
    room_label.grid(row=5, column=3)
    room_entry.grid(row=6, column=3, pady=10)
    res_date_label.grid(row=8, column=3)
    res_date_entry.grid(row=9, column=3, pady=10)
    start_label.grid(row=11, column=3)
    start_entry.grid(row=12, column=3, pady=10)
    end_label.grid(row=14, column=3)
    end_entry.grid(row=15, column=3, pady=10)
    submit.grid(row=17, column=3, pady=10)

def get_name(event, name):
    #validating user input
    if re.search("^[a-z]+ [a-z]+$", name, re.IGNORECASE):
        return f"{str.title(name)}"
    else:
        messagebox.showerror("Name Error", "This is not a valid name!")
        return f"This is not a valid name!"


def get_room(event,room):
    try:
        #checking if room can be converted to int, if not then raise statement will be called
        int(room)
        #checking if number is 101 or 102
        if re.search("^10[1-2]$", room):
            return f"{room}"
        else:
            messagebox.showerror("Room Error", "This is not a valid room number!")
            return f"This is not a valid room number!"

    except ValueError:
        messagebox.showerror("Room Error", "That's not a number!")
        return f"That's not a number!"

def get_date(event, res_date):
    #validate date to be MM-DD-YYYY
    if re.search("^(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])-2[0-9][0-9][0-9]$", res_date):
        #seperating the input
        month, day, year = res_date.split("-")
        #converting the sperated input to an int object
        date_object = date(int(year), int(month), int(day))
        #getting today's date and subtracting it from the entered date
        diff_days = date.today() - date_object
        if diff_days.days > 0:
            messagebox.showerror("Date Error", "That's an old date!")
            return f"That's an old date!"
        else:
            return f"{res_date}"
    else:
        messagebox.showerror("Date Error", "Invalid date format!")
        return f"Invalid date format!"

def get_start(event, start):
    #validating start time input
    if duration := re.search("^([1-9]|1[0-9]|2[0-3]):([0-5][0-9])$", start):
        return start
    else:
        messagebox.showerror("Time Error", "Please enter a valid time format!")
        return f"Please enter a valid time format!"

def get_end(event, end):
    #validating end time input
    if duration := re.search("^([1-9]|1[0-9]|2[0-3]):([0-5][0-9])$", end):
        return end
    else:
        messagebox.showerror("Time Error", "Please enter a valid time format!")
        return f"Please enter a valid time format!"

def reserve(name, room, res_date, start, end):
    #name of the csv file
    file_name = room + ".csv"

    #checking if the csv file already exits
    if os.path.exists(file_name):
        #check if the room is already booked
        reading = pd.read_csv(file_name)
        #getting the start and end times columns that are already in the csv file and converting them to datetime.time object instead of str
        start_time = pd.to_datetime(reading["Start Time"]).dt.time
        end_time = pd.to_datetime(reading["End Time"]).dt.time
        #converting start and end to time object
        start = datetime.strptime(start, '%H:%M').time()
        end = datetime.strptime(end, '%H:%M').time()
        #getting the Date column
        dates = reading["Date"]
        #looping over the start and end time columns
        for dayy, beginging, ending in zip(dates, start_time, end_time):
            #checking if the given start or end time by user are confilcting with already exiisting time
            if dayy == res_date and (beginging <= start <= ending or beginging <= end <= ending):
                messagebox.showerror("Time Conflict Error", f"There is already a booking that exits from {beginging} to {ending}, please choose another time")
                return f"There is already a booking that exists from {beginging} to {ending}, please choose another time"
        #there is no confilct so will add the resvervation to the csv file
        writer = pd.DataFrame([[name, res_date, start, end]])
        writer.to_csv(file_name, mode="a", index=False, header=False)
        response = messagebox.askyesno("Success", f"Your booking is confirmed for {res_date} from {start} to {end}. \\n Do you want to make another booking?")
        if response == 0:
            root.destroy()
        return f"Your booking is confirmed for {res_date} from {start} to {end}."

    #create the csv file with header and add the entry to it
    else:
        writer = pd.DataFrame([[name, res_date, start, end]],
                              columns=["Name", "Date", "Start Time", "End Time"])
        writer.to_csv(file_name, mode= "a", index=False)
        response = messagebox.askyesno("Success", f"Your booking is confirmed for {res_date} from {start} to {end}. \\n Do you want to make another booking?")
        if response == 0:
            root.destroy()
        return f"Your booking is confirmed for {res_date} from {start} to {end}."

if __name__ == "__main__":
    root = Tk()
    main()
    root.mainloop()




