# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import os
from tempfile import mkdtemp

from django.conf import settings


def configure_settings(apps: list[str], url_module: str) -> None:
    """Minimal settings for unittests."""
    # import pdb
    # urlconf = f"{apps[0]}.urls"
    # pdb.set_trace()
    settings.configure(
        TIME_ZONE="UTC",
        USE_TZ=True,
        INSTALLED_APPS=apps,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(
                    mkdtemp(),
                    f"test{os.environ.get('PANTS_EXECUTION_SLOT', '')}.sqlite3",
                ),
            }
        },
        ROOT_URLCONF=url_module,
    )
