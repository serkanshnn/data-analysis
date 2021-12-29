import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(countries):
    sns.scatterplot(
        x="Area",
        y="GDP",
        data=countries,
    )

    plt.title('Area / GDP Scatter Plot')
    plt.xlabel('Area')
    plt.ylabel('GDP')
    plt.show()


def show_regression(countries):
    x_var = pd.DataFrame(countries["Area"])
    y_var = pd.DataFrame(countries["GDP"])

    sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Area / GDP Regression')
    plt.xlabel('Area')
    plt.ylabel('GDP')
    plt.show()
