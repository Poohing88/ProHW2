import json
import hashlib


class Country:
    def __init__(self, way):
        self.way = way
        with open(f'{way}', mode='r', encoding='utf8') as f:
            self.file = json.load(f)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            country = self.file[self.counter]['name']['common'].split()
            countries = '_'.join(country)
            countries_name = ''.join(country)
            url = f'https://wikipedia.org/wiki/{countries}'
            self.counter += 1
            return countries_name, url
        except IndexError:
            raise StopIteration

    def write(self, countries_name, url):
        way = f'db/{countries_name}.txt'
        with open(f'db/{countries_name}.txt', mode='w', encoding='utf8') as files:
            files.write(f'{countries_name}\n{url}')
        return way

    def code(self, way):
        with open(f'{way}', mode='r', encoding='utf8') as file:
            for i in file:
                code = hashlib.md5(i.encode('utf-8')).hexdigest()
                print(code)


country = Country('countries.json')

# for i in country:
#     country.code(country.write(i[0], i[1]))


def code(way):
    with open(f'{way}', mode='r', encoding='utf8') as file:
        line = file.readline()
        while line:
            code = hashlib.md5(line.encode('utf-8')).hexdigest()
            yield code
            line = file.readline()


for i in country:
    for item in code(country.write(i[0], i[1])):
        print(item)