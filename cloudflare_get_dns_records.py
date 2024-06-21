import json
import requests
import pprint

cloudflare_api = "https://api.cloudflare.com/client/v4/"
zone_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
api_token = "Bearer YYYYYYYYYYYYYYYYYYYYYYYYYYYY"
headers = {'Authorization': api_token, 'Content-Type':'application/json'}

cloudflare_dns = cloudflare_api + "zones/" + zone_id + "/dns_records"  
cloudflare_dns_response = requests.get(cloudflare_dns, headers=headers)

if cloudflare_dns_response.status_code == 200:
    print("Ok")
else:
    print(cloudflare_dns_response.status_code)

dns_data = json.loads(cloudflare_dns_response.text)
pprint.pprint(dns_data)
