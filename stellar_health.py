import logging

import log_cleaner

def main():
    log_cleaner.run()

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(format='%(asctime)s %(message)s',filename='stellar.log', level=logging.INFO)

    main()