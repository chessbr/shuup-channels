# Shuup Channels

Enables the power of WebSockets with [Django Channels](https://github.com/django/channels) in [Shuup Ecommerce Platform](https://github.com/shuup/shuup).

This project allows more advanced customizations and addons to be created with Shuup. By using websockets, a new set of solutions can be created and making user experience even better.

To use websocket on your Shuup projects, start by installing Shuup Channels ``pip install shuup-channels`` and add `shuup_channels` to your `INSTALLED_APPS` settings. Check [`workbench_project`](./workbench_project/app) for an example of project and configuration.

## Usage
This project simply defines an ASGI applicaton with a websocket router which loads urls through Shuup Provides.

After the installation, define a provide entry using the `channels_urls` key:

in your `my_addon/apps.py`
```
class AppConfig(shuup.apps.AppConfig):
    provides = {
        "channels_urls": [
            "my_addon.urls:channels_urls"
        ]
    }
```

in your `my_addon/urls.py`
```
from django.conf.urls import url
from my_addon.consumers import MyConsumer
channels_urls = [
    url(r"^ws/myaddon/$", MyConsumer)
]
```

Done, implement your `MyConsumer` following the Django Channels guidelines and you should be safe. The websocket url will be available as `ws://your-site-url/ws/myaddon/`.

## Example of projects

- [Shuup Admin Channel](https://github.com/chessbr/shuup-admin-channel) - Adds a generic and extendable channel to Admin module

# Copyright

Copyright (C) 2019 by Christian Hess

# License

MIT
