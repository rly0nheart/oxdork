import os
import json
import logging
import argparse
from rich.logging import RichHandler


class Version:
    def __init__(self):
        """
        Initialize the Version class.

        Retrieves version components from the data() function and assigns them to instance variables.
        """
        self.major = data()["program"]["version"]["major"]
        self.minor = data()["program"]["version"]["minor"]
        self.patch = data()["program"]["version"]["patch"]
        self.suffix = data()["program"]["version"]["suffix"]

    def full_version(self) -> str:
        """
        Return the full version string composed of the version components.

        :return: The complete version string in the format "major.minor.patchsuffix".
        """
        return f"{self.major}.{self.minor}.{self.patch}{self.suffix}"


def data() -> dict:
    """
    Loads the program's data from data/data.json

    :return: Dictionary (JSON) containing program data
    """
    # Get the absolute path of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the data.json file
    settings_path = os.path.join(current_dir, "data", "data.json")

    # Load the settings from the file
    with open(settings_path) as file:
        program_data = json.load(file)

    return program_data


# Create parser
def create_parser():
    parser = argparse.ArgumentParser(description=f"{data()['program']['name']} v{Version().full_version()} — by" 
                                                 f" {data()['program']['developer']['name']}" 
                                                 f" ({data()['program']['developer']['about']})",
                                     epilog=data()['program']['about'])
    parser.add_argument("query", help="query string or text file containing queries")
    parser.add_argument("-c", "--count", help="number of results to show (default %(default)s).", default=10)
    parser.add_argument("-o", "--output", help="write output to specified file.")
    parser.add_argument("-v", "--version", action="version",
                        version=Version().full_version())
    return parser


logging.basicConfig(level="NOTSET", format="%(message)s",
                    handlers=[RichHandler(markup=True, log_time_format='%I:%M:%S%p', show_level=False)])
log = logging.getLogger("rich")
