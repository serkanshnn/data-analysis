import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model


def show_scatter_plot(countries):
    sns.scatterplot(
        x="NetMigration",
        y="GDP",
        data=countries,
    )

    plt.title('NetMigration / GDP Scatter Plot')
    plt.xlabel('NetMigration')
    plt.ylabel('GDP')
    plt.show()


def show_regression(countries):
    x_var = pd.DataFrame(countries["NetMigration"])
    y_var = pd.DataFrame(countries["GDP"])

    sns.regplot(x=x_var, y=y_var, color="b")
    plt.title('NetMigration / GDP Regression')
    plt.xlabel('NetMigration')
    plt.ylabel('GDP')
    plt.show()
