from django.urls import path, include
from . import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name="upload"),

    path('xml/upload/', views.FileFieldView.as_view(), name="upload_xmls"),
    path('metadata/export/', views.ExportFileView.as_view(), name="export_metadata"),

    path('metadata/', views.metadata_list, name='metadata_list'),
    path('metadata/<int:pk>', views.show_metadata, name='show_metadata'),
    path('metatdata/upload/', views.upload_metadata, name='upload_metadata'),
    path('metadata/<int:pk>/', views.delete_metadata, name="delete_metadata"),
    path('metadata/test/<int:pk>/', views.test_xml, name="test_xml"),

]

# For Development purposes, not to be used in Production -- why? why not? How to upload file(s) in prodcution?
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


