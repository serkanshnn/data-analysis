import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def industry_histogram(countries):
    sns.histplot(
        countries['Industry'],
        kde=True,
        color='grey',
        bins=20,
    )

    plt.title('Histogram of Industry')
    plt.xlabel('Industry')
    plt.ylabel('Industry')
    plt.show()
