"""
======================================================================
ex9
======================================================================
Writen by: Rotem kashani, ID = 209073352,   login = rotemkash
	       David Koplev, ID = 208870279 ,    login = davidkop
Program follows 8 actions from the exercise given:
Q1 - read the file and convert to a chart
Q2- print the 7 first lines
Q3- replace the name of the Severity of illness col to Severity
Q4- remove all non-needed data and keeps the first word only
Q5 - Converting words in to numerical values
Q6 - In the height column insert outer height value
Q7 - Delete any empty cells in weight column and limit to 110kg
Q8 - Search correlation between rows and columns
"""

import pandas as pd

# Question 1
file = pd.read_csv("ex10_file.csv")

# Question 2
print(file.head(7))

# Question 3
file.rename(columns={"Severity of illness - worst score during admission": "Severity"}, inplace=True)

# Question 4
file["Severity"] = file["Severity"].str.split().str[0]

print(file["Severity"])

# Question 5
severity_mapping = {
    "Mild": 0,
    "Moderate": 1,
    "Severe": 2,
    "Critical": 3
}

file["Severity"] = file["Severity"].replace(severity_mapping)
print(file["Severity"])

# Question 6
median_height = file["Height"].median()
file["Height"].fillna(median_height, inplace=True)
print(file["Height"])

# Question 7
file.dropna(subset=["Weight"], inplace=True)
file["Weight"] = file["Weight"].clip(upper=110)  # Limit weight at 110 kg
print(file["Weight"])

# Question 8
file["Severity"] = pd.to_numeric(file["Severity"], errors="coerce")  # Convert "Severity" to numeric values
correlation_matrix = file.corr()
print(correlation_matrix)
