
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'election_data.csv')

# The total number of votes cast
total_votes=0
# A complete list of candidates who received votes
candidates_list=[]
# The percentage of votes each candidate won
candidate_dictionary={}
# The total number of votes each candidate won

# The winner of the election based on popular vote


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_votes=total_votes+1

        candidate_name=row[2]

        if candidate_name not in candidates_list:
            candidates_list.append(candidate_name)
            candidate_dictionary[candidate_name]=0
        candidate_dictionary[candidate_name]+=1
           
candidates_percentage = {key: round(val / total_votes*100,3) for key,val in candidate_dictionary.items()}
max_value = max(candidate_dictionary, key=candidate_dictionary.get)
print(max_value)

print(total_votes)
print(candidates_list)
print(candidate_dictionary)
print(candidates_percentage)

output1=(
f"Election Results\n"
f"-------------------------\n"
f"Total Votes: 369711\n"
f"-------------------------\n")

output3=(f"-------------------------\n"
f"Winner: Diana DeGette\n"
f"-------------------------\n"


)

output_path = os.path.join( 'analysis', 'election_data.txt')
with open(output_path,"w") as output_txt:
    output_txt.write(output1)
    for k, v in candidate_dictionary.items():
        output_txt.write(f"{k}: {candidates_percentage[k]}% ({v})\n")
    output_txt.write(output3)