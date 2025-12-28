
import pandas as pd
from pathlib import Path

from cleaning import standardize_columns, clean_data, add_features


def main():
    df = pd.read_csv("StudentsPerformance.csv")

    df, _ = standardize_columns(df)
    df, _stats = clean_data(df)
    df = add_features(df)

    Path("processed").mkdir(parents=True, exist_ok=True)
    df.to_csv("processed/cleaned_data.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    main()
