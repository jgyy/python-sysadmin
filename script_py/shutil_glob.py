import glob
import os
import shutil
import json

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exist")

# Get a list of recipts
receipts = glob.glob('./receipt/receipt-[0-9]*.json')

subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('\\')[-1]
    destination = "./processed/%s" % name
    print(destination)
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path, destination))

print("Receipt subtotal: $%.2f" % subtotal)

# Iterate over the receipts
# read content and tally a subtotal
# mv the file to the processed directory
# print that we processed the file

# Print the subtotal of all processed receipts
