from django.apps import AppConfig


class AuthenticacaoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticacao'

    def ready(self) -> None:
        import authenticacao.signals