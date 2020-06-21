import os
import sys
import requests
from argparse import ArgumentParser

os.environ["OWM_API_KEY"] = "9f19a663058fc3d29c0c775db61c70bf"
parser = ArgumentParser(description='Get the current weather information')
parser.add_argument('city', help='city name to get the weather for')
parser.add_argument('--country', default='sg', help='country zip/postal belongs to, default is "us"')

args = parser.parse_args()

url = "http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s" % (
    args.city,
    args.country,
    os.getenv("OWM_API_KEY")
)

res = requests.get(url)
print(url)

if res.status_code != 200:
    print("Error talking to weather provider: %s" % res.status_code)
    sys.exit(1)

print(res.json())
