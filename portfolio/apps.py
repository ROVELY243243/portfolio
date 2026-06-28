from django.apps import AppConfig

class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'

    # Cette fonction active l'écoute des signaux au lancement de Django
    def ready(self):
        import portfolio.signals
