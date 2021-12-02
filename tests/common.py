from os import path, getcwd


def fixture_path(day, filename):
    return path.join(getcwd(), 'tests', day, 'fixtures', filename)
