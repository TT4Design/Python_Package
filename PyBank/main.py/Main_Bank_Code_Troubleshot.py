#Insert File Location 
import os
import csv

#Define Variables
highest = 0
lowest = 10000000000
sum = 0
rowcount = 0

j = 0
average_month = 0

with open("../budget_data.csv") as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')

# No Header Line    
    next(readCSV, 0)

    for row in readCSV:
    
        if int(row[1])>= highest:
            highest = int(row[1])
            highestname = str(row[0])
            print(highestname)        
        else:
            if int(row[1]) <= lowest:
                lowest = int(row[1])
                lowestname = str(row[0])
            else:
                print(lowestname)

        # Total
        sum = int(sum) + int(row[1])

        # Total Months
        rowcount = rowcount +1
        
    # While Loop (Not Working) 
    # while j <= rowcount - 2:
    #     previous_value = current_value
    #     current_value = int(row[1])
    #     running_value = current_value + running_value
    # if j == j + 1: 

    # average_month = running_value/rowcount
    # print(average_month)

    # Print Final Analysis Report
    print(row)
    
    print('--------------------------------')
    print('Financial Analysis')
    print('--------------------------------')
    print('Total Months: '+ str(rowcount))
    print('Total: $'+ str(sum))
    # print('Average Change: $' + str(average_month))
    print('Greatest Increase in Profits: $' + str(highest)+ " on " + str(highestname))        
    print('Greatest Decrease in Profits: $' + str(lowest) + " on " + str(lowestname))        
            
    with open('financial_analysis.txt', 'w') as text:
        text.write('--------------------------------')  
        text.write('Financial Analysis')
        text.write('--------------------------------')  
        text.write('Total Months: '+ str(rowcount))
        text.write('Total: $'+ str(sum))
        text.write('Greatest Increase in Profits: $' + str(highest)+ " on " + str(highestname))
        text.write('Greatest Decrease in Profits: $' + str(lowest) + " on " + str(lowestname))
