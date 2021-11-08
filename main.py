import importlib
import logging
import os
import threading


def main():
    for file in os.listdir("tasks"):
        if file.endswith(".py") and not file.startswith("__"):
            module = importlib.import_module("tasks." + file[:-3])
            if hasattr(module, "main"):
                print("Starting task: " + file[:-3])
                logging.info("Starting task: " + file[:-3])
                threading.Thread(target=module.main).start()
            else:
                print(f"main() not found in {file[:-3]}, skipping...")


if __name__ == "__main__":
    main()
