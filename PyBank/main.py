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
                
HV = "Highest Value " + str(positive)
LV = "Lowest Value " + str(negative)
months = "Number of months " + str(month_counter)
NTA = "Net Total Amount " + str(net_total)
average = "Average " + str(net_total/month_counter)
FA = "Financial Analysis"
seperator = "-------------------"

print(FA)
print(seperator)
print (NTA)
print(months)
print(average)
print(HV)
print(LV)



                
out_list = [[FA], [seperator], [NTA], [months], [average], [HV], [LV]]     

# Send results to output csv file
outputfile = os.path.join("Analysis/budget_analysis.csv")

with open(outputfile, "w") as csvoutfile:
     csvwriter = csv.writer(csvoutfile, delimiter=',')
     for i in range(len(out_list)):
        csvwriter.writerow(out_list[i])