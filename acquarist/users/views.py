from rest_framework import viewsets, mixins
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken import views
from rest_framework.response import Response
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class CreateUserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UpdateUserViewSet(generics.UpdateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)

    def get_object(self):
        return self.request.user


user_create = CreateUserViewSet.as_view()
user_update = UpdateUserViewSet.as_view()
