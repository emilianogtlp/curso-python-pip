import read_csv
import utis
import charts

def run():
    data = read_csv.read_csv('/Users/emilianogtlp/Documents/cursos_platzi/py-proyect/app/world_population.csv')
    country = input("Teclee el nombre del pais: ")
    
    country = utis.population_by_country(data,country)

    if len(country) > 0:
        country_name = country[0]
        key,values = utis.get_population(country_name)

        charts.generate_bar_chart(country_name['Country/Territory'],key,values)


def pie():
    data = read_csv.read_csv('/Users/emilianogtlp/Documents/cursos_platzi/py-proyect/app/world_population.csv')
    labels, values = utis.get_percentage(data)
    charts.generate_pie_chart(labels,values)

if __name__ == '__main__':
    run()