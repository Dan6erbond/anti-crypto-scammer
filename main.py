import importlib
import logging
import os
import threading

logging.basicConfig(filename="log.txt", encoding="utf-8", format="%(asctime)s %(message)s", level=logging.INFO)


def main():
    for file in os.listdir("tasks"):
        if file.endswith(".py") and not file.startswith("__"):
            module = importlib.import_module("tasks." + file[:-3])
            print("Starting task: " + file[:-3])
            logging.info("Starting task: " + file[:-3])
            threading.Thread(target=module.main).start()


if __name__ == "__main__":
    main()
