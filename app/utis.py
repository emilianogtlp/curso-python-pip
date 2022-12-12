
def get_population(country_dict):
    population = {
        '2022':int(country_dict['2022 Population']),
        '2020':int(country_dict['2020 Population']),
        '2015':int(country_dict['2015 Population']),
        '2010':int(country_dict['2010 Population']),
        '2000':int(country_dict['2000 Population']),
        '1990':int(country_dict['1990 Population']),
        '1980':int(country_dict['1980 Population']),
        '1970':int(country_dict['1970 Population'])
    }
    labels = population.keys()
    values = population.values()
    return labels,values

def get_percentage(data):
    result = {}
    for country in range(len(data)):
        result.update({data[country]['Country/Territory']:data[country]['World Population Percentage']})
    labels = result.keys()
    values = result.values()
    return labels, values


def population_by_country(data,country):
    result = list(filter(lambda item:item['Country/Territory'] == country,data))
    return result