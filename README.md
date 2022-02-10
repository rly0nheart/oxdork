![Screenshot_20210827-111909-removebg-preview](https://user-images.githubusercontent.com/74001397/131107876-db415339-0c1d-4876-8665-fe9b76c4518c.png)

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/rly0nheart/oxdork?style=flat&logo=github)
![CodeFactor](https://www.codefactor.io/repository/github/rly0nheart/oxdork/badge?style=flat&logo=codefactor)
[![Downloads](https://static.pepy.tech/personalized-badge/oxdork?period=total&units=international_system&left_color=black&right_color=orange&left_text=pypi+downloads&logo=pypi)](https://pepy.tech/project/oxdork)
![Lines of code](https://img.shields.io/tokei/lines/github/rly0nheart/oxdork?style=flat&logo=github)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/rly0nheart/oxdork?include_prereleases?style=flat&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/oxdork?style=flat&logo=github)

<h4 align="center"><samp> Google hacking, also named Google dorking, is a hacker technique that uses Google Search and other Google applications to find security holes in the configuration and computer code that websites are using. Google dorking could also be used for OSINT (Open Source Intelligence). </samp></h4>
 

<h4 align="center"><samp> oxDork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers. </samp></h4>


# Basic dorks

| Dork         | Usage     | Example |
| ------------- |:---------:|:-------:|
| <code>allintext:</code> | finds all specified terms in the title of a page |  **allintext:passwords** |
| <code>inurl:</code> | finds a specified string in the url of a page     |   **inurl:index.php?id=1** |
| <code>site:</code> |  locks a search on a specified site or domain  |  **site:example.com**  |
| <code>intitle:</code> | finds a specified strings in the title of a page |  **intitle:"your text here"** |
| <code>link:</code> | searches for all links to a specified site or domain | **link:example.com** |
| <code>cache:</code> | returns Google's cached copy of a specified url page  | **cache:www.example.com** |
| <code>info:</code> | returns summary information about a specified url | **info:https://example.com** |



# Installation & Usage
**Clone from Github**:
```
$ git clone https://github.com/rly0nheart/oxdork.git
```

```
$ cd oxdork
```

```
$ pip install -r requirements.txt
```

```
$ python dork -q searchquery
```

**Install from PyPI**:
```
$ pip install oxdork
```

```
$ oxdork -q searchquery
```


# Updating
**Github clone**:
```
$ python oxdork --update
```

**PyPI Package**:
```
pip install --upgrade oxdork
```

# Optional Arguments

| Flag           | MetaVar | Usage |
| ------------- |:----------------------:|:---------:|
| <code>-q/--query</code>    ||  search query |
| <code>-u/--update</code>    ||  update oxdork |
| <code>--minimal</code>    || initiate a lightweight alternative of oxdork |
| <code>-c/--count</code>    | *number* |  number of dork results to return (default is 10) |
| <code>-d/--dump</code>      |   *path/to/file* |  write output to a specified file  |
| <code>-v/--verbose</code>      |    |  enable verbosity (recommended)  |



# Note(s):
> *Use VPN for better experience.*

> *Sending more than 5 requests in less than 5 minutes will return a 429 error code. If this happens you can pass the --minimal argument instead.*

# Queries
A collection of 5,568 common dork queries [here](https://github.com/rly0nheart/oxdork/tree/master/dork_queries)

# About author
* [About.me](https://about.me/rly0nheart)
