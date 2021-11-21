import matplotlib.pyplot as plt
import seaborn as sns

def area_boxplot(countries):
    plt.figure(figsize=(10, 10))  #
    sns.boxplot(countries.Area, color="brown")
    plt.xlabel('\nArea')
    plt.title('Distributions of Area')
    plt.ylabel('Area\n')
    plt.show()
