import pandas as pd
import matplotlib.pyplot as plt

from utils.plotting import COLORS, save


def plot_univariate_analysis(df: pd.DataFrame, output_dir: str = 'graphs') -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 6))
    
    outcome_counts = df['Outcome'].value_counts()

    # Graph 1
    axes[0].bar(
        ['No Diabetes', 'Diabetes'], 
        outcome_counts.values,
        color=[COLORS['negative'], COLORS['positive']], 
        edgecolor='black'
    )
    axes[0].set_title('Distribution of Diabetes Outcome', fontsize=12)
    axes[0].set_xlabel('Outcome')
    axes[0].set_ylabel('Count')
    for i, v in enumerate(outcome_counts.values):
        axes[0].text(i, v + 5, str(v), ha='center', fontweight='bold')
    
    # Graph 2
    axes[1].pie(
        outcome_counts.values, 
        labels=['No Diabetes', 'Diabetes'],
        autopct='%1.1f%%', 
        colors=[COLORS['negative'], COLORS['positive']],
        explode=(0, 0.05), 
        shadow=True
    )
    axes[1].set_title('Proportion of Diabetes Outcome', fontsize=12)
    
    save(fig, f'{output_dir}/01_univariate_analysis.png')
