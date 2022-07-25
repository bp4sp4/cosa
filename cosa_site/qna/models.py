from django.db import models

class Qmain(models.Model):
    site_name = models.CharField(max_length=200)

    def __str__(self):
        return self.site_name
