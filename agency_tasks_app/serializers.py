from rest_framework import serializers

from .models import SpyCat


class SpyCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        exclude = ('id', 'breed', 'salary')


class SpyCatDetailSerializer(SpyCatSerializer):

    class Meta(SpyCatSerializer.Meta):
        exclude = ('id', )
