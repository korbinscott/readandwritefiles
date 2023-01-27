import os
import csv

employee_info = "EmployeePay.csv"

infile = open(employee_info, "r", encoding="utf-8-sig")
reader = csv.reader(infile)
fields = next(reader)
print(
    format(fields[0], "2"),
    format(fields[1], "12"),
    format(fields[2], "15"),
    format(fields[3], "7"),
    format(fields[4], "5"),
)

for row in reader:
    print(
        format(row[0], "2"),
        format(row[1], "12"),
        format(row[2], "15"),
        format(int(row[3]), "<7"),
        format(row[4], "5"),
    )

infile.close
