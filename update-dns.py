from cloudflare import CloudFlare
from dotenv import load_dotenv
import os

load_dotenv()

api_email = os.getenv("EMAIL")
api_secret = os.getenv("KEY")
api_domain = os.getenv("DOMAIN")

cf = CloudFlare(api_email, api_secret, api_domain, proxied=True)
cf.headers = {
    'Authorization': f'Bearer {api_secret}',
    'X-Auth-Email': api_domain
}
cf.sync_dns_from_my_ip()
