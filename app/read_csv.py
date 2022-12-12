import csv

def read_csv(path):
    with open(path,'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header,row)
            country = {key:value for key,value in iterable }
            data.append(country)
        return data

if __name__ == '__main__':
    data = read_csv('/Users/emilianogtlp/Documents/cursos_platzi/Python 201/app/world_population.csv')
    print(data[0])