### Blu Training Log V2 ###

import csv
import datetime

# Initialize filename 
filename = input("Enter the filename to store exercise data: ")

# Get the current date and time
current_date = datetime.date.today()
current_time = datetime.datetime.now()

# Initialize variables to store exercise data
push_ups = int(input("Enter the number of Push Ups: "))
pull_ups = int(input("Enter the number of Pull Ups: "))
sit_ups = int(input("Enter the number of Sit Ups: "))
burpees = int(input("Enter the number of Burpees: "))
exercise_time = float(input("Enter the exercise time (in minutes): "))
run_distance = float(input("Enter the run distance (in miles): "))
run_time = float(input("Enter the run time (in minutes): "))

# Calculate total time 
total_time = run_time + exercise_time

# Open CSV file in append mode
with open(filename, 'a', newline='') as csvfile:

    # Create CSV writer
    writer = csv.writer(csvfile)

    # Write header row if file is empty
    if csvfile.tell() == 0:
        writer.writerow(["Date", "Push Ups", "Pull Ups", "Sit Ups", 
                        "Burpees", "Exercise Time", "Run Distance", "Run Time", "Total Time"])
 
    # Write exercise data as row    
    writer.writerow([current_date, push_ups, pull_ups, sit_ups, 
                    burpees, exercise_time, run_distance, run_time, total_time]) 

print(f"Exercise data saved to {filename} as CSV.")
