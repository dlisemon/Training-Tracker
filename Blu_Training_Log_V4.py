### Blu Training Log V4 ###


import csv
import datetime


# Initialize filename 
filename = input("Enter the filename to store exercise data: ")

# Initialize variables to store exercise data
entry_number = 1
previous_entry = None

# Get the current date and time
current_date = datetime.date.today()
current_time = datetime.datetime.now()


# Fucntion to print the previous entry
def print_previous_entry():
    if previous_entry is not None:
        print("Previous entry:")
        print(f"Entry number: {previous_entry['entry_number']}")
        print(f"Date: {previous_entry['date']}")
        print(f"Push Ups: {previous_entry['push_ups']}")
        print(f"Pull Ups: {previous_entry['pull_ups']}")
        print(f"Sit Ups: {previous_entry['sit_ups']}")
        print(f"Burpees: {previous_entry['burpees']}")
        print(f"Exercise Time: {previous_entry['exercise_time']}")
        print(f"Run Distance: {previous_entry['run_distance']}")
        print(f"Run Time: {previous_entry['run_time']}")
        print(f"Difficulty Rating: {previous_entry['difficulty_rating']}")


# Function to print the current entry number
def print_current_entry_number():
    print(f"Current entry number: {entry_number}")


# Open CSV file in append mode
with open(filename, 'a', newline='') as csvfile:
    
    # Create CSV writer
    writer = csv.writer(csvfile)
    
    # Write header row if file is empty
    if csvfile.tell() == 0:
        writer.writerow(["Entry Number", "Date", "Push Ups", "Pull Ups", "Sit Ups", 
                        "Burpees", "Run Distance", "Run Time", "Difficulty Rating"])
        
    while True:
        # Print the previous entry
        print_previous_entry()

        # Print the current entry number
        print_current_entry_number()

        # Get the exercise data for the current entry
        push_ups = int(input("Enter the number of Push Ups: "))
        pull_ups = int(input("Enter the number of Pull Ups: "))
        sit_ups = int(input("Enter the number of Sit Ups: "))
        burpees = int(input("Enter the number of Burpees: "))
        exercise_time = float(input("Enter the exercise time (in minutes): "))
        run_distance = float(input("Enter the run distance (in km): "))
        run_time = int(input("Enter the run time (in minutes): "))
        difficulty_rating = int(input("Enter a difficulty rating (1-10): "))

        # Calculate total time 
        total_time = run_time + exercise_time

        # Write the exercise data as a row
        writer.writerow([entry_number, current_date, push_ups, pull_ups, sit_ups, 
                         burpees, exercise_time, run_distance, run_time, difficulty_rating])

        # Update the previous entry
        previous_entry = {
            "entry_number": entry_number,
            "date": current_date,
            "push_ups": push_ups,
            "pull_ups": pull_ups,
            "sit_ups": sit_ups,
            "burpees": burpees,
            "run_distance": run_distance,
            "run_time": run_time,
            "difficulty_rating": difficulty_rating
        }

        # Increment the entry number
        entry_number += 1

        # Ask the user if they want to enter another entry
        again = input("Enter another entry? (y/n): ")
        if again != "y":
            break

print(f"Exercise data saved to {filename} as CSV.")
