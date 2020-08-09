from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView

from acquarist.authentication.views import ObtainAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/sessions/', ObtainAuthToken.as_view()),
    path('api/v1/users/', include('acquarist.users.urls')),
    path('auth/forgot-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
