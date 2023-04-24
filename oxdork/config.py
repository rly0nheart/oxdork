import logging
import argparse
from rich.logging import RichHandler
from oxdork.banner import ascii_banner


# Create parser
def create_parser():
    parser = argparse.ArgumentParser(description="Google dorking tool — by Richard Mwewa (https://about.me/rly0nheart)",
                                     epilog="oxDork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers.")
    parser.add_argument("query", help="query string or text file containing queries")
    parser.add_argument("-c", "--count", help="number of results to show (default %(default)s).", default=10)
    parser.add_argument("-o", "--output", help="write output to specified file.")
    parser.add_argument("-v", "--version", action="version",
                        version=ascii_banner()[1])
    return parser


# Parse command line arguments
parser = create_parser()
arguments = parser.parse_args()

# Configure logging
logging.basicConfig(level="NOTSET", format="%(message)s",
                    handlers=[RichHandler(markup=True, log_time_format='[%I:%M:%S%p]', show_level=False)])
log = logging.getLogger("rich")
