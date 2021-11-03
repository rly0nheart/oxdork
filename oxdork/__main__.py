#!/usr/bin/env python3

import sys
import random
import argparse
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
	    		google_search = 
	    		
	    		for result in search(args.query, num=int(args.count),start=0,stop=None,lang="en",tld="com", pause=2.5,user_agent=f"{random.choice(user_agents)}"):
	    		  counter+=1
	    		  print(f"{white}├─ {counter}: {green}{result}{end}")
	    		  if args.output:
	    		  	self.on_result(self,result)
	    		  number += 1
	    		  if number >= int(args.count):
	    		  	break
	    		if args.verbose:
	    			exit(f"{white}└╼ Oxdork stopped in {green}{datetime.now()-start}{white} seconds.{end}")
	    		break
	    		
	    	except KeyboardInterrupt:
	    	    if args.verbose:
	    	    	exit(f"{white}└╼ Oxdork interrupted with {red}Ctrl{white}+{red}C{end}")
	    	    break

	    	except Exception as e:
	    	    if args.verbose:
	    	    	print(f"{white}├ Error: {red}{e}{end}")
	    	    	print(f"{white}├─ Status: {green}Retrying...{end}")

	    
	def on_results(self,result):
		with open(args.output, "a") as file:
			file.write(f"{result}\n")
			file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"{green}ox{white}Dork (Google dorking tool) : OXDORK uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers. {green}Developed by{white} Richard Mwewa | {green}https://github.com/{white}rlyonheart{end}")
    parser.add_argument("query", help=f"{white}query; {red}Note{white} if query contains spaces, put it inside {green}quote symbols{end}")
    parser.add_argument("-c","--count",help=f"{green}number{white} of results to return ({green}default is 50{white}){end}",dest="count", metavar=f"{white}NUMBER{end}", default=50)
    parser.add_argument("-o","--outfile",help=f"{white}write output to a specified {green}file{end}",dest="output", metavar=f"{white}FILENAME{end}")
    parser.add_argument("-v", "--verbose", help=f"{white}run oxdork in {green}verbose{white} mode{end}", dest="verbose", action="store_true")
    args = parser.parse_args()
    if args.verbose:
    	print(f"{white}* Started Oxdork v2021.2.1.6 (https://pypi.org/project/oxdork) at {green}{start}{end}")
    	print(f"\n{white}{args.query}\n├ Status: fetching {green}{args.count}{white} dorks...")
    oxdork(args).on_connect()
