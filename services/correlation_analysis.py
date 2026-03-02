import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.plotting import COLORS, save


def plot_correlation_heatmap(df: pd.DataFrame, output_dir: str = 'graphs') -> None:
    
    fig, ax = plt.subplots(figsize=(10, 8))
    correlation_matrix = df.corr()
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap='coolwarm', 
        center=0,
        fmt='.2f', 
        linewidths=0.5, 
        ax=ax
    )
    ax.set_title('Correlation Heatmap - All Features', fontsize=14)
    
    save(fig, f'{output_dir}/07_correlation_heatmap.png')


def plot_pair_plot(
    df: pd.DataFrame, 
    features: list[str] = None,
    output_dir: str = 'graphs'
) -> None:    
    if features is None:
        features = ['Glucose', 'BMI', 'Age', 'BloodPressure', 'Outcome']
    
    g = sns.pairplot(
        df[features], 
        hue='Outcome',
        palette=COLORS['palette'],
        diag_kind='kde', 
        plot_kws={'alpha': 0.5}
    )
    g.fig.suptitle('Pair Plot: Key Features by Diabetes Status', y=1.02, fontsize=14)
    plt.savefig(f'{output_dir}/08_pair_plot.png', dpi=150, bbox_inches='tight')
    plt.show()
