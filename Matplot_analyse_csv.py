from matplotlib import pyplot as pyplot
import csv
import numpy as np


with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    row = next(csv_reader)
    print(row)
    