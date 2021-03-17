import requests
import sys


url = sys.argv[1 ]

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print("Timeout Error, url:", url)
except requests.HTTPError as err:
    print("HTTP Error, url:", url)
else:
    print(response.content)

