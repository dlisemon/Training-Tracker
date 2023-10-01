### Blu Training Log V1 ###


import csv


# Initialize filename 
filename = input("Enter the filename to store exercise data: ")

# Initialize variables to store exercise data
date = input("Enter the date of the workout (e.g., YYYY-MM-DD): ")
push_ups = int(input("Enter the number of Push Ups: "))
pull_ups = int(input("Enter the number of Pull Ups: "))  
sit_ups = int(input("Enter the number of Sit Ups: "))
burpees = int(input("Enter the number of Burpees: "))
run_distance = float(input("Enter the run distance (in miles): "))
run_time = float(input("Enter the run time (in minutes): "))

# Calculate total time 
total_time = run_time

# Open CSV file in append mode
with open(filename, 'a', newline='') as csvfile:
    
    # Create CSV writer
    writer = csv.writer(csvfile)
    
    # Write header row if file is empty
    if csvfile.tell() == 0:
        writer.writerow(["Date", "Push Ups", "Pull Ups", "Sit Ups", 
                        "Burpees", "Run Distance", "Run Time", "Total Time"])
        
    # Write exercise data as row    
    writer.writerow([date, push_ups, pull_ups, sit_ups, 
                     burpees, run_distance, run_time, total_time]) 
    
print(f"Exercise data saved to {filename} as CSV.")
