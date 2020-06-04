from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from acquarist.users.views import UserViewSet, UserCreateViewSet
from acquarist.aquariums import views
from acquarist.authentication.views import ObtainAuthToken

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)
router.register(r'aquariums', views.AquariumsViewSet, basename='aquariums')
router.register(r'aquarium-types', views.AquariumTypesViewSet, basename='aquariums_types')
router.register(r'volume-types', views.VolumeTypeViewSet, basename='volume_types')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('auth/sessions/', ObtainAuthToken.as_view()),
    path('auth/forgot-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
