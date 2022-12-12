import read_csv
import utis
import charts
import pandas as pd

def run():
    '''
    data = read_csv.read_csv('./world_population.csv')
    country = input("Teclee el nombre del pais: ")
    
    '''

    df = pd.read_csv('./world_population.csv')
    df = df[df['Continent']=='South America']

    countries = df['Country/Territory'].values
    percentage = df['World Population Percentage'].values

    charts.generate_pie_chart('South America',countries,percentage)

    '''
    country = utis.population_by_country(data,country)

    if len(country) > 0:
        country_name = country[0]
        key,values = utis.get_population(country_name)

        charts.generate_bar_chart(country_name['Country/Territory'],key,values)


def pie():
    data = read_csv.read_csv('./world_population.csv')
    labels, values = utis.get_percentage(data)
'''

if __name__ == '__main__':
    run()