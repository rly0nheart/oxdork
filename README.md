![Screenshot_20210827-111909-removebg-preview](https://user-images.githubusercontent.com/74001397/131107876-db415339-0c1d-4876-8665-fe9b76c4518c.png)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/0xdork?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/0xdork/badge)
![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/rlyonheart/0xdork)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/0xdork)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/rlyonheart/0xdork?include_prereleases)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/0xdork)
![0xdork](images/0xdork.gif)



![IMG_20210922_200225](https://user-images.githubusercontent.com/74001397/134488831-a82c78b4-4dd0-41ad-ac71-e14e53b85f13.jpg)



 𝟎𝐱𝐝𝐨𝐫𝐤 *uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers*.

 # Google dorking:
 Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. Google dorking could also be used for OSINT(Open Source Intelligence).
 
# Basic Google dorks:
| Query         | Usage     | Example |
| ------------- |:---------:|:-------:|
| <code>allintext:</code> | *finds all specified terms in the title of a page* |  **allintext:passwords** |
| <code>inurl:</code> | *finds a specified string in the url of a page*      |   **inurl:index.php?id=1** |
| <code>site:</code> |  *locks a search on a specified site or domain*  |  **site:example.com**  |
| <code>intitle:</code> |  *finds a specified strings in the title of a page* |  **intitle:"your text here"** |
| <code>link:</code> | *searches for all links to a specified site or domain* | **link:example.com** |
| <code>cache:</code> | *returns Google's cached copy of a specified url page* | **cache:www.example.com** |
| <code>info:</code> | *returns summary information about a specified url* | **info:https://example.com** |

# Installation:
**Clone this repo**:
> <code>$ git clone https://github.com/rlyonheart/0xdork.git</code>

> <code>$ cd 0xdork</code>

> <code>$ pip install -r requirements.txt</code>

# Arguments:

| Flag           | Or            |MetaVar|                 Usage|
| ------------- |:-------------:|:----------------------:|:---------:|
| <code>-c</code>           | <code>--count</code>    | **RESULT COUNT** |  *Number of dork results to return (default is 50)* |
| <code>-o</code>      | <code>--outfile</code>      |   **OUTFILE** |  *Output filename with extension*  |
| <code>-h</code> | <code>--help</code>  |  **HELP**  |  *View help message*  |


# Notes:

* *If your search query contains spaces, you can put it inside " " symbols.*

* *When using **dork**; Sending more than 5 requests in less than 5 minutes will return a 429 error code. If you get this error your best bet will be using a VPN to avoid it.*

# dork_lite:
*A lightweight faster version of **dork** with no verbosity. It does not return a 429 error code, neither does it need a VPN.*
![dork_lite](images/rlyonheart-1.gif)

| Flag           | Or            |MetaVar|                 Usage|
| ------------- |:-------------:|:----------------------:|:---------:|
| <code>query</code>           |     | **SEARCH QUERY** |  *search query* |
| <code>-o</code>      | <code>--outfile</code>      |   **OUTFILE** |  *Output filename with extension*  |
| <code>-h</code> | <code>--help</code>  |  **HELP**  |  *View help message*  |

# dork_lite.sh

*A bash version of the python dork_lite*

* *Run* <code>$ bash dork_lite.sh</code>
* *then enter query*
![0xdork_lite](images/0xdork_lite.gif)


# dork_queries/dork_queries.txt:
A collection of 5,568 common dork queries here [Dorks](dork_queries/dork_queries.txt)



  
  # Disclaimer:
  *This is for educational purposes only, and should not be used in environments without legal authorization. Therefore, the author will not be responsible for the damages that might be done with it.*
  
  

 



