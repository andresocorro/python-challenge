# Import necessary modules to run code
import os
import csv

# Open File
elections_csv = os.path.join("Resources","election_data.csv")

with open(elections_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)

# Create lists that will be used to collect voters and their vote

    voters = []
    candidates_with_votes = []
    candidates = []

# Add the content to the lists by reading through file
    for row in csv_reader:
        voters.append(row[0])
        candidates_with_votes.append(row[2])

# Count the total number of votes
    total_votes = len(voters)
    # print(total_votes)

# Look through vote choice to see how many candidates there were
    [candidates.append(i) for i in candidates_with_votes if i not in candidates] 
    # print(candidates)
    # print (candidates[0])

    # Tally the votes per candidate and their percentage
    candidate0_votes = candidates_with_votes.count(candidates[0])
    candidate0_percentage = format((float(candidate0_votes) / float(total_votes) *100), ".3f")
    
    candidate1_votes = candidates_with_votes.count(candidates[1])
    candidate1_percentage = format((float(candidate1_votes) / float(total_votes) *100), ".3f")

    candidate2_votes = candidates_with_votes.count(candidates[2])
    candidate2_percentage = format((float(candidate2_votes) / float(total_votes) *100), ".3f")

    candidate3_votes = candidates_with_votes.count(candidates[3])
    candidate3_percentage = format((float(candidate3_votes) / float(total_votes) *100), ".3f")    

    # Create list with the total votes and pair with candidates to find candidate with the most votes

    vote_count = (candidate0_votes, candidate1_votes, candidate2_votes, candidate3_votes)
    
    votes = list(vote_count)
    winner = []
    for election, Results in enumerate(votes):
        if Results == max(votes):
            winner.append(candidates[election])
    
    def convert(string_value, seperator=' '):
        return seperator.join(string_value)
    winner = convert(winner)  
    print(winner) 

    #Print output to terminal
    print()
    print(f"Election Results")
    print("-"*30)
    print(f"Total Votes: {total_votes}")
    print("-"*30)
    print(f"{candidates[0]}: {candidate0_percentage}% ({candidate0_votes})  ")
    print(f"{candidates[1]}: {candidate1_percentage}% ({candidate1_votes}) ")
    print(f"{candidates[2]}: {candidate2_percentage}% ({candidate2_votes}) ")
    print(f"{candidates[3]}: {candidate3_percentage}% ({candidate3_votes}) ")
    print("-"*30)
    print(f"Winner: {winner}")
    print("-"*30)


    # print output to text file

    elections_analysis_text = os.path.join("Analysis", "analysis_results.txt")

    nl = "\n"
    output_file = open(elections_analysis_text, "w")

    output_file.write(f"Election Results {nl}")
    output_file.write(f" ---------------------------------------- {nl}")
    output_file.write(f"Total Votes: {total_votes} {nl}")
    output_file.write(f" ---------------------------------------- {nl}")
    output_file.write(f" {candidates[0]}: {candidate0_percentage}% ({candidate0_votes}) {nl}")
    output_file.write(f" {candidates[1]}: {candidate1_percentage}% ({candidate1_votes}) {nl}")
    output_file.write(f" {candidates[2]}: {candidate2_percentage}% ({candidate2_votes}) {nl}")
    output_file.write(f" {candidates[3]}: {candidate3_percentage}% ({candidate3_votes}) {nl}")
    output_file.write(f" ---------------------------------------- {nl}")
    output_file.write(f" Winner: {winner} {nl}")
    output_file.write(f" ---------------------------------------- {nl}")
    output_file.close()
