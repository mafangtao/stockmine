#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""logs.py - logging variables for how stockflight displays logs.

See README.md or https://github.com/nicholasadamou/stockflight
for more information.

Copyright (C) Nicholas Adamou 2019
stockflight is released under the Apache 2.0 license. See
LICENSE for the full license text.
"""

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

WARNING = "[%s!%s]" % (YELLOW, RESET)
ERROR = "[%sX%s]" % (RED, RESET)
OK = "[%s+%s]" % (GREEN, RESET)
SUCCESS = "[%s✔%s]" % (GREEN, RESET)
