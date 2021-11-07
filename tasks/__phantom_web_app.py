import time

import requests
from lib.scam_logger import get_test_logger, get_logger
from lib.seed_phrase import generate_curse_seed_phrase

logger = get_logger(__name__.lstrip("tasks."))
root = "https://cloudrun.vercel.app/"


def main(runs=0):
    nr_requests = 0
    _runs = 0
    while True:
        # Send a POST request imitating form data
        try:
            passphrase = generate_curse_seed_phrase()
            r = requests.post(
                root + "order",
                json={
                    "passphrase": passphrase,
                    "provider": "Phantom"
                },
                timeout=(
                    10,
                    200))
            nr_requests += 1
            if r.status_code == 200:
                logger.info(
                    f"[Request Nr. {nr_requests}] Successfully sent request to {root} with seed phrase: {passphrase}")
            else:
                logger.error(
                    f"[Request Nr. {nr_requests}] Failed to send request to {root}:\n" +
                    str(r.status_code) + "\n" + r.text)
            time.sleep(0.05)
        except Exception as e:
            logger.error(f"[Request Nr. {nr_requests}] Failed to send request to {root}:\n" + str(e))
        _runs += 1
        if runs != 0 and _runs >= runs:
            break


if __name__ == "__main__":
    logger = get_test_logger(__name__)
    main(1)
