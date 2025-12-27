
import pandas as pd
#from data_cleaning.cleaning import clean_data
#from data_normalization.normalize import normalize_data

def main():
    df = pd.read_csv("StudentsPerformance.csv")
    df.to_csv("processed/cleaned_data.csv", index=False)

if __name__ == "__main__":
    main()
