import os
import csv

customer_file = "customers.csv"
customer_country = "customer_country.csv"

infile = open(customer_file, "r", newline="")
reader = csv.reader(infile)
field_names = next(reader)
outfile = open(customer_country, "w", newline="")
writer = csv.writer(outfile, delimiter=",")
firstname = field_names[1]
lastname = field_names[2]
country = field_names[4]
new_names = [firstname, lastname, country]
writer.writerow(new_names)

for row in reader:
    customer_firstname = row[1]
    customer_lastname = row[2]
    customer_country = row[4]
    new_row = [customer_firstname, customer_lastname, customer_country]

    writer.writerow(new_row)

infile.close
outfile.close
