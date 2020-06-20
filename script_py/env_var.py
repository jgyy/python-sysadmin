import os

staging = input("STAGE=")
os.environ["STAGE"] = staging
stage = (os.getenv("STAGE") or "development").upper()

output = "We're running in %s" % stage

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
