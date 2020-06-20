# $Env:STAGE = "PROD"; python .\script_py\env_var.py
import os

stage = (os.getenv("STAGE") or "development").upper()

output = "We're running in %s" % stage

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
