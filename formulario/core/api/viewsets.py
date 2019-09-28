from rest_framework.viewsets import ModelViewSet
from core.models import Cliente
from core.api.serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication



class ClienteViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = ClienteSerializer
    filter_fields = ('id', 'nome', 'dataNascimento','dataColeta', 'dataEntrega', 'statusEntrega', 'CRM', 'codigoIdentificador')
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    #authentication_classes = (TokenAuthentication,)
    lookup_field = 'codigoIdentificador'

    def get_queryset(self):
        return Cliente.objects.all()





