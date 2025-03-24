import pandas as pd

# Load the CSV file
df = pd.read_csv('customer_feedback.csv')

# Check the first few rows of the data
print("First few rows of the data:\n")
print(df.head())

# Check for missing values
print("\nChecking for missing values:\n")
print(df.isnull().sum())

# Get a summary of the data
print("\nSummary of the data:\n")
print(df.info())

