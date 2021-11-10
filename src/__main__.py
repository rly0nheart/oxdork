#!/usr/bin/env python3

import os
import sys
import random
import argparse
import requests
import subprocess
from datetime import datetime
from googlesearch import search
from lib.headers import user_agents
from lib.colors import red,white,yellow,green,end


class Dork:
	def __init__(self,args):
		self.headers = {"User-Agent": f"{random.choice(user_agents)}"}
		self.google = f"https://www.google.com/search?q={args.query}&hl=en"
		self.api = f"https://api.hackertarget.com/pagelinks/?q={self.google}"
		self.response = requests.get(self.api,headers=self.headers).text
		
	def main(self):
	    if args.lite:
	        print(self.response)
	    elif args.litesh:
	    	subprocess.run(["chmod","+x",f"{os.getcwd()}/src/.__main__.sh"],text=True)
	    	subprocess.run([f"{os.getcwd()}/src/.__main__.sh",f"{args.query}"],text=True)
	    else:
	        self.oxdork()
	        
			    		
	def oxdork(self):
	    print(f"\n{white}{args.query}\n├ Status: fetching {green}{args.count}{white} dorks...")
	    counter = 0
	    number = 0
	    for result in search(args.query, num=int(args.count),start=0,stop=None,lang="en",tld="com", pause=2.5,user_agent=f"{random.choice(user_agents)}"):
	        counter+=1
	        print(f"{white}├─ {counter}: {green}{result}{end}")
	        if args.output:
	        	self.on_result(self,result)
	        number += 1
	        if number >= int(args.count):
	        	break
	        		        	
	    
	def on_results(self,result):
		with open(args.output, "a") as file:
			file.write(f"{result}\n")
			file.close()
			
			
parser = argparse.ArgumentParser(description=f"{green}ox{white}Dork (Google dorking tool) : OXDORK uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers. {green}Developed by{white} Richard Mwewa | {green}https://github.com/{white}rlyonheart{end}")
parser.add_argument("query", help=f"{white}query; {red}Note{white} if query contains spaces, put it inside {green}quote symbols{end}")
parser.add_argument("--lite-shell", help=f"{white}initiate the {green}bash{white} version of {green}--lite{end}",dest="litesh",action="store_true")
parser.add_argument("--lite", help=f"{white}initiate the {green}lite{white} version of oxdork{end}", dest="lite", action="store_true")
parser.add_argument("-c","--count",help=f"{green}number{white} of results to return ({green}default is 50{white}){end}",dest="count", metavar=f"{white}NUMBER{end}", default=50)
parser.add_argument("-o","--output",help=f"{white}write output to a specified {green}file{end}",dest="output", metavar=f"{white}FILENAME{end}")
parser.add_argument("-v", "--verbose", help=f"{white}run oxdork in {green}verbose{white} mode{end}", dest="verbose", action="store_true")
args = parser.parse_args()
