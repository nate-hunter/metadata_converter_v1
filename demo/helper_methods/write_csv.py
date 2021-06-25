import lxml.etree as etree
import csv
import os

def extract_columns(data):
    """ EXTRACTS COLUMNS TO USE IN `write_to_csv()`'s `DictWriter()` """
    columns = []

    column_headers = data[0]

    for key in column_headers:
        columns.append(key)

    return columns

def extract_row_data(data):
    """ EXTRACTS ROW DATA TO USE IN THE TABLE IN THE 'HOME' TEMPLATE"""
    row_data = []
    print('\n\t------Incoming data:')
    print(data)
    print('\n\t--------')
    

    for row_dict in data:
        row_array = []
        # count = 0
        for row in row_dict.values():
            # print(f'row {count}:  {row}')
            # count = count + 1
            row_array.append(row)
        
        row_data.append(row_array)
    return row_data


def write_to_csv(filename, data):
    columns = extract_columns(data)
    
    # WORK ON SORTING ITEMS, here in process dictionary functions?
    # for d in data:
        # print('\t----', d)
        
    # print("---------------------------------------")
    # newD = sorted(data, key = lambda k: k['container_position'])

    with open(filename, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=columns)
        writer.writeheader()

        for row in newD:
            writer.writerow(row)