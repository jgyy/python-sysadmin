# python .\script_py\rand_json.py
import glob
import os
import shutil
import json
import re

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exist")
    shutil.rmtree('./processed')
    os.mkdir("./processed")
finally:
    # Get a list of recipts
    # receipts = glob.glob('./receipt/receipt-[0-9]*.json')
    receipts = [f for f in glob.iglob('./receipt/receipt-[0-9]*.json') if re.match('./receipt\\\\receipt-[0-9][02468].json', f)]
    print(receipts)
    subtotal = 0.0

    # Iterate over the receipts
    for path in receipts:
        # read content and tally a subtotal
        with open(path) as f:
            content = json.load(f)
            subtotal += float(content['value'])
        destination = path.replace('receipt', 'processed')
        print(destination)
        # mv the file to the processed directory
        shutil.move(path, destination)
        # print that we processed the file
        print("moved '%s' to '%s'" % (path, destination))

    # Print the subtotal of all processed receipts
    print("Receipt subtotal: $%s" % round(subtotal, 2))
