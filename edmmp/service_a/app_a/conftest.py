# Copyright 2021 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from util.settings_for_tests import configure_settings

configure_settings(["service_a.app_a"], "service_a.app_a.urls")
