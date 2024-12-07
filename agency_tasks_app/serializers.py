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


class RelatedTargetSerializer(TargetSerializer):
    class Meta(TargetSerializer.Meta):
        exclude = ('id', 'mission')


class MissionSerializer(serializers.ModelSerializer):
    targets = RelatedTargetSerializer(many=True, required=False)

    def validate_empty_values(self, data):
        return True, data

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        cat = SpyCat.objects.get(id=validated_data.pop('spy_cat'))
        mission = Mission.objects.create(**validated_data, spy_cat=cat)
        targets = [Target.objects.create(**data, mission=mission) for data in targets_data]
        if len(targets) > 3:
            raise ValueError('3 targets is maximum')
        for target in targets:
            target.save()
        return mission

    class Meta:
        model = Mission
        exclude = ('id', )
