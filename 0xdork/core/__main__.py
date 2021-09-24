import sys
import time
import logging
import random
import argparse
from tqdm import tqdm
from googlesearch import search
from assets.banner import banner
from resources.headers import user_agents
from assets.colors import red,white,yellow,green,end


logging.basicConfig(format=f"{white}[%(asctime)s] {red}%(message)s{white}"
,datefmt=f"{white}%I{red}:{white}%M{red}:{white}%S%p",level=logging.DEBUG)

print(banner)
class Dork:
	def __init__(self):
		self.start = time.time()
		self.end = time.time()-self.start
		
	def on_connect(self,args):
	    number = 0
	    counter = 0
	    while True:
	    	try:
	    		google_search = search(args.query, num=int(args.count),start=0,stop=None,lang="en",
	    		tld="com", pause=2.5,
	    		user_agent=f"{random.choice(user_agents)}")
	    		for result in tqdm(google_search):
	    		  counter+=1
	    		  if args.output:
	    		  	self.on_results(result)
	    		  logging.info(f"{white}0xdork::: [{counter}] {green}{result}{end}")
	    		  time.sleep(0.05)
	    		  number += 1
	    		  if number >= int(args.count):
	    		  	break
	    		  	
	    		sys.exit(f"{yellow}0xdork{white} stopped in {red}{self.end}{white} seconds.{end}")
	    	except KeyboardInterrupt:
	    		sys.exit()
	    	except Exception as e:
	    		logging.debug(f"{white}Error: {red}{e}{end}")
	    		logging.debug(f"{white}Reconnecting...{end}")
	    
	    
	def on_results(self,result):
		with open(f"{args.output}", "a") as file:
			file.write(f"{result}\n")
			file.close()