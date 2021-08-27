# 0xdork

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/0xdork?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/0xdork/badge)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/0xdork)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/0xdork)
![Twitter](https://img.shields.io/twitter/follow/rly0nheart?&style=flat&logo=twitter)


![Screenshot_20210827-111909-removebg-preview](https://user-images.githubusercontent.com/74001397/131107876-db415339-0c1d-4876-8665-fe9b76c4518c.png)

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
> $ git clone https://github.com/rlyonheart/0xdork

> $ cd 0xdork 

> $ pip install -r requirements.txt

# Usage:

> python3 dork [SEARCH QUERY] -C [RESULT COUNT]

**Example** 
> $ python dork inurl:index.php?id=1 -C 10

*Or*
> $ python dork inurl:index.php?id=1 --count 10
  ![Screenshot_20210827-134753](https://user-images.githubusercontent.com/74001397/131123053-4048e715-1e8c-40c7-a4ad-b1ca9c3ccb38.jpg)

**Note**: 
*If your search query contains spaces, you can put your query inside " " symbols.*
  
# Help:
> $ python3 dork -h

*Or*
> $ python3 dork --help
![Screenshot_20210827-133546](https://user-images.githubusercontent.com/74001397/131123277-8e7cb714-4be2-47d5-a926-1931941fd9d5.jpg)


To view the help message. 

# dork_queries.txt:
A collection of some common dork queries here [dorks_queries](https://github.com/rlyonheart/0xdork/blob/master/dork_queries.txt)



  
  # Disclaimer:
  *This is for educational purposes only, the author Richard Mwewa [rly0nheart] will not be responsible for the damages that might be done with this tool.*
  
  

 



