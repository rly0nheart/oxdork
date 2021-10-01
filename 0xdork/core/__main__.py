import sys
import time
import random
import argparse
from tqdm import tqdm
from datetime import datetime
from googlesearch import search
from resources.headers import user_agents
from assets.colors import red,white,yellow,green,end


class Dork:
	def __init__(self):
		self.start = datetime.now()
		
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
	    		  print(f"{white}({green}{args.query}{white}) 0xdork:: ({counter}) {green}{result}{end}")
	    		  time.sleep(0.05)
	    		  number += 1
	    		  if number >= int(args.count):
	    		  	break
	    		  	
	    		sys.exit(f"{yellow}0xdork{white} stopped in {red}{datetime.now()-self.start}{white} seconds.{end}")
	    	except KeyboardInterrupt:
	    		sys.exit()
	    	except Exception as e:
	    		print(f"{white}* Error: {red}{e}{end}")
	    		print(f"{white}* Retrying ({green}{args.query}{white})...{end}")
	    
	    
	def on_results(self,result):
		with open(f"{args.output}", "a") as file:
			file.write(f"{result}\n")
			file.close()
