from rest_framework.serializers import ModelSerializer
from rest_framework import fields, serializers
from core.models import Cliente



class ClienteSerializer(ModelSerializer):
    dataNascimento = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y'])
    dataColeta = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y'])
    dataEntrega = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y'])

    class Meta:
        model = Cliente
        fields = ['id', 
                  'nome', 
                  'dataNascimento',
                  'dataColeta', 
                  'dataEntrega', 
                  'dataCadastro', 
                  'codigoIdentificador',
                  'CRM'
                ]