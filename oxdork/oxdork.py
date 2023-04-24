import os
import time
import requests
from datetime import datetime
from rich.prompt import Prompt
from googlesearch import search
from rich import print as xprint
from oxdork.banner import ascii_banner
from oxdork.config import log, arguments


# Process user input
# If input is a file, open it and loop through each line and use it as a query.
# in the start_search_with_query function
# If input is a string, call start_search_with_query
def process_user_query(query):
    if os.path.isfile(query):
        with open(query, 'r') as file:
            log.info(f"Loaded queries from file: {file.name}")
            for count, line in enumerate(file, start=1):
                log.info(f"Current query: {count}. {line}")
                start_search_with_query(query=line, count=arguments.count, output=arguments.output)
    else:
        start_search_with_query(query=query, count=arguments.count, output=arguments.output)


# Start search with the query from the process_query function
def start_search_with_query(query, count, output):
    number = 0
    log.info(f"Fetching {count} results for {query}...")
    for counter, result in enumerate(search(query, num=int(count), start=0, stop=None, lang="en", tld="com", pause=2.5), start=1):
        number += 1
        log.info(f"{counter}. {result}")

        # Start writting results to a file
        # if user passes the filename to -o/--output
        if output:
            write_output(result, counter, output)

        # If result number is greate than or equal to
        # the user specified count limit. Break the search loop. 
        if number >= int(count):
            break


# Write results to a file
def write_output(result, counter, output):
    with open(f"{output}.txt", "a") as file:
        file.write(f"{counter}. {result}\n")
        file.close()


# Check program updates
def check_updates():
    response = requests.get("https://api.github.com/repos/rly0nheart/oxdork/releases/latest").json()
    if response['tag_name'] == ascii_banner()[1]:
        pass
    else:
        log.info(f"A new release is available: oxDork {response['tag_name']}")
        xprint(f"\n{response['body']}\n")
        log.info("Run 'pip install --upgrade oxdork' to get the updates.\n")
