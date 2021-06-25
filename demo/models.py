from django.db import models

STUDIO_CHOICES = [
    ('A&E', 'A&E'),
    ('Discovery', 'Discovery'),
    ('Disney', 'Disney'),
    ('Disney2', 'Disney2'),
    ('Viacom', 'Viacom'),
]

class Metadata(models.Model):
    studio = models.CharField(max_length=100, choices=STUDIO_CHOICES)
    show = models.CharField(max_length=100, blank=True)
    xml = models.FileField(upload_to='metadata/xmls/')
    csv = models.FileField(upload_to='metadata/csvs/')

    def __str__(self):
        return self.show

    def delete(self, *args, **kwargs):
        self.csv.delete()
        super().delete(*args, **kwargs)
 