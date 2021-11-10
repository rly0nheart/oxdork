![Screenshot_20210827-111909-removebg-preview](https://user-images.githubusercontent.com/74001397/131107876-db415339-0c1d-4876-8665-fe9b76c4518c.png)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rlyonheart/oxdork?ystyle=flat)
![CodeFactor](https://www.codefactor.io/repository/github/rlyonheart/oxdork/badge)
[![Downloads](https://static.pepy.tech/personalized-badge/oxdork?period=total&units=international_system&left_color=black&right_color=orange&left_text=pypi+downloads)](https://pepy.tech/project/oxdork)
![Lines of code](https://img.shields.io/tokei/lines/github/rlyonheart/oxdork)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/rlyonheart/oxdork?include_prereleases)
![GitHub repo size](https://img.shields.io/github/repo-size/rlyonheart/oxdork)

<h4 align="center"><samp> Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. Google dorking could also be used for OSINT (Open Source Intelligence). </samp></h4>
 

<h4 align="center"><samp> OXDORK uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers. </samp></h4>


# Basic dorks

| Dork         | Usage     | Example |
| ------------- |:---------:|:-------:|
| <code>allintext:</code> | <h4 align="center"><samp>finds all specified terms in the title of a page</samp></h4> |  **allintext:passwords** |
| <code>inurl:</code> | <h4 align="center"><samp>finds a specified string in the url of a page</samp></h4>      |   **inurl:index.php?id=1** |
| <code>site:</code> |  <h4 align="center"><samp>locks a search on a specified site or domain</samp></h4>  |  **site:example.com**  |
| <code>intitle:</code> |  <h4 align="center"><samp>finds a specified strings in the title of a page</samp></h4> |  **intitle:"your text here"** |
| <code>link:</code> | <h4 align="center"><samp>searches for all links to a specified site or domain</samp></h4> | **link:example.com** |
| <code>cache:</code> | <h4 align="center"><samp>returns Google's cached copy of a specified url page</samp></h4> | **cache:www.example.com** |
| <code>info:</code> | <h4 align="center"><samp>returns summary information about a specified url</samp></h4> | **info:https://example.com** |



# Installation
**Clone from Github**:
```
git clone https://github.com/rlyonheart/oxdork.git
```

```
cd oxdork
```

```
pip install -r requirements.txt
```

**Install from PyPI**:
```
pip install oxdork
```

# Usage
**Github clone**:
```
python oxdork -v query
```

**Or**:
```
chmod +x oxdork
```

```
./oxdork -v query
```

**PyPI Package**:
```
oxdork -v query
```


# Lite Packages
**oxdork lite:python**:
```
python oxdork -v --lite query
```

**oxdork lite:bash**:
```
python oxdork -v --lite-shell query
```

# Optional Arguments

| Flag           | MetaVar | Usage |
| ------------- |:----------------------:|:---------:|
| <code>--lite</code>    ||  <h4 align="center"><samp>initiate the lightweight version of oxdork</samp></h4> |
| <code>--lite-shell</code>    ||  <h4 align="center"><samp>initiate the bash lightweight version of oxdork</samp></h4> |
| <code>-c/--count</code>    | **NUMBER** |  <h4 align="center"><samp>number of dork results to return (default is 50)</samp></h4> |
| <code>-o/--output</code>      |   **FILENAME** |  <h4 align="center"><samp>write output to a file</samp></h4>  |
| <code>-v/--verbose</code>      |    |  <h4 align="center"><samp>run oxdork in verbose mode (recommended)</samp></h4>  |



# Notes:
* *Use VPN for better experience.*

* *If search query contains spaces, it should be put inside quote* **" "** *symbols.*

* *Sending more than 5 requests in less than 5 minutes will return a 429 error code. That is why using a VPN is recommended.*

# Queries
A collection of 5,568 common dork queries [here](https://github.com/rlyonheart/oxdork/tree/master/dork_queries)

# About author
* [About.me](https://about.me/rlyonheart)

# Contact author
* [Github](https://github.com/rlyonheart)

* [Twitter](https://twitter.com/rly0nheart)
