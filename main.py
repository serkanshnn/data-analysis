from modules.csv import init_csv
from modules.data_set.region import region
from modules.data_set.population import population
from modules.data_set.area import area
from modules.data_set.coastline import coastline
from modules.data_set.net_migration import net_migration
from modules.data_set.gdp import gdp
from modules.data_set.literacy import literacy
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
    area.area_boxplot(countries)

def coastline_graph(countries):
    coastline.coastline_hist(countries)

def net_migration_graph(countries):
    net_migration.net_migration_hist(countries)

def gdp_graph(countries):
    gdp.gdp_hist(countries)

def literacy_graph(countries):
    literacy.literacy_histogram(countries)

def agriculture_graph(countries):
    agriculture.agriculture_histogram(countries)

def industry_graph(countries):
    industry.industry_histogram(countries)

def service_graph(countries):
    service.service_histogram(countries)

def describe_attributes(countries):
    print(countries['Region'].describe())
    print(countries['Population'].describe())
    print(countries['Area'].describe())
    print(countries['Coastline'].describe())
    print(countries['NetMigration'].describe())
    print(countries['GDP'].describe())
    print(countries['Literacy'].describe())
    print(countries['Agriculture'].describe())
    print(countries['Industry'].describe())
    print(countries['Service'].describe())

countries = initialize_analysis()
region_graph(countries)
population_graph(countries)
area_graph(countries)
coastline_graph(countries)
net_migration_graph(countries)
gdp_graph(countries)
literacy_graph(countries)
agriculture_graph(countries)
industry_graph(countries)
service_graph(countries)
describe_attributes(countries)
