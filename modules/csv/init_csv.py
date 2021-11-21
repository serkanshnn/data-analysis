from matplotlib import rcParams
import pandas as pd


def initialize_data_set():
    countries = pd.read_csv('../assets/countries.csv')
    print(f'Number of movies in dataset: {len(countries)}')

    countries.head()

    return countries


def configure_rc_params():
    rcParams['figure.figsize'] = 8, 6
    rcParams['font.family'] = 'Courier New',
    rcParams['font.size'] = 12.0
    rcParams['axes.titlesize'] = 18
    rcParams['axes.labelsize'] = 14
    rcParams['xtick.labelsize'] = 14
    rcParams['ytick.labelsize'] = 14
    rcParams['legend.fontsize'] = 11
    return rcParams
