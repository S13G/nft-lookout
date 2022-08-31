from django.apps import AppConfig


class RarenftsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rarenfts'

    def ready(self) -> None:
        import rarenfts.signals.handlers