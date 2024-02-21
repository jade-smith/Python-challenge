import csv

# Path to the CSV file
file_path = "/Users/jadesmith/Desktop/ptda-dec-2023/Assignments/Module-3/03-Python/PyPoll/resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""

# Read the CSV file and perform analysis
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip the header row
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        
        # Track the number of votes each candidate receives
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Find the winner based on popular vote
winner = max(candidates, key=candidates.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export .txt
with open("election_results.txt", "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        txt_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")
