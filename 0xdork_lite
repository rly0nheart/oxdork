#!/usr/bin/env python3

import sys
import argparse
import requests

class Dork:
	def __init__(self,args):
		self.google = f"https://www.google.com/search?q={args.query}&hl=en"
		self.api = f"https://api.hackertarget.com/pagelinks/?q={self.google}"
		self.resp = requests.get(self.api).text
		
	def on_connection(self):
		if args.output:
			self.output()
		print(self.resp + "\n")
				
	def output(self):
		with open(f"{args.output}", "w") as file:
			file.write(self.resp)		


parser = argparse.ArgumentParser(description=f"0xDork Lite: Lite version of 0xdork developed by rly0nheart. https://github.com/rlyonheart")
parser.add_argument("query", help="search query")
parser.add_argument("-o","--outfile",help="output filename",dest="output", metavar="OUTPUT FILENAME")
args = parser.parse_args()
	
if __name__ == "__main__":
	while True:
		try:
			Dork(args).on_connection()
			break
		except KeyboardInterrupt:
			sys.exit()
		except Exception as e:
			print(f"An error occured: {e}")
			print("Retrying...")
