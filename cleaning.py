from __future__ import annotations
from typing import Dict, Tuple

import numpy as np
import pandas as pd


def _normalize_col_name(col: str) -> str:
    s = col.strip().lower()
    for ch in ["/", "-", "(", ")", "[", "]"]:
        s = s.replace(ch, " ")
    s = "_".join(s.split())
    return s


def standardize_columns(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, str]]:
    mapping = {c: _normalize_col_name(c) for c in df.columns}
    df2 = df.rename(columns=mapping).copy()
    return df2, mapping


def clean_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, int]]:
    df2 = df.copy()

    cat_cols = [c for c in df2.columns if df2[c].dtype == "object"]
    for c in cat_cols:
        df2[c] = df2[c].astype(str).str.strip()
        df2.loc[df2[c].str.lower().isin(["nan", "none", "null", ""]), c] = np.nan
        df2[c] = df2[c].str.lower()

    before = len(df2)
    df2 = df2.drop_duplicates().reset_index(drop=True)
    removed_dups = before - len(df2)

    score_like = [c for c in df2.columns if "score" in c]
    for c in score_like:
        df2[c] = pd.to_numeric(df2[c], errors="coerce")
        out_of_range = (~df2[c].isna()) & ((df2[c] < 0) | (df2[c] > 100))
        df2.loc[out_of_range, c] = np.nan

    missing_before = int(df2.isna().sum().sum())

    for c in score_like:
        if df2[c].isna().any():
            df2[c] = df2[c].fillna(df2[c].mean())

    for c in cat_cols:
        if df2[c].isna().any():
            mode = df2[c].mode(dropna=True)
            fill_val = mode.iloc[0] if len(mode) else "unknown"
            df2[c] = df2[c].fillna(fill_val)

    missing_after = int(df2.isna().sum().sum())

    stats = {
        "removed_duplicates": int(removed_dups),
        "missing_before": int(missing_before),
        "missing_after": int(missing_after),
    }
    return df2, stats


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    score_cols = [c for c in df2.columns if c in ["math_score", "reading_score", "writing_score"]]
    if len(score_cols) == 3:
        df2["tong_diem"] = df2["math_score"] + df2["reading_score"] + df2["writing_score"]
        df2["average_score"] = df2["tong_diem"] / 3.0
    return df2
