"""This is a calendar, the user should be able to choose to:
- View the calendar
- Add an event to the calendar
- - Update an existing event
Delent an existing event"""
from time import sleep, strftime
name = "James"
calendar = {
}
def welcome(): #displays current date and time and welcomes the user
  print "Welcome, %s!" % name
  print "Calendar is opening..."
  sleep(1)
  print strftime("%A %B %d, %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print
  print "What would you like to do?"
def start_calendar():
  welcome()
  start = True
  while start: #this will allow the calendar to continue running as long as start = True
    user_choice = raw_input("A to add, U to update, V to View, D to Delete, X to Exit: ")
    user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print("Calendar is empty.")
        print
      else:
        print calendar
        print
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print("%s updated.") % date
      print
      print calendar
      print
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))): #checks if date is invalid
        print("Invalid date entered.")
        try_again = raw_input("Try again? Y/N ")
        try_again.upper()
        if try_again == "Y":
          continue #continue keyword will start the loop from beginning again
        else:
          start = False #this would exit the program
      else: #this runs if date is valid
        calendar[date] = event#changes event
        print("Event successfully added to %s") % date
        print
        print calendar
        print
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("The calendar is empty.")
        print
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print("%s successfully deleted.") % event
            print
            print calendar
            print
            break
          else:
            print("Incorrect event was specified.")
            print
    elif user_choice == "X": #this will exit the program
      print("Exiting...")
      start = False
    else:
      print("Invalid command entered.")
      start = False
start_calendar()#need this for the function to run