import pandas as pd


def load_diabetes_data(filepath: str = 'graphs/diabetes.csv') -> pd.DataFrame:
    return pd.read_csv(filepath)
