from django.db import models
from django.conf import settings
from django.utils import timezone

class Medico(models.Model):
    
    CRM                  = models.CharField('CRM', max_length=10, unique=True)
    nome                 = models.CharField('Nome', max_length=80, null=False)

    def __str__(self):
        return self.CRM

