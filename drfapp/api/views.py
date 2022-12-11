from rest_framework import viewsets
from .models import Demography
from .serializers import DemographySerializer

class DemographyViewSet(viewsets.ModelViewSet):
    queryset = Demography.objects.all()
    serializer_class = DemographySerializer