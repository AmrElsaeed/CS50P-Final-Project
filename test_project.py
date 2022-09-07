from project import *


def test_get_name():
    assert get_name("event", "john smith") == "John Smith"
    assert get_name("event", "amr R") == "Amr R"
    assert get_name("event", "cat") == "This is not a valid name!"

def test_get_room():
    assert get_room("event", "101") == "101"
    assert get_room("event", "102") == "102"
    assert get_room("event", "500") == "This is not a valid room number!"
    assert get_room("event", "cat") == "That's not a number!"

def test_get_date():
    assert get_date("event", "09-09-2022") == "09-09-2022"
    assert get_date("event", "09/09/2022") == "Invalid date format!"
    assert get_date("event", "07-07-2022") == "That's an old date!"

def test_get_start():
    assert get_start("event", "13:00") == "13:00"
    assert get_start("event", "11 AM") == "Please enter a valid time format!"

def test_get_end():
    assert get_end("event", "15:00") == "15:00"
    assert get_end("event", "3 PM") == "Please enter a valid time format!"

def test_reserve():
    assert reserve("John Smith", "101", "10-10-2022", "13:00", "14:00") == "Your booking is confirmed for 10-10-2022 from 13:00 to 14:00."
    assert reserve("John Smith", "101", "10-10-2022", "13:30", "14:30") == "There is already a booking that exists from 13:00:00 to 14:00:00, please choose another time"

