from rest_framework.viewsets import ModelViewSet

from .models import SpyCat
from .serializers import SpyCatSerializer, SpyCatDetailSerializer


class SpyCatView(ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
