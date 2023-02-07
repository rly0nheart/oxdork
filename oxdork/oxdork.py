import logging
import requests
import argparse
from datetime import datetime
from googlesearch import search
from rich import print as xprint
from rich.logging import RichHandler
from oxdork.banner import version_tag, ascii_banner
from oxdork.config import args, RED, WHITE, GREEN, RESET

logging.basicConfig(level="NOTSET", format="%(message)s",
                    handlers=[RichHandler(markup=True, log_time_format='[%H:%M:%S%p]', show_level=False)])
log = logging.getLogger("rich")


def dork():
    check_updates()
    number = 0
    log.info(f"Fetching {args.count} dork results...")
    for counter, results in enumerate(search(args.query, num=int(args.count), start=0, stop=None, lang="en", tld="com", pause=2.5), start=1):
        number += 1
        log.info(f"{counter}. {results}")

        if args.output:
            output(results, counter)

        if number >= int(args.count):
            break


def output(results, counter):
    with open(args.output, "a") as file:
        file.write(f"[{counter}] {results}\n")
        file.close()


def check_updates():
    response = requests.get("https://api.github.com/repos/rly0nheart/oxdork/releases/latest").json()
    if response['tag_name'] == version_tag:
        pass
    else:
        log.info(f"A new release of oxDork is available ({response['tag_name']})")
        xprint(f"\n{response['body']}\n")
        log.info("Run 'pip install --upgrade oxdork' to get the updates.\n")
