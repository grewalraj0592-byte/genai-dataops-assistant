import pandas as pd

def load_issue_log(file_path=r"C:\Users\grewa\p_AI\data\issue_log (1).xlsx"):
    df = pd.read_excel(file_path)
    print(f"Loaded {df.shape[0]} records.")
    print(df.head())
    return df

if __name__ == "__main__":
    load_issue_log()

