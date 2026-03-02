import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.preprocessing import split_by_outcome
from utils.plotting import COLORS, save


def plot_boxplot_violin(df: pd.DataFrame, output_dir: str = 'graphs') -> None:
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    sns.boxplot(
        data=df, x='Outcome', y='Glucose', 
        ax=axes[0, 0], hue='Outcome',
        palette=COLORS['palette'], legend=False
    )
    axes[0, 0].set_title('Boxplot: Glucose Distribution by Diabetes Status', fontsize=12)
    axes[0, 0].set_xticklabels(['No Diabetes', 'Diabetes'])
    
    sns.violinplot(
        data=df, x='Outcome', y='Glucose', 
        ax=axes[0, 1], hue='Outcome',
        palette=COLORS['palette'], 
        inner='quartile', legend=False
    )
    axes[0, 1].set_title('Violin Plot: Glucose Distribution by Diabetes Status', fontsize=12)
    axes[0, 1].set_xticklabels(['No Diabetes', 'Diabetes'])
    
    sns.boxplot(
        data=df, x='Outcome', y='BMI', 
        ax=axes[1, 0], hue='Outcome',
        palette=COLORS['palette'], legend=False
    )
    axes[1, 0].set_title('Boxplot: BMI Distribution by Diabetes Status', fontsize=12)
    axes[1, 0].set_xticklabels(['No Diabetes', 'Diabetes'])
    
    sns.violinplot(
        data=df, x='Outcome', y='BMI', 
        ax=axes[1, 1], hue='Outcome',
        palette=COLORS['palette'], 
        inner='quartile', legend=False
    )
    axes[1, 1].set_title('Violin Plot: BMI Distribution by Diabetes Status', fontsize=12)
    axes[1, 1].set_xticklabels(['No Diabetes', 'Diabetes'])
    
    save(fig, f'{output_dir}/04_boxplot_violin_plots.png')


def plot_distribution_comparison(df: pd.DataFrame, output_dir: str = 'graphs') -> None:
    df_no_diabetes, df_diabetes = split_by_outcome(df)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    axes[0, 0].hist(
        df_no_diabetes['Glucose'], bins=25, alpha=0.6,
        label='No Diabetes', color=COLORS['negative'], edgecolor='black'
    )
    axes[0, 0].hist(
        df_diabetes['Glucose'], bins=25, alpha=0.6,
        label='Diabetes', color=COLORS['positive'], edgecolor='black'
    )
    axes[0, 0].set_title('Overlapping Histograms: Glucose by Diabetes Status', fontsize=12)
    axes[0, 0].set_xlabel('Glucose')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].legend()
    
    sns.kdeplot(
        data=df, x='Glucose', hue='Outcome', 
        ax=axes[0, 1],
        palette=COLORS['palette'], 
        fill=True, 
        alpha=0.5
    )
    axes[0, 1].set_title('KDE Plot: Glucose Distribution by Diabetes Status', fontsize=12)
    
    
    sns.stripplot(
        data=df, x='Outcome', y='Glucose', 
        ax=axes[1, 0], hue='Outcome',
        palette=COLORS['palette'], 
        alpha=0.5, 
        jitter=True, legend=False
    )
    axes[1, 0].set_title('Strip Plot: Glucose by Diabetes Status', fontsize=12)
    axes[1, 0].set_xticklabels(['No Diabetes', 'Diabetes'])
    
    sample_df = df.sample(min(200, len(df)), random_state=42)
    sns.swarmplot(
        data=sample_df, x='Outcome', y='Glucose', 
        ax=axes[1, 1], hue='Outcome',
        palette=COLORS['palette'], legend=False
    )
    axes[1, 1].set_title('Swarm Plot: Glucose by Diabetes Status (Sampled)', fontsize=12)
    axes[1, 1].set_xticklabels(['No Diabetes', 'Diabetes'])
    
    save(fig, f'{output_dir}/06_distribution_across_categories.png')
