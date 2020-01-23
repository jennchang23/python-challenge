import os
import csv

voterCount = 0
candidateList = []
voteCountDict = dict()
votePctgDict = dict()
summaryDict = dict()
summaryList = []
winner = str()
body = 0

# Open data file
with open(os.path.join("../../USC-LA-DATA-PT-11-2019-U-C/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv"), "r") as electiondatafile:
    electiondata_reader = csv.reader(electiondatafile,delimiter = ",")
    csv_header = next(electiondatafile)
    for row in electiondata_reader:
        # Count total votes
        voterCount = voterCount + 1
        # List of candidate names (unique)
        if row[2] not in candidateList:
            candidateList.append(row[2])
        # Count votes for each candidate in dictionary voteCountDict
        for candidate in row[2].split(" "):
            if candidate not in voteCountDict:
                voteCountDict[candidate] = 1
            else:
                voteCountDict[candidate] += 1
        # Calculate %age of total votes each candidate has in dictionary votePctgDict
        for candidate, votes in voteCountDict.items():
            votePctgDict[candidate] = "{:.3%}".format(votes / voterCount)
        # Find out who has most votes
        winner = max(voteCountDict, key=voteCountDict.get)
        # Zip dictionaries together
        def summaryDict(*args):
            result = {}
            for dic in args:
                for key in (result.keys() | dic.keys()):
                    if key in dic:
                        result.setdefault(key, []).append(dic[key])
            return result
        summaryDict = summaryDict(votePctgDict, voteCountDict)
    # Header and footer lines
    header = ("\n" + "Election Results" + "\n" + "-"*25 + "\n" + f"Total Votes: {voterCount}" + "\n" + "-"*25 + "\n")
    footer = ("\n" + "-"*25 + "\n" + f"Winner: {winner}" + "\n" + "-"*25)
# Print to Terminal
print(header)
for i in candidateList:
    for x in summaryDict:
        if body == 0 and x == i:
            body = (f'{i}: {summaryDict[x][0]} ({summaryDict[x][1]})')
        elif x == i:
            body = (f"{body}" + "\n" + f'{i}: {summaryDict[x][0]} ({summaryDict[x][1]})')
print(body)
print(footer)
# Variable for body of output -- for printing to txt file
output = (f"{header}" + "\n" + f"{body}" + "\n" + f"{footer}")

# Create text file name
output_path = os.path.join("Election_Results.txt")

with open(output_path,'w') as txtfile:
    txtfile.write(output)