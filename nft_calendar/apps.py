from django.apps import AppConfig


class NftCalendarConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "nft_calendar"

    def ready(self) -> None:
        import nft_calendar.signals.handlers