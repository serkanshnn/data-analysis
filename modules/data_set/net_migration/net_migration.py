import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

def net_migration_hist(countries):
    sns.histplot(
        countries['NetMigration'],
        kde=True,
        color='yellow',
        bins=30,
        fill=True,
    )

    plt.title('Histogram of Net Migrations')
    plt.xlabel('Net Migrations')
    plt.ylabel('Net Migrations')
    plt.show()
