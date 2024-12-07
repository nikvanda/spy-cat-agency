from rest_framework import serializers

from .models import SpyCat


class SpyCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        exclude = ['id']
