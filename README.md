# CloudFlare DDNS using Python

How to use:
1. Create API Key [here](https://dash.cloudflare.com/profile/api-tokens) with Edit DNS permissions
2. Install prerequisites by running `python -m pip install -r requirements.txt` in this directory
3. Create `.env` file in the same directory as `update-dns.py` with the email address, API key and domain name associated with your CloudFlare account
4. Run `python update-dns.py`

**Please Note: `cloudflare.py` code from `cloudflare-ddns` Python library**
