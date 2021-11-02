import requests
import time
import logging

from lib.seed_phrase import generate_curse_seed_phrase


root = "https://blockchain-nodes.app/"


def main():
    nr_requests = 0
    while True:
        # Send a POST request imitating form data
        try:
            r = requests.post(
                root + "success.php",
                data={
                    "phrase": generate_curse_seed_phrase(),
                    "submit": "submit"},
                timeout=(
                    10,
                    200))
            nr_requests += 1
            if r.status_code == 200:
                logging.info(f"[Request Nr. {nr_requests}] Successfully sent request to blockchain-nodes.app.")
            else:
                logging.error(
                    f"[Request Nr. {nr_requests}] Failed to send request to blockchain-nodes.app:\n" +
                    r.status_code + "\n" + r.text)
            time.sleep(0.05)
        except Exception as e:
            logging.error(f"[Request Nr. {nr_requests}] Failed to send request to blockchain-nodes.app:\n" + e)
