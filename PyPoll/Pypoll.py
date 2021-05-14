# Import modules
import os
import csv

#declare variables
total_votes = 0
vote_percent = []
votes_per_candidate = []
candidate_vote_count = []
winner = ""

#read in csv
file = os.path.join("Resources","election_data.csv")
with open(file) as csvFile:

    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)
    for x in csvReader:
        
        total_votes += 1
        if str(x[2]) not in vote_percent:
            vote_percent.append(x[2])
            votes_per_candidate.append(0)
            candidate_vote_count.append(0)
        if str(x[2]) in vote_percent:
                candidate_vote_count[vote_percent.index(x[2])]  += 1 

for n in range (0, len(candidate_vote_count)):
    votes_per_candidate[n] = round((candidate_vote_count[n]/total_votes) * 100, 3)

winner = vote_percent[candidate_vote_count.index(max(candidate_vote_count))]
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for candidate in vote_percent:
    print(f"{candidate}: {votes_per_candidate[int(vote_percent.index(candidate))]:.3f}% ({str(candidate_vote_count[int(vote_percent.index(candidate))])})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

txtOutDir = os.path.join("Analysis","PyPollAnalysis.txt")

with open(txtOutDir, "w", newline="") as txtFile:
    
    txtFile.write(f"Election Results\n")
    txtFile.write(f"-------------------------\n")
    txtFile.write(f"Total Votes: {total_votes}\n")
    txtFile.write(f"-------------------------\n")
    for candidate in vote_percent:
        txtFile.write(f"{candidate}: {votes_per_candidate[int(vote_percent.index(candidate))]:.3f}% ({str(candidate_vote_count[int(vote_percent.index(candidate))])})")
    txtFile.write(f"-------------------------\n")
    txtFile.write(f"Winner: {winner}\n")
    txtFile.write(f"-------------------------")