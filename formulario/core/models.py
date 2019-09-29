from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from medicos.models import Medico
import uuid

class Cliente(models.Model):
    
   nome                 = models.CharField('Nome', max_length=80, null=False)
   dataNascimento       = models.DateField('Data de Nascimento')
   dataColeta           = models.DateField('Data da Coleta')
   dataEntrega          = models.DateField('Data da Entrega')
   CRM                  = models.ForeignKey(Medico, related_name='clientes', blank=True, on_delete=models.CASCADE)
   codigoIdentificador  = models.CharField(max_length=100, null=False, unique=True, default=uuid.uuid1)
   dataCadastro         = models.DateTimeField(auto_now_add=True)

   def data_Cadastro (self):
      self.cadastro = timezone.now()
      self.save()

   def __str__(self):
      return self.nome


  
