from rest_framework import serializers
from .models import Aquariums, TestTypes, Goals


class TestTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestTypes
        fields = ('id', 'name', 'unit')


class TestTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestTypes
        fields = ('id', 'name', 'unit')


class GoalSerializer(serializers.ModelSerializer):
    test_type = TestTypesSerializer(required=True)

    class Meta:
        model = Goals
        fields = ('id', 'test_type', 'amount')


class AquariumsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aquariums
        fields = ('id', 'name', 'volume_type', 'aquarium_type', 'length', 'height',
                  'width', 'tank_volume', 'tank_volume_real', 'visibility', 'start', 'end')
