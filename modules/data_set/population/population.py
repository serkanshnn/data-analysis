import matplotlib.pyplot as plt
import seaborn as sns


def population_histogram(countries):
    countries_dict_first_20 = dict(countries.Population.value_counts().sort_values(ascending=False).head(20))

    plt.figure(figsize=(10, 10))  #
    sns.boxplot(y=list(countries_dict_first_20.keys()), x=list(countries_dict_first_20.values()), color="purple")
    plt.xlabel('\nPopulation')
    plt.title('Distributions of Population')
    plt.ylabel('Population\n')
    plt.show()
