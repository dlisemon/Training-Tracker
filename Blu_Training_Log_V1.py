# Initialize a filename for data storage
filename = input("Enter the filename to store exercise data: ")

# Initialize variables to store exercise data
push_ups = int(input("Enter the number of Push Ups: "))
pull_ups = int(input("Enter the number of Pull Ups: "))
sit_ups = int(input("Enter the number of Sit Ups: "))
burpees = int(input("Enter the number of Burpees: "))
run_distance = float(input("Enter the run distance (in miles): "))
run_time = float(input("Enter the run time (in minutes): "))

# Calculate total exercise time
total_time = run_time

# Open the file in append mode to update or create it
with open(filename, 'a') as file:
    # Write exercise data to the file
    file.write(f"Push Ups: {push_ups}\n")
    file.write(f"Pull Ups: {pull_ups}\n")
    file.write(f"Sit Ups: {sit_ups}\n")
    file.write(f"Burpees: {burpees}\n")
    file.write(f"Run Distance: {run_distance} miles\n")
    file.write(f"Run Time: {run_time} minutes\n")
    file.write(f"Total Exercise Time: {total_time} minutes\n")
    file.write("\n")  # Add a separator for each entry

# Display a confirmation message
print(f"Exercise data has been saved to {filename}.")
