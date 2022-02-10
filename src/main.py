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
		if args.minimal:
			print(self.minimal())
		elif args.update:
			self.update()
		else:
			self.on_connection()
			
			
	def on_connection(self):
	   number=0
	   counter=0
	   if args.verbose:
	   	logging.info(f"{white}Fetching {args.count} dorks...")
	   for results in search(args.query, num=int(args.count),start=0,stop=None,lang="en",tld="com", pause=2.5):
	       number+=1
	       counter+=1
	       logging.debug(f"[{counter}] {green}{results}{reset}")
	       
	       if args.dump:
	           self.dump(results,counter)
	           
	       if number >= int(args.count):
	       	break
	       	
	   
	def dump(self,results,counter):
		with open(args.dump, "a") as file:
			file.write(f"[{counter}] {results}\n")
			file.close()
			
		
	def minimal(self):
		google_url = f"https://www.google.com/search?q={args.query}&hl=en"
		api = f"https://api.hackertarget.com/pagelinks?q={google_url}"
		response = requests.get(api).text
		return response
		
	
	def update(self):
		files_to_update = ["src/main.py","lib/banner.py","lib/colors.py","dork"]
		for file in tqdm(files_to_update,desc=f"{white}Updating {red}ox{white}Dork{reset}"):
			data = urllib.request.urlopen(f"https://raw.githubusercontent.com/rly0nheart/oxdork/master/{file}").read()
			with open(file, "wb") as code:
				code.write(data)
				code.close()
					
		logging.info(f"{white}Update complete. Re-run program.{reset}")
		exit()
		

parser = argparse.ArgumentParser(description=f"{white}Google dorking tool{reset}",epilog=f"{red}ox{white}Dork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers. Developed by {green}Richard Mwewa{white} | https://about.me/{green}rly0nheart{reset}")
parser.add_argument("-q","--query", help=f"{white}search query{reset}")
parser.add_argument("-c","--count",help=f"{white}number of results to show ({green}default is 10{white}){reset}",metavar=f"{white}number{reset}", default=10)
parser.add_argument("-d","--dump",help=f"{white}dump output to specified file{reset}",metavar=f"{white}path/to/file{reset}")
parser.add_argument("--minimal",help=f"{white}run a minimal version of oxdork{reset}",action="store_true")
parser.add_argument("-v","--verbose",help=f"{white}enable verbosity{reset}",action="store_true")
parser.add_argument("-u","--update",help=f"{white}update oxdork to the most current version{reset}",action="store_true")
args = parser.parse_args()

start_time = datetime.now()
logging.basicConfig(format=f"%(asctime)s {white}%(message)s{reset}",datefmt=f"{white}%I{red}:{white}%M{red}:{white}%S%p{reset}",level=logging.DEBUG)
