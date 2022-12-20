import requests

api = "https://public-dns.info/nameserver/ua.json"

response = requests.get(api)
response.raise_for_status()
result = response.json()

# print(len(result))

filtered = filter(lambda i: i['reliability'] ==
                  1 and i['city'] == 'Lviv', result)
sorted_ = sorted(filtered, key=lambda el: el['as_org'])
for e in sorted_:
    print(f"{e['ip']}, {e['as_org']}")
