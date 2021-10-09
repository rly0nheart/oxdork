#!/bin/bash

# This is a bash version of the python oxlite file
# It uses curl to send requests

function oxlite(){
	read -r query
	search="https://www.google.com/search?q=$query"
	curl "https://api.hackertarget.com/pagelinks/?q=$search"

}
oxlite
