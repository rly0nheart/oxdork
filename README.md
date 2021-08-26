# 0xdork

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/0xdork?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/0xdork/badge)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/0xdork)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/0xdork)
![Twitter](https://img.shields.io/twitter/follow/rly0nheart?&style=flat&logo=twitter)

![Screenshot_20210826-214404](https://user-images.githubusercontent.com/74001397/131028816-b10318e9-a6a9-4774-a6f6-4f963d9bf673.jpg)

 𝟎𝐱𝐝𝐨𝐫𝐤 *uses Google dorking techniques and Google dorks to find security holes in configurations that websites use*.

 
 # Google dorking
 Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. Google dorking could also be used for OSINT(Open Source Intelligence).
 
 # Basic Google dorks:
> intitle:    [Finds a specified strings in the title of a page]  e.g intitle:"your text"

> allintext:  [Finds all specified terms in the title of a page]  e.g allintext:Passwords

> inurl:      [Finds a specified string in the url o a page]      e.g inurl:index.php?id=1

> site:       [Locks a search to a specified site or domain]      e.g site:example.com

> link:       [Searches for all links to a specified site or url] e.g link:example.com

> cache:      [Displays Google's cached copy of a specified url page] e.g cache:example.com

> info:      [Displays summary information about a specified url]  e.g info:www.example.com

# Installation:
**Clone this repo**:
> git clone https://github.com/rlyonheart/0xdork

> cd 0xdork 

> pip install -r requirements.tx

# Usage:
**Run**:
> python3 dork [SEARCH QUERY] -C [RESULT COUNT]
![InShot_20210607_140317944](https://user-images.githubusercontent.com/74001397/121014591-71055d00-c79a-11eb-9db9-73ac137f67d0.jpg)


**Example** 
> python3 dork inurl:index.php?id=1 -C 10
  
**Or**:

> python3 dork [SEARCH QUERY] --count [RESULT COUNT]

**Example**:
> python3 dork inurl:index.php?id=1 --count 10
  
# Help:
> python3 dork -h
> python3 dork --help

To view the help message. 

# The file dorks.txt:
A collection of some Dorks here [dorks.txt](https://github.com/rlyonheart/0xdork/blob/master/dorks.txt)



  
  # Disclaimer:
  This is for educational purposes only, the author Richard Mwewa [rly0nheart] will not be responsible for the damages that might be done with this tool.
  
  

 



