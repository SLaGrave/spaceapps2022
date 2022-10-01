# A python script which opens the config file
# and exposes the important aspects as python variables

import logging
import json


__all__ = ["APIKEY", "LOCALDIR", "SCRIPTDIR", "TMPDIR"]

with open("./config.json", "r") as f:
    config = json.loads(f.read())

APIKEY = config.get("api_key")
LOCALDIR = config.get("local_dir")
SCRIPTDIR = config.get("script_dir")
TMPDIR = config.get("tmp_dir")

# Log info

logging.debug(f"APIKEY: {APIKEY}")
logging.debug(f"LOCALDIR: {LOCALDIR}")
logging.debug(f"SCRIPTDIR: {SCRIPTDIR}")
logging.debug(f"TMPDIR: {TMPDIR}")
