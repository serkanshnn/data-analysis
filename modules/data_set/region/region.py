import seaborn as sns
import matplotlib.pyplot as plt


def region_pie(countries):
    region_dict_first_10 = dict(countries.Region.value_counts().sort_values(ascending=False).head(10))
    labels = region_dict_first_10.keys()
    sizes = region_dict_first_10.values()
    colors = [
        '#fff100',
        '#ff8c00',
        '#e81123',
        '#ec008c',
        '#68217a',
        '#00188f',
        '#00bcf2',
        '#00b294',
        '#009e49',
        '#bad80a',
    ]

    with sns.color_palette("colorblind"):
        plt.pie(
            sizes,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            startangle=45,
        )

    plt.title("Regions")
    plt.axis('equal')
    plt.show()
