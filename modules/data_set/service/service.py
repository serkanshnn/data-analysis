import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def service_histogram(countries):
    sns.histplot(
        countries['Service'],
        kde=True,
        color='green',
        bins=30,
        fill=True,
    )

    plt.title('Histogram of Service')
    plt.xlabel('Service')
    plt.ylabel('Service')
    plt.show()
