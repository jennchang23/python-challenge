# Import dependencies
import os
import csv
import statistics

# Create empty list to store each month value and profit/loss value
monthlist = []
plvaluelist = []

# Open data file
with open(os.path.join("../../USC-LA-DATA-PT-11-2019-U-C/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv"),"r") as budgetdatafile:
    budgetdata_reader = csv.reader(budgetdatafile,delimiter = ",")
    csv_header = next(budgetdatafile)
    
    for row in budgetdata_reader:
        # Count months -- add months from Column 1 to monthlist & store length of list in totalmonthcount variable -- this is working under the assumption that all values in this column will always be unique & there is no need to check for unique values.
        monthlist.append(row[0])
        totalmonthcount = int(len(monthlist))
        # Create list of profit/loss values in plvaluelist
        plvaluelist.append(int(row[1]))
        # Profit/Loss Calculations
        # Net Total in totalprofitloss variable
        totalprofitloss = sum(plvaluelist)
        # Create new list for changes MoM
        plchangelist = []
        for i in range(1, len(plvaluelist)):
            momchange = int(plvaluelist[i] - plvaluelist[i-1])
            plchangelist.append(int(momchange))
            # Average of Profit/Loss changes in avgprofitloss variable
            avgprofitloss = round(statistics.mean(plchangelist),2)
            # Greatest increase in profits (date and amount)
            greatIncValue = 0
            for plchangevalue in plchangelist:
                if plchangevalue >= greatIncValue:
                    greatIncValue = plchangevalue
                else:
                    greatIncValue = greatIncValue
            greatIncMonth = monthlist[plchangelist.index(greatIncValue) + 1]
            # Greatest decrease in profits (date and amount)
            greatDecValue = 0
            for plchangevalue in plchangelist:
                if plchangevalue < greatDecValue:
                    greatDecValue = plchangevalue
                else:
                    greatDecValue = greatDecValue
    greatDecMonth = monthlist[plchangelist.index(greatDecValue) + 1]
    ## Why does this have to be indented here when greatIncMonth is indented further and prints fine?
   
    # Print analysis to Terminal
    FinancialAnalysis = ("Financial Analysis" + '\n' + "-"*25 + '\n' + f"Total Months: {totalmonthcount}" + '\n' + f"Total: ${totalprofitloss}" + '\n' + f"Average Change: ${avgprofitloss}" + '\n' + f"Greatest Increase in Profits: {greatIncMonth} (${greatIncValue})" + '\n' + f"Greatest Decrease in Profits: {greatDecMonth} (${greatDecValue})")
    print(FinancialAnalysis)

# Specify the file to write to
output_path = os.path.join("Finanacial_Analysis.txt")
# Open the file using "write" mode. Specify the variable to hold the contents

with open(output_path, 'w') as txtfile:
    # Initialize txt.writer
    txtfile.write(FinancialAnalysis)