import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(countries):
    sns.scatterplot(
        x="Industry",
        y="GDP",
        data=countries,
    )

    plt.title('Industry / GDP Scatter Plot')
    plt.xlabel('Industry')
    plt.ylabel('GDP')
    plt.show()


def show_regression(countries):
    x_var = pd.DataFrame(countries["Industry"])
    y_var = pd.DataFrame(countries["GDP"])

    sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Industry / GDP Regression')
    plt.xlabel('Industry')
    plt.ylabel('GDP')
    plt.show()
