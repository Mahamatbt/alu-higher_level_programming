#!/usr/bin/env python3
import requests

# Fetch the URL
response = requests.get('https://alu-intranet.hbtn.io/status')

# Display the formatted output
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
