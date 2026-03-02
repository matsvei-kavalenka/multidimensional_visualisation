import matplotlib.pyplot as plt

COLORS = {
    'negative': 'steelblue',
    'positive': 'coral',
    'palette': {0: 'steelblue', 1: 'coral'},
}


def setup_plot_style() -> None:
    plt.style.use('seaborn-v0_8-whitegrid')


def save(fig, filepath: str, dpi: int = 150) -> None:
    plt.tight_layout()
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight')