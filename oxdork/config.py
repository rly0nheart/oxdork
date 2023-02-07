import argparse
from oxdork.banner import version_tag


def create_parser():
    parser = argparse.ArgumentParser(description="Google dorking tool — by Richard Mwewa | https://about.me/rly0nheart",
                                     epilog="oxDork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers.")
    parser.add_argument("query", help="dork query.")
    parser.add_argument("-n", "--count", help="number of results to show (default %(default)s).", default=10)
    parser.add_argument("-c", "--colors", "--colours", help="enable colo[u]rs", action="store_true")
    parser.add_argument("-w", "--output", help="write output to specified file.")
    parser.add_argument("-V", "--version", action="version",
                        version=version_tag)
    return parser


_parser = create_parser()
args = _parser.parse_args()

if args.colors:
    RED = "[red]"
    WHITE = "[white]"
    GREEN = "[green]"
    RESET = "[/]"
else:
    RED = ""
    WHITE = ""
    GREEN = ""
    RESET = ""
