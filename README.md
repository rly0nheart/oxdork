# 0XDORK
 𝟎𝐱𝐝𝐨𝐫𝐤 *uses Google dorking techniques and Google dorks to get sensitive information that is not easily available to the average user*.
![0xdork](https://user-images.githubusercontent.com/74001397/121006418-2a5f3500-c791-11eb-81e3-8abd806dc84a.jpg)


 
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

> pip install -r REQUIREMENTS

# Usage:
**Run**:
> python3 dork -Q [QUERY] -C [RESULT COUNT]
![InShot_20210607_140317944](https://user-images.githubusercontent.com/74001397/121014591-71055d00-c79a-11eb-9db9-73ac137f67d0.jpg)


**Example** 
> python3 dork -Q inurl:index.php?id=1 -C 10
  
**Or**:

> python3 dork --query [QUERY] --count [RESULT COUNT]
![InShot_20210607_140449880](https://user-images.githubusercontent.com/74001397/121014948-c93c5f00-c79a-11eb-8b70-7d0d9ed75936.jpg)

**Example**:
> python3 dork --query inurl:index.php?id=1 --count 10
  
# Help:
> python3 dork -h
> python3 dork --help
![InShot_20210607_140613492](https://user-images.githubusercontent.com/74001397/121015529-626b7580-c79b-11eb-9863-04b73ff2cd0a.jpg)
To view the help message. 

# The file dorks.txt:
A collection of some Dorks here [dorks.txt](https://github.com/rlyonheart/0xdork/blob/master/dorks.txt)



  
  # Notice:
  This is for educational purposes only, the author Richard Mwewa [rly0nheart] will not be responsible for the damages that might be done with this tool.
  
  # Contact me:
  Social media:
  * [Twitter](https://twitter.com/rly0nheart/)
  * [Facebook](https://fb.me/rly0nheart/)
  * [Instagram](https://instagram.com/rlyonheart/)
  * [Telegram](https://t.me/rlyonheart/)
