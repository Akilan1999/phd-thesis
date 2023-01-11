import csv
import dateutil.parser as parser

with open('PhD_Planner.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
        ## parse start date and
        text = "starts " + parser.parse(row['Start date']).strftime("%Y-%m-%d") + " and ends " + parser.parse(row['End date']).strftime("%Y-%m-%d")
        print(text) 
