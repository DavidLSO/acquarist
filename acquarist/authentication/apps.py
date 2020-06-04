from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuthenticationConfig(AppConfig):
    name = 'acquarist.authentication'
    verbose_name = _('authentication')

    def ready(self):
        import acquarist.authentication.signals  # noqa
