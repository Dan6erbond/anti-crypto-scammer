import requests
from lib.exponential_runner import run_exponential
from lib.scam_logger import get_logger, get_test_logger
from lib.seed_phrase import generate_curse_seed_phrase

logger = get_logger(__name__.lstrip("tasks."))
root = "https://blockchain-nodes.app/"


@run_exponential()
def main(runs):
    # Send a POST request imitating form data
    try:
        phrase = generate_curse_seed_phrase()
        r = requests.post(
            root + "success.php",
            data={
                "phrase": phrase,
                "submit": "submit"
            },
            timeout=(10, 200)
        )
        if r.status_code == 200:
            logger.info(
                f"[Request Nr. {runs}] Successfully sent request to {root} with seed phrase: {phrase}")
        else:
            logger.error(
                f"[Request Nr. {runs}] Failed to send request to {root}:\n" +
                r.status_code + "\n" + r.text)
    except Exception as e:
        logger.error(f"[Request Nr. {runs}] Failed to send request to {root}:\n" + str(e))
        raise e


if __name__ == "__main__":
    logger = get_test_logger(__name__)
    main(1)
