import os
import csv

sales = "sales.csv"
sales_report = "salesreport.csv"

infile = open(sales, "r", newline="")
reader = csv.reader(infile)
field_names = next(reader)
outfile = open(sales_report, "w", newline="")
writer = csv.writer(outfile, delimiter=",")
line_one = ["Customer | Total"]
writer.writerow(line_one)

new_total = 0
total = 0
prev_id = -1

for row in reader:

    cust_id = int(row[0])

    if prev_id == -1:
        prev_id = cust_id

    subtotal = float(row[3])
    tax = float(row[4])
    freight = float(row[5])

    if cust_id == prev_id:
        total = subtotal + tax + freight
        new_total += total

    else:

        # write the previous results
        sales_info = [format(cust_id - 1, "<11") + format(float(new_total), "<8.7")]
        writer.writerow(sales_info)

        new_total = 0
        total = 0
        total = subtotal + tax + freight
        new_total += total

        # reinitialize for the new customer
        prev_id = cust_id


# write the final results
sales_info = [format(cust_id, "<11") + format(float(new_total), "<8.7")]
writer.writerow(sales_info)

infile.close
outfile.close
