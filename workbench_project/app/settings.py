# -*- coding: utf-8 -*-
from shuup_workbench.settings import *  # noqa

INSTALLED_APPS = list(INSTALLED_APPS) + [   # noqa
    'channels',
    'shuup_channels',
    'shuup_admin_channel',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'shuup_channels.sqlite3'
    }
}

ASGI_APPLICATION = "shuup_channels.routing.application"

# For development and tests purposes, use InMemoryChannelLayer
# Make sure to use Redis os other backend on production
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}
