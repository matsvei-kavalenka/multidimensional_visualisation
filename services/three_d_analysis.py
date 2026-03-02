import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from utils.preprocessing import split_by_outcome
from utils.plotting import COLORS, save


def plot_3d_scatter(df: pd.DataFrame, output_dir: str = 'graphs') -> None:
    df_no_diabetes, df_diabetes = split_by_outcome(df)
    
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(
        df_no_diabetes['Glucose'], 
        df_no_diabetes['BMI'], 
        df_no_diabetes['Age'],
        c=COLORS['negative'], 
        label='No Diabetes', 
        alpha=0.6, 
        s=50
    )
    ax.scatter(
        df_diabetes['Glucose'], 
        df_diabetes['BMI'], 
        df_diabetes['Age'],
        c=COLORS['positive'], 
        label='Diabetes', 
        alpha=0.6, 
        s=50
    )
    
    ax.set_xlabel('Glucose', fontsize=11)
    ax.set_ylabel('BMI', fontsize=11)
    ax.set_zlabel('Age', fontsize=11)
    ax.set_title('3D Scatter Plot: Glucose, BMI, and Age by Diabetes Status', fontsize=14)
    ax.legend()
    ax.view_init(elev=20, azim=45)
    
    save(fig, f'{output_dir}/05_3d_scatter_plot.png')
    
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(
        df_no_diabetes['BloodPressure'], 
        df_no_diabetes['Insulin'], 
        df_no_diabetes['Age'],
        c=COLORS['negative'], 
        label='No Diabetes', 
        alpha=0.6, 
        s=50
    )
    ax.scatter(
        df_diabetes['BloodPressure'], 
        df_diabetes['Insulin'], 
        df_diabetes['Age'],
        c=COLORS['positive'], 
        label='Diabetes', 
        alpha=0.6, 
        s=50
    )
    
    ax.set_xlabel('Blood Pressure', fontsize=11)
    ax.set_ylabel('Insulin', fontsize=11)
    ax.set_zlabel('Age', fontsize=11)
    ax.set_title('3D Scatter Plot: Blood Pressure, Insulin, and Age', fontsize=14)
    ax.legend()
    ax.view_init(elev=20, azim=135)
    
    save(fig, f'{output_dir}/05b_3d_scatter_plot_bp_insulin.png')
