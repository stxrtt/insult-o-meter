"""Deprecated: Use the .env file and PI_API_KEY instead.

This module is kept for backward compatibility. Prefer setting PI_API_KEY in a .env file.
"""

import os

apikey = os.getenv("PI_API_KEY", "")