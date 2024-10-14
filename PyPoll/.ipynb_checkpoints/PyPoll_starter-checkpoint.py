# -*- coding: UTF-8 -*-


# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes +=1

        # Get the candidate's name from the row
        name = row[2]

        # If the candidate is not already in the candidate list, add them
        if name not in candidate_votes:
            candidate_votes[name]=0

        # Add a vote to the candidate's count
        candidate_votes[name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    results = (
        f"Election Results\n"
        f"\n"
        f"----------------------------\n"
        f"\n"
        f"Total Votes: {total_votes}\n"
        f"\n"
        f"----------------------------\n"
        f"\n"
    )

    # Write the total vote count to the text file

    # Loop through the candidates to determine vote percentages and identify the winner
    for name in candidate_votes:
        

        # Get the vote count and calculate the percentage
        votes = candidate_votes[name]
        percentage = (votes/total_votes) *100

        # Update the winning candidate if this one has more votes
        if (votes > winning_count) and (percentage > winning_percentage):
            winning_count = votes
            winning_candidate = name
            winning_percentage = percentage

        # Print and save each candidate's vote count and percentage
        candidate_votes[name] = (percentage,votes)

        results += (
            f"\n"
            f"{name}: {percentage:.3f}% ({votes})\n"
            f"\n"
        )

    # Generate and print the winning candidate summary
    results += (
        f"\n"
        f"---------------------\n"
        f"\n"
        f"Winner: {winning_candidate}\n"
        f"\n"
        f"---------------------\n"
    )

    print(results)
    with open(file_to_output, "w") as txt_file:
    # Save the winning candidate summary to the text file
        txt_file.write(results)
