import json
import requests
import pprint
from datetime import datetime

today = datetime.now()
datetimenow = today.strftime('%Y-%m-%d-%H%M%S')
zone_name= "domainname.com"
export_filename = "./cision_cloudflare_dns_records-export-"+zone_name+"-"+datetimenow+".json"

cloudflare_api = "https://api.cloudflare.com/client/v4/"

zone_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
api_token = "Bearer YYYYYYYYYYYYYYYYYYYYYYYYYYYY"
headers = {'Authorization': api_token, 'Content-Type':'application/json'}

cloudflare_dns = cloudflare_api + "zones/" + zone_id + "/dns_records"
cloudflare_dns_response = requests.get(cloudflare_dns, headers=headers)

if cloudflare_dns_response.status_code == 200:
    dns_data = json.loads(cloudflare_dns_response.text)
    pprint.pprint(dns_data)

    with open(export_filename, 'w') as json_file:
        json.dump(dns_data, json_file, indent=1)
else:
    print(cloudflare_dns_response.status_code)
