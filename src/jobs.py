import csv


def read(path):
    with open(path) as file:
        result_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        lista = []
        for job in result_jobs:
            lista.append(job)
        return lista
