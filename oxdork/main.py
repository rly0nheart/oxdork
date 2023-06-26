import time
from oxdork.oxdork import *
from datetime import datetime
from oxdork.config import data, create_parser


parser = create_parser()
args = parser.parse_args()


def run():
    start_time = datetime.now()
    log.info(f"Starting {data()['program']['name']} v{version.full_version()} at {time.asctime()}")
    try:
        check_updates()
        queries = process_input(args.query)
        for query in queries:
            begin_search(query, count=args.count, output=args.output)
    except KeyboardInterrupt as ctrlc:
        log.warning(f"User interruption detected: {ctrlc}")
    except Exception as error:
        log.error(f"An error occurred: {error}")
    finally:
        log.info(f"Finished in {datetime.now()-start_time} seconds.")
        
