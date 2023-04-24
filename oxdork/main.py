from oxdork.oxdork import *
from datetime import datetime

xprint(ascii_banner()[0])


def main():
    start_time = datetime.now()
    log.info(f"Started Oxdork {ascii_banner()[1]} at {time.asctime()}")
    try:
        check_updates()
        process_user_query(arguments.query)
    except KeyboardInterrupt as ctrlc:
        log.warning(f"User interruption detected: {ctrlc}")
    except Exception as error:
        log.error(f"An error occurred: {error}")
    finally:
        log.info(f"Finished in {datetime.now()-start_time} seconds.")
        
