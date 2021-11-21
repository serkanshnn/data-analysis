import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd


def coastline_hist(countries):
    coastlines = pd.Series(countries.Coastline)

    sns.boxplot(
        coastlines,
        color='purple',
    )

    plt.title('Histogram of Coastline')
    plt.xlabel('Coastline')
    plt.ylabel('Coastline')
    plt.show()



