from django.apps import AppConfig


class CoutureconnectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coutureconnect'

    # def ready(self):
    #     import coutureconnect.signals
