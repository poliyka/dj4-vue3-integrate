from .base import *

DEBUG = False

# DATABASES = {
#     "default": {
#         # "ENGINE": "django.db.backends.postgresql",
#         "ENGINE": "psqlextra.backend",
#         "OPTIONS": {"options": f"-c search_path={env('POSTGRES_SCHEMA')},public"},
#         "NAME": env("POSTGRES_DB"),
#         "USER": env("POSTGRES_USER"),
#         "PASSWORD": env("POSTGRES_PASSWORD"),
#         "HOST": env("POSTGRES_HOST"),
#         "PORT": env("POSTGRES_PORT"),
#     }
# }
