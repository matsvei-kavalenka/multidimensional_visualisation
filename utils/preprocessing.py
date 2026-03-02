import pandas as pd


def normalize_dataframe(df: pd.DataFrame, exclude_cols: list[str] = None) -> pd.DataFrame:
    if exclude_cols is None:
        exclude_cols = []
    
    df_normalized = df.copy()
    for col in df.columns:
        if col not in exclude_cols:
            col_min = df[col].min()
            col_max = df[col].max()
            if col_max != col_min:
                df_normalized[col] = (df[col] - col_min) / (col_max - col_min)
    
    return df_normalized


def split_by_outcome(df: pd.DataFrame, outcome_col: str = 'Outcome') -> tuple[pd.DataFrame, pd.DataFrame]:
    df_negative = df[df[outcome_col] == 0]
    df_positive = df[df[outcome_col] == 1]
    return df_negative, df_positive
