import csv
import os
import pandas as pd

election_csv = os.path.join('Resources','election_data.csv')
election_df = pd.read_csv(election_csv)
print(election_df.head())
total_votes = len(election_df['Voter ID'].unique())
candidate_counts = election_df['Candidate'].value_counts()
candidate_percents = election_df['Candidate'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'

election_results = pd.DataFrame({'Counts':candidate_counts,'Percentages':candidate_percents})
# winner = election_results.iloc[election_results['Percentages'].idxmax()]


print(election_results)
print(f"There are total votes of {total_votes}")
# print(winner)
output_file = os.path.join('PyPoll_Result.txt')

with open(output_file,"w") as file:
    file.write(f"There are total votes of {total_votes}")
    file.write("\n")
    file.write("\n")
    file.write(f"{election_results}")
