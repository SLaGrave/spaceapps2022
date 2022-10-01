# A python script which opens the config file
# and exposes the important aspects as python variables

import logging
import json
import os


__all__ = ["APIKEY", "LOCALDIR", "SCRIPTDIR", "TMPDIR"]

with open("./config.json", "r") as f:
    config = json.loads(f.read())

APIKEY = config.get("api_key")
LOCALDIR = config.get("local_dir")
SCRIPTDIR = config.get("script_dir")
TMPDIR = config.get("tmp_dir")

# Ensure dirs exist
os.makedirs(LOCALDIR, exist_ok=True)
os.makedirs(SCRIPTDIR, exist_ok=True)
os.makedirs(TMPDIR, exist_ok=True)

# Log info
logging.debug(f"APIKEY: {APIKEY}")
logging.debug(f"LOCALDIR: {LOCALDIR}")
logging.debug(f"SCRIPTDIR: {SCRIPTDIR}")
logging.debug(f"TMPDIR: {TMPDIR}")
