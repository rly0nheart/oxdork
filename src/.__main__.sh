#!/bin/bash

# This is a bash version of --lite 
# It uses curl to send requests

query="https://www.google.com/search?q=$1"
curl "https://api.hackertarget.com/pagelinks/?q=$query"
