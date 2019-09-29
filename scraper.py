from selectorlib import Extractor
import requests
import json
import argparse

# argparser = argparse.ArgumentParser()
# argparser.add_argument('url', help='Amazon Product Details URL')

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selector.yml')
cookies = {'enwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

# Download the page using requests
# args = argparser.parse_args()
# for i in range(10):
r = requests.get("https://www.amazon.com/dp/B07QCYVXXX",
                headers=headers, cookies=cookies)
# Pass the HTML of the page and create
# html = r.text
# index = html.find('"'+"priceblock_ourprice"+'"')

# price = ""
# while html[index] != '<':
#     if(html[index] == ">"):
#         index += 1
#         while html[index] != '<':
#             price += html[index]
#             index += 1
#     else:
#         print(html[index])
#         index += 1


data = e.extract(r.text)
# Print the data
print(json.dumps(data, indent=True),end="")
# print(price)
