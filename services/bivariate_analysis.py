import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.plotting import COLORS


def plot_joint_plots(df: pd.DataFrame, output_dir: str = 'graphs') -> None:    
    g = sns.jointplot(
        data=df, x='Glucose', y='BMI', 
        hue='Outcome',
        palette=COLORS['palette'],
        kind='scatter', 
        alpha=0.6, 
        height=8
    )
    g.fig.suptitle('Glucose vs BMI by Diabetes', y=1.02, fontsize=14)
    plt.savefig(f'{output_dir}/03_joint_plot_glucose_bmi.png', dpi=150, bbox_inches='tight')
