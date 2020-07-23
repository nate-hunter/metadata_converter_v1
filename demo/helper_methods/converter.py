import lxml.etree as etree
import csv
import os


def test_funk(directory, studio):

    return f"DIRECTORY: {directory} || STUDIO: {studio}" 


def extract_columns(data):
    """ EXTRACTS COLUMNS TO USE IN `write_to_csv()`'s `DictWriter()` """
    columns = []

    column_headers = data[0]

    for key in column_headers:
        columns.append(key)

    return columns


def write_to_csv(filename, data):
    columns = extract_columns(data)

    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


