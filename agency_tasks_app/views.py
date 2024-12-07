from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import SpyCat
from .serializers import SpyCatSerializer, SpyCatDetailSerializer, SpySalary


class SpyCatView(ModelViewSet):
    model = SpyCat
    queryset = SpyCat.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list':
                return SpyCatSerializer
            case 'partial_update':
                return SpySalary
            case _:
                return SpyCatDetailSerializer

    # TODO: put validation to a decorator
    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'Salary must be more than 0!'}, status=400)

    def partial_update(self, request, *args, **kwargs):
        try:
            super().partial_update(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'Salary must be more than 0!'}, status=400)

    def update(self, request, *args, **kwargs):
        try:
            super().update(request, *args, **kwargs)
        except IntegrityError:
            return Response({'error': 'Salary must be more than 0!'}, status=400)
