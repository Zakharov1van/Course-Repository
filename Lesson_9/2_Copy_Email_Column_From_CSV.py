import csv

with open("names.csv", "r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

    with open("emails.csv", "w", newline="") as csv_emails:
        email_writer = csv.DictWriter(csv_emails, fieldnames=["email"])
        email_writer.writeheader()

        for line in csv_reader:
            email_writer.writerow({"email": line["email"]})
