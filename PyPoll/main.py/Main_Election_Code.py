import os
import csv

Election_Win = os.path.join("..", "PyPoll", "../election_data.csv")

#Define Variables
count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#Open the csv file

with open("../election_data.csv") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #Eliminate Header
    csv_header = next(csvreader)
    
    for row in csvreader:
        #Count the Total Number of Votes
        count = count +1

        #Candidates names to candidatelist
        candidatelist.append(row[2])

    #Created a set to identify unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)

        #Total number of votes/candidate
        y = candidatelist.count(x)
        vote_count.append(y)

        #Percentage of Total Votes/candidate
        z = (y/count)*100
        vote_percent.append(z)
        
        winning_vote_count = max(vote_count)
        winner = unique_candidate[vote_count.index(winning_vote_count)]


print("------------------------------")
print("Election Results")
print("------------------------------")
print("Total Votes :" + str(count))
print("------------------------------")

for i in range(len(unique_candidate)):
    print(unique_candidate[i] + "i" + str(vote_percent[i] + str(vote_count[i]+ "i")))
print("------------------------------")
print("The winner is: " + winner)
print("------------------------------")

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("--------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("--------------------------\n")   
    for i in range(len(set(unique_candidate))):
            print(unique_candidate[i] + "i" + str(vote_percent[i] + str(vote_count[i]+ "i")
    text.write("--------------------------\n") 
    text.write("The winner is: " + winner + "\n")
    text.write("--------------------------\n")                