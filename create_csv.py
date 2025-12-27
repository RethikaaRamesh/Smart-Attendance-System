import csv
import os

filename = "Attendance.csv"

# Check if file already exists
if not os.path.isfile(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Time", "Date"])
    print("Attendance.csv created successfully")
else:
    print("Attendance.csv already exists")
