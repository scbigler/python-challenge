from audioop import avg
import os

import csv


csvpath = os.path.join("Resources", "budget_data.csv")
# print (csvpath)

month_counter = 0
net_total = 0
negative = 0
positive = 0
avg_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        month_counter = month_counter + 1
        
        amount = int(row[1])
        avg_list.append(int(row[1]))
       
        net_total = net_total + int(amount)
        # print(net_total)
        if amount < 0:
            if amount < negative:
                negative = amount
        if amount > 0:
            if amount > positive:
                positive = amount
                
print ("Highest Value "+ str(positive))
print("Lowest Value " + str(negative))
print("Number of months " + str(month_counter))
print("Net Total Amount " + str(net_total))
print("Average " + str(net_total/month_counter))
                
        