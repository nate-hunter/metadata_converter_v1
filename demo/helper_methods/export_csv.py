from django.http import HttpResponse

import csv


def export_csv(columns, row_data):
    """ EXPORT CSV """
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(columns)

    for row in row_data:
        writer.writerow(row)

    response['Content-Disposition'] = 'attachment; filename="_compiledXMLs_.csv"'

    return response

