#!/usr/bin/env python3

from oxdork.oxdork import *
from datetime import datetime

xprint(ascii_banner())


def main():
    start_time = datetime.now()
    try:
        dork()
    except KeyboardInterrupt as ctrlc:
        raise KeyboardInterrupt("User interruption detected.") from ctrlc
    except Exception as error:
        raise Exception("An error occurred") from error
    finally:
        log.info(f"Stopped in {datetime.now()-start_time} seconds.")
