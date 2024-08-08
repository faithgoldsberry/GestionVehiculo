from django_filters import rest_framework as filters
from rest_framework import viewsets
from .models import Vehiculo
from .serializers import VehiculoSerializer

class VehiculoFilter(filters.FilterSet):
    vin = filters.CharFilter(lookup_expr='icontains')
    placa = filters.CharFilter(method='filter_by_placa')

    class Meta:
        model = Vehiculo
        fields = []

    def filter_by_placa(self, queryset, name, value):
        # Filtrar por placa si existe
        return queryset.filter(placas__patente__icontains=value)

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VehiculoFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        if search:
            # Primero, busca por placa
            filtered_queryset = self.filterset_class(queryset=queryset, data={'placa': search}).qs
            if filtered_queryset.exists():
                return filtered_queryset
            # Si no resulta con placa, busca por VIN
            queryset = queryset.filter(vin__icontains=search)
        return queryset
