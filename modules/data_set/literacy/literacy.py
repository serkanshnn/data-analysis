import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def literacy_histogram(countries):
    sns.histplot(
        countries['Literacy'],
        kde=True,
        color='blue',
        bins=20,
    )

    plt.title('Histogram of Literacy')
    plt.xlabel('Literacy')
    plt.ylabel('Literacy')
    plt.show()
