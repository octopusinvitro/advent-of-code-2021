from os import path, getcwd


def fixture_path(day, filename):
    return path.join(getcwd(), 'tests', day, 'fixtures', filename)


def data_path(day):
    return path.join(getcwd(), 'data', day + '_input')
