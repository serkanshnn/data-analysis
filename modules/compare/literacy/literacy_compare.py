import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(countries):
    sns.scatterplot(
        x="Literacy",
        y="GDP",
        data=countries,
    )

    plt.title('Literacy / GDP Scatter Plot')
    plt.xlabel('Literacy')
    plt.ylabel('GDP')
    plt.show()


def show_regression(countries):
    x_var = pd.DataFrame(countries["Literacy"])
    y_var = pd.DataFrame(countries["GDP"])

    sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('Literacy / GDP Regression')
    plt.xlabel('Literacy')
    plt.ylabel('GDP')
    plt.show()
