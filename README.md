![Screenshot_20210827-111909-removebg-preview](https://user-images.githubusercontent.com/74001397/131107876-db415339-0c1d-4876-8665-fe9b76c4518c.png)

![Screenshot_2022-03-17_10-25-50](https://user-images.githubusercontent.com/74001397/158896243-8f05629b-5efe-4174-ada8-85569d512e01.png)

oxDork uses Google dorking techniques and Google dorks to find security holes and misconfigurations in web servers.

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=for-the-badge&logo=linux)
![GitHub](https://img.shields.io/github/license/rly0nheart/oxdork?style=for-the-badge&logo=github)
![CodeFactor](https://www.codefactor.io/repository/github/rly0nheart/oxdork/badge?style=for-the-badge&logo=codefactor)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/rly0nheart/oxdork?include_prereleases&style=for-the-badge&logo=github)
![GitHub repo size](https://img.shields.io/github/repo-size/rly0nheart/oxdork?style=for-the-badge&logo=github)

# Installation
```
$ git clone https://github.com/rly0nheart/oxdork.git
```

```
$ cd oxdork
```

```
$ pip install -r requirements.txt
```

# Usage
```
$ python oxdork [query]
```

# Updating
```
$ python oxdork --update
```

# Optional Arguments

| Flag           | MetaVar | Usage |
| ------------- |:----------------------:|:---------:|
| <code>-q/--query</code>    | [query] |  search query |
| <code>-u/--update</code>    ||  update oxdork |
| <code>-m/--minimal</code>    || initiate a minimal alternative of oxdork |
| <code>-c/--count</code>    | *number* |  number of dork results to return (default is 10) |
| <code>-d/--dump</code>      |   *path/to/file* |  write output to a specified file  |
| <code>-v/--verbose</code>      |    |  enable verbosity (recommended)  |

# Note(s):
> *Use VPN for better experience.*

> *Sending more than 5 requests in less than 5 minutes will return a 429 error code. If this happens you can pass the -m/--minimal argument instead.*

# PyPI Package
View package on [PyPI](https://pypi.org/project/oxdork)

# Queries
A collection of 5,568 common dork queries [here](https://github.com/rly0nheart/oxdork/tree/master/dork_queries)

# About author
* [About.me](https://about.me/rly0nheart)
