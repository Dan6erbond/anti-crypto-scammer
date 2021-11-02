import requests
import time

from lib.seed_phrase import generate_curse_seed_phrase


root = "https://blockchain-nodes.app/"

nr_requests = 0
while True:
    # Send a POST request imitating form data
    r = requests.post(root + "success.php", data={"phrase": generate_curse_seed_phrase()})
    nr_requests += 1
    if r.status_code == 200:
        print(f"[Request Nr. {nr_requests}] Successfully sent request to blockchain-nodes.app.")
    else:
        print(f"[Request Nr. {nr_requests}] Failed to send request to blockchain-nodes.app:")
        print(r.status_code)
        print(r.text)
    time.sleep(0.05)
