from utils.data_loader import load_diabetes_data
from utils.plotting import setup_plot_style
from services.univariate_analysis import plot_univariate_analysis
from services.multivariate_analysis import plot_parallel_coordinates
from services.bivariate_analysis import plot_joint_plots
from services.distribution_analysis import plot_boxplot_violin, plot_distribution_comparison
from services.three_d_analysis import plot_3d_scatter


DATA_PATH = 'data/diabetes.csv'
OUTPUT_DIR = 'graphs'

df = load_diabetes_data(DATA_PATH)

setup_plot_style()

# 1. Univariate Analysis (discrete/categorical 1-D)
plot_univariate_analysis(df, OUTPUT_DIR)

# 2. Multivariate Analysis - Parallel coordinates
plot_parallel_coordinates(df, OUTPUT_DIR)

# 3. Joint Plot (two continuous numeric attributes)
plot_joint_plots(df, OUTPUT_DIR)

# 4. Boxplot and Violin plots (compare distributions across categories)
plot_boxplot_violin(df, OUTPUT_DIR)

# 5. 3D scatter plots (three dimensions)
plot_3d_scatter(df, OUTPUT_DIR)

# 6. Distribution across categories
plot_distribution_comparison(df, OUTPUT_DIR)

