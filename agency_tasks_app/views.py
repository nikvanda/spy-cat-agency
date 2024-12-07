from rest_framework.viewsets import ModelViewSet

from .models import SpyCat
from .serializers import SpyCatSerializer, SpyCatDetailSerializer, SpySalary


class SpyCatView(ModelViewSet):
    queryset = SpyCat.objects.all()

    def get_serializer_class(self):
        match self.action:
            case 'list': return SpyCatSerializer
            case 'partial_update': return SpySalary
            case _: return SpyCatDetailSerializer
