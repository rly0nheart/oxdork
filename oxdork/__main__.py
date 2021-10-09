#!/usr/bin/env python3

import sys
import time
import random
import argparse
from tqdm import tqdm
from lib.banner import banner
from datetime import datetime
from googlesearch import search
from lib.headers import user_agents
from lib.colors import red,white,yellow,green,end


class oxdork:
	def __init__(self,args):
		self.start = datetime.now()
			    		
	def on_connect(self):
	    number = 0
	    counter = 0
	    while True:
	    	try:
	    		google_search = search(args.query, num=int(args.count),start=0,stop=None,lang="en",
	    		tld="com", pause=2.5,
	    		user_agent=f"{random.choice(user_agents)}")
	    		
	    		for result in tqdm(google_search):
	    		  counter+=1
	    		  print(f"{white}[{counter}] oxdork:: [query={green}{args.query}{white}] {green}{result}{end}")
	    		  if args.output:
	    		  	self.on_result(self,result)
	    		  time.sleep(0.05)
	    		  number += 1
	    		  if number >= int(args.count):
	    		  	break
	    		if args.verbose:
	    			exit(f"{white}* Stopped [seconds={red}{datetime.now()-self.start}{white}]{end}")
	    		break
	    		
	    	except KeyboardInterrupt:
	    	    if args.verbose:
	    	    	exit(f"{white}* Process interrupted [{red}Ctrl{white}+{red}C{white}].{end}")
	    	    break

	    	except Exception as e:
	    	    if args.verbose:
	    	    	print(f"{white}* Error [query={red}{args.query}{white}]: {red}{e}{end}")
	    	    	print(f"{white}* Retrying [query={green}{args.query}{white}]...{end}")

	    
	def on_results(self,result):
		with open(args.output, "a") as file:
			file.write(f"{result}\n")
			file.close()
		if args.verbose:
			print(f"{white}* result(s) written to ./{red}{args.output}{end}")		




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"{red}ox{white}Dork{red}: Google dorking tool developed by {white}Richard Mwewa || {red}https://github.com/rlyonheart{end}")
    parser.add_argument("query", help="search query")
    parser.add_argument("-c","--count",help="number of results to show",dest="count", metavar="NUNBER", default=50)
    parser.add_argument("-o","--outfile",help="output filename",dest="output", metavar="FILENAME")
    parser.add_argument("-v", "--verbose", help="verbosity", dest="verbose", action="store_true")
    args = parser.parse_args()
    if args.verbose:
    	print(banner)
    	print(f"{white}* Fetching dorks [query={green}{args.query}{white}] [dorks_count={red}{args.count}{end}{white}]...{end}")
    oxdork(args).on_connect()
