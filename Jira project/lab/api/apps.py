from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals