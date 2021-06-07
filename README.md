# 0XDORK
![0xdork](https://user-images.githubusercontent.com/74001397/121006418-2a5f3500-c791-11eb-81e3-8abd806dc84a.jpg)

 𝟎𝐱𝐝𝐨𝐫𝐤 uses Google dorking techniques and Google dorks to get sensitive information that is not easily available to the average user.
 
 # Google dorking
 Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. Google dorking could also be used for OSINT(Open Source Intelligence).
 
 # Basic Google dorks:
 * intitle:    [Finds a specified strings in the title of a page]  e.g intitle:"your text"
 * allintext:  [Finds all specified terms in the title of a page]  e.g allintext:Passwords
 * inurl:      [Finds a specified string in the url o a page]      e.g inurl:index.php?id=1
 * site:       [Locks a search to a specified site or domain]      e.g site:example.com
 * link:       [Searches for all links to a specified site or url] e.g link:example.com
 * cache:      [Displays Google's cached copy of a specified url page] e.g cache:example.com
 *  info:      [Displays summary information about a specified url]  e.g info:www.example.com

# Installation:
Clone this repo:
* git clone https://github.com/rlyonheart/0xdork
* cd 0xdork 
* pip install -r REQUIREMENTS

# Usage:
Run:
* python3 dork -Q [Query] -C [RESULT COUNT] 

  e.g python3 dork -Q info:example.com -C 10
  
Or:
* python3 dork --query [QUERY] --count [RESULT COUNT] 
  e.g python3 dork --query info:example.com --count 10
  
# Help:
* python3 dork -h
* python3 dork --help
  To view the help message
