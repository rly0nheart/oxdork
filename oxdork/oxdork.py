import os
import json
from googlesearch import search
from rich import print as xprint
from urllib.request import urlopen
from oxdork.config import log, Version

version = Version()


def process_input(user_input) -> list:
    """
    Processes user input. If input is a file, opens the file and reads the contents, line by line.
    If not, use the input as it is

    :param user_input: user input
    :return: A list of the processed queries/query
    """
    if os.path.isfile(user_input):
        with open(user_input, 'r') as file:
            log.info(f"Loaded queries from file: {file.name}")
            queries = file.readlines()
            queries = [query.strip() for query in queries]
            return queries
    else:
        return [user_input]


def begin_search(query, count, output) -> None:
    """
    Start search with the processed input

    :param query: Search query
    :param count: Number of results to return (defaults to 10)
    :param output: String representing a file to which results will be written
    :return: None
    """
    number = 0
    log.info(f"Fetching {count} results for `{query}`...")
    for counter, result in enumerate(search(query, num=int(count), start=0, stop=None,
                                            lang="en", tld="com", pause=2.5), start=1):
        number += 1
        log.info(f"{counter}. {result}")

        # Start writing results to a file
        # if user passes the filename to -o/--output
        if output:
            __write_output(result, counter, output)

        # If result number is greate than or equal to
        # the user specified count limit. Break the search loop. 
        if number >= int(count):
            break


def __write_output(result: str, counter: int, filename: str) -> None:
    """
    Write a result to a file.

    :param result: The result to write.
    :type result: str
    :param counter: The index of the result.
    :type counter: int
    :param filename: The name of the output file (without extension).
    :type filename: str
    :return: None
    """
    with open(f"{filename}.txt", "a") as file:
        file.write(f"{counter}. {result}\n")


def check_updates() -> None:
    """
    Checks for latest updates by retrieving the release tag from the releases page of the program from GitHub
    Then compares the remote version tag with the tag in the program.
    If they match, program assumes it's up-to-date.
    If not, print a message notifying the user about the remote version (which is treated as the official new release)
    , and lastly prints the release notes of the presumed new release.

    :return: None
    """
    with urlopen("https://api.github.com/repos/rly0nheart/oxdork/releases/latest") as response:
        release_data = json.loads(response.read().decode())
        if release_data['tag_name'] != version.full_version():
            xprint(f"* A new release of `OxDork` is available ({release_data['tag_name']}).\n")
        else:
            pass
