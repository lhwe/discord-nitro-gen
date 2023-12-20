import threading
from itertools import cycle
import requests
def get_discord_link(api_url, payload, proxies, output_file):
    try:
        proxy = next(proxies)
        session = requests.Session()
        response = session.post(api_url, json=payload, proxies={'http': proxy, 'https': proxy}, verify=False)
        if response.status_code == 200:
            token = response.json().get('token')
            promo_link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{token}"
            print(f"Generated promo link: {promo_link}")
            with open(output_file, 'a') as file:
                file.write(f"{promo_link}\n")
        else:
            print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
proxy_file = 'proxys.txt'
output_file = 'good_links.txt'
api_url = 'https://api.discord.gx.games/v1/direct-fulfillment'
payload = {"partnerUserId": "3ea453deb97178555843a6c1f1be932114a331833e84f1651e6ee6b45ecbbc39"}
with open(proxy_file, 'r') as file:
    proxies_list = [line.strip() for line in file]
proxy_cycle = cycle(proxies_list)
num_threads = 5000
threads = []
for i in range(num_threads):
    thread = threading.Thread(target=get_discord_link, args=(api_url, payload, proxy_cycle, output_file))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
