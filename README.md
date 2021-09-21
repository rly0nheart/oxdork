# 0xdork

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/0xdork?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/0xdork/badge)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/rlyonheart/0xdork)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/0xdork)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/rlyonheart/0xdork)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/0xdork)


![Screenshot_20210827-111909-removebg-preview](https://user-images.githubusercontent.com/74001397/131107876-db415339-0c1d-4876-8665-fe9b76c4518c.png)
![Screenshot_20210921-211108](https://user-images.githubusercontent.com/74001397/134234528-d838820c-bbfa-4576-946c-4227bff89e01.jpg)


 𝟎𝐱𝐝𝐨𝐫𝐤 *uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers*.

 
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
> <code>$ git clone https://github.com/rlyonheart/0xdork</code>

> <code>$ cd 0xdork</code>

> <code>$ pip install -r requirements.txt</code>

# Arguments

| Flag           | Or            |MetaVar|                 Usage|
| ------------- |:-------------:|:----------------------:|:---------:|
| <code>-c</code>           | <code>--count</code>    | **RESULT COUNT** |  *Number of dork results to return* |
| <code>-o</code>      | <code>--outfile</code>      |   **OUTFILE** |  *Output filename with extension*  |
| <code>-h</code> | <code>--help</code>  |  **HELP**  |  *View help message*  |

>**Note**: 
*If your search query contains spaces, you can put it inside " " symbols.*

> **Important**:
*Sending more than 5 requests in less than 5 minutes will return a 429 error code. If you get this error your best bet will be using a VPN to avoid it.*


# dork_queries.txt:
A collection of some common dork queries here [dorks_queries](https://github.com/rlyonheart/0xdork/blob/master/dork_queries.txt)



  
  # Disclaimer:
  *This is for educational purposes only, and should not be used in environments without legal authorization. Therefore, the author will not be responsible for the damages that might be done with it.*
  
  

 



