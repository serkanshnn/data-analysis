from modules.csv import init_csv
from modules.data_set.region import region
from modules.data_set.population import population
from modules.data_set.area import area
from modules.data_set.population_density import population_density
from modules.data_set.coastline import coastline
from modules.data_set.net_migration import net_migration
from modules.data_set.infant_mortality import infant_mortality
from modules.data_set.gdp import gdp
from modules.data_set.literacy import literacy
from modules.data_set.phones import phones
from modules.data_set.arable import arable
from modules.data_set.crops import crops
from modules.data_set.other import other
from modules.data_set.climate import climate
from modules.data_set.birthrate import birthrate
from modules.data_set.agriculture import agriculture
from modules.data_set.industry import industry
from modules.data_set.service import service


def initialize_analysis():
    countries_set = init_csv.initialize_data_set()
    init_csv.configure_rc_params()
    return countries_set

def region_graph(countries):
    region.region_pie(countries)

def population_graph(countries):
    population.population_histogram(countries)

def area_graph(countries):
    area.area_histogram(countries)

def population_density_graph(countries):
    population_density.population_density_bar(countries)

def coastline_graph(countries):
    coastline.coastline_hist(countries)

def net_migration_graph(countries):
    net_migration.net_migration_hist(countries)

def infant_mortality_graph(countries):
    infant_mortality.infant_mortality_bar(countries)

def gdp_graph(countries):
    gdp.gdp_dis(countries)

def literacy_graph(countries):
    literacy.literacy_histogram(countries)

def phones_graph(countries):
    phones.phones_histogram(countries)

def arable_graph(countries):
    arable.arable_bar(countries)

def crops_graph(countries):
    crops.crops_histogram(countries)

def other_graph(countries):
    other.other_bar(countries)

def climate_graph(countries):
    climate.climate_bar(countries)

def birthrate_graph(countries):
    birthrate.birthrate_bar(countries)

def agriculture_graph(countries):
    agriculture.agriculture_histogram(countries)

def industry_graph(countries):
    industry.industry_histogram(countries)

def service_graph(countries):
    service.service_histogram(countries)

countries = initialize_analysis()
region_graph()
# population_graph()
# area_graph()
# population_density_graph()
# coastline_graph()
# net_migration_graph()
# infant_mortality_graph()
# gdp_graph()
# literacy_graph()
# phones_graph()
# arable_graph()
# crops_graph()
# other_graph()
# climate_graph()
# birthrate_graph()
# agriculture_graph()
# industry_graph()
# service_graph()
