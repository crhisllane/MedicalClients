from rest_framework.serializers import ModelSerializer
from core.models import Cliente
from medicos.api.serializers import MedicoSerializer



class ClienteSerializer(ModelSerializer):
    CRM = MedicoSerializer(many=False)

    class Meta:
        model = Cliente
        fields = ['id', 
                  'nome', 
                  'dataNascimento',
                  'dataColeta', 
                  'dataEntrega', 
                  'statusEntrega', 
                  'codigoIdentificador',
                  'CRM'
                ]


