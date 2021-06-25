from django.shortcuts import render, redirect
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic.edit import FormView

from .forms import MetadataForm, FileFieldForm, ExportFileForm
from .models import Metadata
from demo.helper_methods import create_dictionarys, process_xmls, write_csv, export_csv

import lxml.etree as etree
import os
import csv
import io

 
def home(request):
    return render(request, 'home.html', {})


class FileFieldView(FormView):
    """Uploads multiple XML files which will create a CSV file."""
    """Pulled from Django Docs: https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/#uploading-multiple-files"""

    form_class = FileFieldForm
    template_name = 'upload_multiple.html'
    success_url = reverse_lazy('metadata_list')

    def post(self, request, *args, **kwards):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('xml_files')
        studio = request.POST['studio']
        show = request.POST['show']
        if form.is_valid():
            """ TO DO:
            [1.] Check the studio's value to see which dictionary to create, e.g., 'A&E', 'Discovery', or 'Disney'
            [2.] Based on the studio, create a dictionary of the XML's data
            [3.] Append the dictionary to a list, which will be a 'list of dictionaries -> [{}, {}, {}, ... ]
            [4.] Extract column headers
            [5.] Extract row data
            [6.] Write to CSV
            [7.] Output the CSV
            8. ---
            """
            list_data = []

            for f in files:
                xml = f.read()
                xml_data = process_xmls.handle_xml(studio, xml)
                # print('\n\t xml data File Field View-------')
                # print(xml_data)
                # print('\n\t-----')
                list_data.append(xml_data)


            # EXTRACT COLUMN HEADERS TO SEND TO TEMPLATE:
            columns = write_csv.extract_columns(list_data) 

            # EXTRACT COLUMN ROWS
            row_data = write_csv.extract_row_data(list_data)

            csv_output = Metadata(studio=studio, show=show)

            csv_buffer = io.StringIO()
            csv_writer = csv.writer(csv_buffer)
            csv_writer.writerow(columns)
            for r in row_data:
                csv_writer.writerow(r)

            csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))

            filename= '_compiledXMLs_' + show + '.csv'

            csv_output.csv.save(filename, csv_file)

            list_metadata = []

            # Abstract this method and in `show_metadata()` 
            with open(csv_output.csv.path, mode='r', encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    list_metadata.append(row)

            columns = list_metadata[0]
            rows = list_metadata[1:]
            episode_count = len(rows)

            return render(request, 'csv_table.html', {
                'metadata': csv_output,
                'name': show,
                'columns': columns,
                'rows': rows,
                'studio': studio,
                'episode_count': episode_count
            })            

            # return self.form_valid(form)
        else:
            return self.form_invalid(form)
 
class ExportFileView(FormView):
    """Uploads multiple XML files which will create a CSV file."""
    """Pulled from Django Docs: https://docs.djangoproject.com/en/2.2/topics/http/file-uploads/#uploading-multiple-files"""

    form_class = ExportFileForm
    template_name = 'quick_export.html'
    success_url = reverse_lazy('metadata_list')

    def post(self, request, *args, **kwards):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('xml_files')
        studio = request.POST['studio']
        print('\n\t----STUDIO:')
        print(studio)
        print('------------------------')
        if form.is_valid():
            list_data = []

            count = 0
            for f in files:
                xml = f.read()
                xml_data = process_xmls.handle_xml(studio, xml) # Returns a dictionary of the parsed XML 
                print('\n\t xml data: ExportFileView-------')
                print(count)
                print(xml_data)
                count += 1
                print('\n\t-----')
                list_data.append(xml_data)  # Appends the returned dictionary to a list

            # EXTRACT COLUMN HEADERS TO SEND TO TEMPLATE:
            columns = write_csv.extract_columns(list_data) 

            # EXTRACT ROWS
            row_data = write_csv.extract_row_data(list_data)

            response = export_csv.export_csv(columns, row_data)

            return response
        else:
            return self.form_invalid(form)


def show_metadata(request, pk):
    if request.method == 'POST':
        metadata = Metadata.objects.get(id=pk)

        list_metadata = []
        columns = []
        rows = [] 

        print('\tMETADATA?-->', metadata)

        try:
            with open(metadata.csv.path, mode='r', encoding="utf8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    list_metadata.append(row)
        except:
            return redirect('error_page')

        columns = list_metadata[0]
        rows = list_metadata[1:]
        season_name = rows[0][0]
        studio = metadata.studio
        episode_count = len(rows)

    return render(request, 'csv_table.html', {
        'metadata': metadata,
        'name': season_name,
        'columns': columns,
        'rows': rows,
        'studio': studio,
        'episode_count': episode_count
    })


def metadata_list(request):
    context = {}
    metadata = Metadata.objects.all()

    return render(request, 'metadata_list.html', {
        'metadata': metadata
    })


def delete_metadata(request, pk):
    if request.method == 'POST':
        xml_file = Metadata.objects.get(id=pk)
        xml_file.delete()
    return redirect('metadata_list')  

def error_page(request):
    return render(request, 'error_page.html')

