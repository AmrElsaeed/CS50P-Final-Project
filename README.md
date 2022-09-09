# RezVroom

### **Video Demo:**  <[URL HERE](https://www.youtube.com/watch?v=k82ndO7uVXY)>
---
### **Description:**
RezVroom is a room reservation system that can be used to book conference/seminar/meeting rooms in a building.
The system validates user input before making any booking, the input includes entering a valid name, valid room number,
valid format of date and time.
If all the inputs are according to standards then a booking request shall be made; if the room is available then the booking is confirmed,
if it's already booked, then the user is notified that there is a booking that already exists and another time should be chosen.

The code is written using python, and the GUI part is implemented using tkinter the standard GUI library for python.

Below is the docstring explanation of each function in the code:

#### **get_name(event, name):**
validate input name that it contains two words separated by one space and each word contains alphabetical characters only.

:param event: Return key

:type event: tkinter event handler

:param name: input name

:type name: str

:return: name/error message

:rtype: str

#### **get_room(event, room):**
validate room number that is either 101 or 102

:param event: Return key

:type event: tkinter event handler

:param room: room number

:type room: str

:raise ValueError: If room is not an int

:return: room/error message

:rtype: str

#### **get_date(event, res_date):**
validate date format to be MM-DD-YYYY and ensure that no old dates are entered

:param event: Return key

:type event: tkinter event handler

:param res_date: booking date

:type res_date: str

:return: date/error message

:rtype: str

#### **get_start(event, start):**
Validate start time format of the booking to be HH:MM

:param event: Return key

:type event: tkinter event handler

:param start: starting time of the booking

:type start: str

:return: start/error message

:rtype: str

#### **get_end(event, end):**
validate end time format of the booking to be HH:MM

:param event: Return key

:type event: tkinter event handler

:param end: ending time of the booking

:type end: str

:return: end/error message

:rtype: str

#### **reserve(name, room, res_date, start, end):**
saves the booking time to csv file if there are no conflicts.

:param name: validated input name for the booking

:type name: str

:param room: validated room number for the booking

:type room: int

:param res_date: validated input date of the booking

:type res_date: str

:param start: validated starting time of the booking

:type start: str

:param end: validated ending time of the booking

:type end: str

:return: success/error message

:rtype: str






