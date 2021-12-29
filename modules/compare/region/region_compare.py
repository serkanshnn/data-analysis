import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(countries):
    sns.scatterplot(
        x="Region",
        y="GDP",
        data=countries,
    )

    plt.title('Region / GDP Scatter Plot')
    plt.xlabel('Region')
    plt.ylabel('GDP')
    plt.xticks(rotation=20)
    plt.show()
