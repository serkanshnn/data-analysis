from modules.csv import init_csv
from modules.data_set.region import region


def initialize_analysis():
    countries_set = init_csv.initialize_data_set()
    init_csv.configure_rc_params()
    return countries_set

def region_graph(countries):
    region.region_pie(countries)


countries = initialize_analysis()
region_graph(countries)
