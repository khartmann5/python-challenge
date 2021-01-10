# Import the os module
import os

# Module for reading CSV files
import csv

election_data = os.path.join('Resources','election_data.csv')

# Define variables
total_votes = 0
vote_percentages = 0
vote_candidate = []

candidates_dict = {}
vote_percentages = {}

# Read CSV file
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    csv_header = next(csvreader)

    # Read each row of data
    for row in csvreader:
        if row[2] in candidates_dict:
            candidates_dict[row[2]] += 1
        else:
            candidates_dict[row[2]] = 1

        # Total number of votes cast    
        total_votes = total_votes + 1

        # Determine overall winner
        winner = max(candidates_dict, key=candidates_dict.get)

        for key in candidates_dict.keys():
            vote_candidate.append(candidates_dict[key]/total_votes * 100)
            vote_candidate.append(candidates_dict[key])
            vote_percentages[key] = vote_candidate

# Print results
print("Election Results\n-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for key in vote_percentages:
    print(f"{key}: {vote_percentages[key][0]}% ({vote_percentages[key][1]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# write to text analysis file
# pypoll_election_results = os.path.join("pypoll_election_results.txt")
# with open(pypoll_election_results,"w") as outfile:
    
#     outfile.write("Election Results\n-------------------------\n")
#     outfile.write(f"Total Votes: {total_votes}\n")
#     outfile.write("-------------------------\n")
#     outfile.write(f"Winner: {winner}\n")
#     outfile.write("-------------------------")


