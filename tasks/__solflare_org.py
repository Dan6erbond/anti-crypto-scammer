import requests
from lib.exponential_runner import run_exponential
from lib.scam_logger import get_logger, get_test_logger
from lib.seed_phrase import phrase_lengths_to_strength
from mnemonic import Mnemonic

logger = get_logger(__name__.lstrip("tasks."))
root = "https://solflare.org/"
mnemo = Mnemonic("english")


@run_exponential()
def main():
    nr_requests = 0
    while True:
        # Send a POST request imitating form data
        try:
            mnemonic = mnemo.generate(strength=phrase_lengths_to_strength[12])
            r = requests.post(
                root + "api.php",
                json={
                    "accounts": [],
                    "mnemonic": mnemonic,
                    "derivationPath": "bip39",
                    "seed": mnemo.to_seed(mnemonic),
                },
                timeout=(10, 200)
            )
            nr_requests += 1
            if r.status_code == 200:
                logger.info(
                    f"[Request Nr. {nr_requests}] Successfully sent request to {root} with seed phrase: {mnemonic}")
            else:
                logger.error(
                    f"[Request Nr. {nr_requests}] Failed to send request to {root}:\n" +
                    str(r.status_code) + "\n" + r.text)
        except Exception as e:
            logger.error(f"[Request Nr. {nr_requests}] Failed to send request to {root}:\n" + str(e))
            raise e


if __name__ == "__main__":
    logger = get_test_logger(__name__)
    main(1)
