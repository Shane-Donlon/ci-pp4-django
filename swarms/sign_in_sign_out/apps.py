from django.apps import AppConfig
from django.db.models.signals import post_save

class SignInSignOutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sign_in_sign_out'
    
    def ready(self):
        from .signals import create_profile
        from django.contrib.auth.models import User
        post_save.connect(create_profile, sender=User)
        from .signals import update_profile
        post_save.connect(update_profile, sender=User)