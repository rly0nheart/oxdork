#!/usr/bin/env python3

from core.__main__ import *
from assets.colors import red, white, green, end

parser = argparse.ArgumentParser(description=f"{red}0x{white}Dork{red}: Google dorking tool developed by {white}rly0nheart{red}. https://github.com/rlyonheart{end}")
parser.add_argument("query", help="search query")
parser.add_argument("-c","--count",help="number of results to show (default is 50)",dest="count", metavar="RESULTS COUNT", default=50)
parser.add_argument("-o","--outfile",help="output filename",dest="output", metavar="OUTPUT FILENAME")
args = parser.parse_args()

if __name__ == "__main__":
	logging.info(f"{white}Connecting to google[{green}{args.query}{white}]...{end}")
	while True:
		try:
			Dork(args).on_connect()			
		except KeyboardInterrupt:
			sys.exit()					
		except Exception as e:
			logging.info(f"{white}Error: {red}{e}{end}")
			logging.info(f"{white}Reconnecting...{end}")

			
		
