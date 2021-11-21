import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def agriculture_histogram(countries):
    sns.histplot(
        countries['Agriculture'],
        kde=True,
        color='brown',
        bins=30,
        fill=True,
    )

    plt.title('Histogram of Agriculture')
    plt.xlabel('Agriculture')
    plt.ylabel('Agriculture')
    plt.show()
