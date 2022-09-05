import csv

with open('riesling.csv', 'a')as file1:
    writer = csv.DictWriter(file1)
    with open('riesling1.csv', 'r')as file2:
        reader = csv.DictReader(file2)
        for i in reader:
            writer.writerow(i)