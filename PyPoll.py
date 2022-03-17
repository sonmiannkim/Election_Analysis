# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
first_row = ''
candidate_options = []
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    try:
        file_reader = csv.reader(election_data)        

        # Read the header row.
        headers = next(file_reader)
        print(headers)

        # Print each row in the CSV file.
        
        for row in file_reader:
            #read first row with data
            if first_row == '':
                first_row = row

            candidate_name = row[2]
            if candidate_name != '' and candidate_name not in candidate_options:
                candidate_options.append(candidate_name)
                candidate_votes[candidate_name] = 0               
                
            #Add to the total vote counts
            candidate_votes[candidate_name] += 1
            total_votes += 1
            last_row = row
        
    except OSError:
        file_reader.seek(0)

#print last row
#print(f"First line read : {first_row}")
#print(f"Last line read : {last_row}")
print("=============Practice loops====================\n")
#print totla votes
print(f"Total Votes : {total_votes}")
print(f"Candidates : {candidate_options}")
print(f"Each Candidates votes count: {candidate_votes}")
for candidate_name in candidate_votes:
    vote_percentage = candidate_votes[candidate_name] / total_votes * 100
    print(f"{candidate_name} Recieved of : {vote_percentage:.2f}% from the total vote!\n")

winning_candidate = ""
winning_count = 0
winning_percentage = 0

print("===============Summary Recorded==================\n")
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes/total_votes) * 100

    #Last count is the winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
    #Print each candidate summary
    print(f"{candidate_name} : {vote_percentage:.1f} ({votes:,})\n")

# Winning summary
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
