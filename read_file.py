# src/read_file.py
import pandas as pd
# step 1: Define file path
file_path = r"C:\Users\grewa\p_AI\data\issue_log (1).xlsx"
# step 2: Read the Excel file into a DataFrame
df = pd.read_excel(file_path)
# step 3: Display the first few rows of the DataFrame
print("file read successfully")
print("total rows:", len(df))
print(df.head())
