#!/bin/bash

# This is a bash version of the python dork_lite file
# It uses curl to send requests

function 0Xdork(){
	read query
	search="https://www.google.com/search?q=$query"
	curl "https://api.hackertarget.com/pagelinks/?q=$search"

}
0Xdork

