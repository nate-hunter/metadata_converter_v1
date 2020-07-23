from django import forms

from .models import Metadata, STUDIO_CHOICES


class MetadataForm(forms.ModelForm):
    class Meta:
        model = Metadata
        fields = ('studio', 'show', 'xml')
        file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class FileFieldForm(forms.Form):
    studio = forms.CharField(
        max_length=100,
        widget=forms.Select(choices=STUDIO_CHOICES),
    )    
    show = forms.CharField(max_length=100)
    xml_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class ExportFileForm(forms.Form):
    studio = forms.CharField(
        max_length=100,
        widget=forms.Select(choices=STUDIO_CHOICES),
    )   
    xml_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    


