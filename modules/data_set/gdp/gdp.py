import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def gdp_hist(countries):
    sns.histplot(
        countries['GDP'],
        kde=True,
        color='blue',
        bins=30,
        fill=True,
    )

    plt.title('Histogram of GDP')
    plt.xlabel('GDP')
    plt.ylabel('GDP')
    plt.show()
