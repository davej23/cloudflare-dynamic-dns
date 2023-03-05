# CloudFlare DDNS using Python

How to use:
1. Create API Key [here](https://dash.cloudflare.com/profile/api-tokens) with Edit DNS permissions
2. Install prerequisites by running `python -m pip install -r requirements.txt` in this directory
3. Create `.env` file in the same directory as `update-dns.py` with the email address, API key and domain name associated with your CloudFlare account (see `.env.template` for correct format)
4. Run `python update-dns.py`

(Optional) To run this command every hour on a Linux system
1. Run `crontab -e` on Linux system
2. Enter this line at the end of the file `0 * * * * python3 PATH_TO_UPDATE_DNS_SCRIPT`
3. If required, delete root user mail everyday using `0 0 * * *  cat /dev/null > /var/spool/mail/root 2>&1 > mailroot.log`

**Please Note: `cloudflare.py` code from `cloudflare-ddns` Python library**
