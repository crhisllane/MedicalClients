from rest_framework.viewsets import ModelViewSet
from medicos.models import Medico
from medicos.api.serializers import MedicoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication



class MedicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = MedicoSerializer
    filter_fields = ('nome', 'CRM')
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = (TokenAuthentication,)
    lookup_field = 'CRM'

    def get_queryset(self):
        return Medico.objects.all()