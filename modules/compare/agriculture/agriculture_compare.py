import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(countries):
    sns.scatterplot(
        x="Agriculture",
        y="GDP",
        data=countries,
    )

    plt.title('Agriculture / GDP Scatter Plot')
    plt.xlabel('Agriculture')
    plt.ylabel('GDP')
    plt.show()


def show_regression(countries):
    x_var = pd.DataFrame(countries["Agriculture"])
    y_var = pd.DataFrame(countries["GDP"])

    sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Agriculture / GDP Regression')
    plt.xlabel('Agriculture')
    plt.ylabel('GDP')
    plt.show()
