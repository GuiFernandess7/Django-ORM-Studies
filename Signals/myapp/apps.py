from django.apps import AppConfig
from django.db.models.signals import post_save

def example_receiver(sender, **kwargs):
    print("Intance is saved")

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self) -> None:
        import myapp.signals
        
