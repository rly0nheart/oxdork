import sys
import time
import datetime
import logging
import random
import argparse
from dork import *
from assets.colors import red,white,yellow,end
from tqdm import tqdm
from assets.banner import banner
from googlesearch import search
from resources.headers import user_agents

logging.basicConfig(format=f"{white}[%(asctime)s] {red}%(message)s{white}"
,datefmt=f"{white}%I{red}:{white}%M{red}:{white}%S%p",level=logging.INFO)

print(banner)
class Dork:
	def __init__(self, args):
		self.sec = datetime.datetime.now()
		self.seconds = datetime.datetime.now()-self.sec
		
	def on_connect(self):
	    number = 0
	    counter = 0
	    google_search = search(args.query, num=int(args.count),start=0,stop=None,lang="en",
	    tld="com", pause=2.5,
	    user_agent=f"{random.choice(user_agents)}")
	    for result in tqdm(google_search):
	        counter+=1
	        if args.output:
	        	self.on_results(result)
	        	
	        logging.info(f"{white}0xdork::: [{counter}] {green}{result}{end}")
	        time.sleep(0.5)
	        number += 1
	        if number >= int(args.count):
	        	break
	        	
	    sys.exit(f"{yellow}0xdork{white} stopped in {red}{self.seconds}{white} seconds.{end}")
	    
	    
	def on_results(self,result):
		with open(f"{args.output}", "a") as file:
			file.write(f"{result}\n")
			file.close()
