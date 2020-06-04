import json
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import AquariumsSerializer
from .models import Aquariums


class AquariumsViewSet(viewsets.ViewSet):

    def list(self, request):
        user = request.user
        queryset = user.aquariums.all()
        serializer = AquariumsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = AquariumsSerializer(data=request.data.get('data'))
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = request.user
        aquarium = user.aquariums.get(pk=pk)
        serializer = AquariumsSerializer(aquarium, many=False)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = request.user
        aquarium = user.aquariums.get(pk=pk)
        serializer = AquariumsSerializer(aquarium, data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        user = request.user
        aquarium = user.aquariums.get(pk=pk)
        serializer = AquariumsSerializer(aquarium, data=request.data, partial=True, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = request.user
        user.aquariums.filter(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AquariumTypesViewSet(viewsets.ViewSet):
    def list(self, request):
        aquarium_types_formated = []

        for value, label in Aquariums.AQUARIUM_TYPE_CHOICES:
            aquarium_types_formated.append({
                'value': value,
                'label': label
            })

        return Response(aquarium_types_formated)


class VolumeTypeViewSet(viewsets.ViewSet):
    def list(self, request):
        volume_type_formated = []

        for value, label in Aquariums.VOLUME_TYPE_CHOICES:
            volume_type_formated.append({
                'value': value,
                'label': label
            })

        return Response(volume_type_formated)
