import logging
import requests
import argparse
import urllib.request
from tqdm import tqdm
from datetime import datetime
from googlesearch import search
from lib.colors import red,white,green,reset

class oxdork:
	def __init__(self,args):
		if args.query:
			if args.minimal:
				print(self.minimal())
			else:
				self.dork()
		elif args.update:
			self.update()
		else:
			exit(f"{white}oxdork: use {green}-h{white}/{green}--help{white} to show usage.{reset}")
			
			
	def dork(self):
	   number=0
	   counter=0
	   if args.verbose:
	   	logging.info(f"{white}Fetching [{args.count}] dorks. Please wait...")
	   for results in search(args.query, num=int(args.count),start=0,stop=None,lang="en",tld="com", pause=2.5):
	       number+=1
	       counter+=1
	       logging.debug(f"[{counter}] {green}{results}{reset}")
	       
	       if args.output:
	           self.output(results,counter)
	           
	       if number >= int(args.count):
	       	break
	       	
	   
	def output(self,results,counter):
		with open(args.output, "a") as file:
			file.write(f"[{counter}] {results}\n")
			file.close()
			
		
	def minimal(self):
		google_url = f"https://www.google.com/search?q={args.query}&hl=en"
		api = f"https://api.hackertarget.com/pagelinks?q={google_url}"
		response = requests.get(api).text
		return response
		
	
	def update(self):
		files_to_update = ["src/main.py","lib/banner.py","lib/colors.py","oxdork","dork_queries/dork_queries.txt","LICENSE","README.md","requirements.txt"]
		for file in tqdm(files_to_update,desc=f"{white}Updating {red}ox{white}Dork{reset}"):
			data = urllib.request.urlopen(f"https://raw.githubusercontent.com/rly0nheart/oxdork/master/{file}").read()
			with open(file, "wb") as code:
				code.write(data)
				code.close()
					
		logging.info(f"{white}Update complete. Re-run program.{reset}")
		exit()
		

parser = argparse.ArgumentParser(description=f"{white}Google dorking tool — by Richard Mwewa | https://about.me/rly0nheart{reset}",epilog=f"{red}ox{white}Dork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers.{reset}")
parser.add_argument("-q","--query", help="query",metavar="<query>")
parser.add_argument("-c","--count",help="number of results to show (default is 10){reset}",metavar="<number>", default=10)
parser.add_argument("-o","--output",help="write output to specified file",metavar="<filename>")
parser.add_argument("-m","--minimal",help="enable a minimal alternative of oxdork",action="store_true")
parser.add_argument("-v","--verbose",help="enable verbosity",action="store_true")
parser.add_argument("-u","--update",help="update oxdork",action="store_true")
parser.add_argument("--version",version="2022.2.2.0 Released on 20th March 2022",action="version")
args = 
args = parser.parse_args()

start_time = datetime.now()
logging.basicConfig(format=f"%(asctime)s {white}%(message)s{reset}",datefmt=f"{white}%I{red}:{white}%M{red}:{white}%S%p{reset}",level=logging.DEBUG)
