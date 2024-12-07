from rest_framework import serializers

from .models import SpyCat, Mission, Target


class SpyCatSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpyCat
        exclude = ('id', 'breed', 'salary')


class SpyCatDetailSerializer(SpyCatSerializer):

    class Meta(SpyCatSerializer.Meta):
        exclude = ('id', )


class SpySalary(SpyCatSerializer):

    class Meta:
        model = SpyCat
        fields = ('salary',)


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        exclude = ('id', )


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        exclude = ('id', )
