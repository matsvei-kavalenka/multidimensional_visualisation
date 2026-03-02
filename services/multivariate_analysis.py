import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

from utils.preprocessing import normalize_dataframe
from utils.plotting import save


def plot_parallel_coordinates(df: pd.DataFrame, output_dir: str = 'graphs') -> None:
    df_normalized = normalize_dataframe(df, exclude_cols=['Outcome'])
    
    df_normalized['Diabetes_Status'] = df['Outcome'].map({
        0: 'No Diabetes', 
        1: 'Diabetes'
    })
    
    fig, ax = plt.subplots(figsize=(14, 7))
    parallel_coordinates(
        df_normalized, 
        'Diabetes_Status',
        colormap=plt.cm.coolwarm, 
        alpha=0.5, 
        ax=ax
    )
    ax.set_title('Parallel Coordinates Plot', fontsize=14)
    ax.set_ylabel('Normalized Value')
    ax.legend(loc='upper right')
    plt.xticks(rotation=45, ha='right')
    
    save(fig, f'{output_dir}/02_parallel_coordinates.png')
