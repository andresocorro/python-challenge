# Import necessary modules to run code
import os
import csv

elections_csv = os.path.join("Resources","election_data.csv")

with open(elections_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    csv_header = next(csv_reader)

    voters = []
    candidates_with_votes = []
    candidates = []
    for row in csv_reader:
        voters.append(row[0])
        candidates_with_votes.append(row[2])

    total_votes = len(voters)
    # print(total_votes)

    [candidates.append(i) for i in candidates_with_votes if i not in candidates] 
    # print(candidates)
    # print (candidates[0])

      
    candidate0_votes = candidates_with_votes.count(candidates[0])
    candidate0_percentage = format((float(candidate0_votes) / float(total_votes) *100), ".3f")
    

    candidate1_votes = candidates_with_votes.count(candidates[1])
    candidate1_percentage = format((float(candidate1_votes) / float(total_votes) *100), ".3f")

    candidate2_votes = candidates_with_votes.count(candidates[2])
    candidate2_percentage = format((float(candidate2_votes) / float(total_votes) *100), ".3f")

    candidate3_votes = candidates_with_votes.count(candidates[3])
    candidate3_percentage = format((float(candidate3_votes) / float(total_votes) *100), ".3f")    

    
    print()
    print(f"Election Results")
    print("-"*30)
    print(f"Total Votes: {total_votes}")
    print("-"*30)
    print(f"{candidates[0]}: {candidate0_percentage}% ({candidate0_votes})  ")
    print(f"{candidates[1]}: {candidate1_percentage}% ({candidate1_votes}) ")
    print(f"{candidates[2]}: {candidate2_percentage}% ({candidate2_votes}) ")
    print(f"{candidates[3]}: {candidate3_percentage}% ({candidate3_votes}) ")