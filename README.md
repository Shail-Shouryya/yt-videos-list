# General Overview

#### See the [releases](https://github.com/slow-but-steady/yt-videos-list/releases) page to see new additions/modifications for each release!
#### See this [comparison](https://github.com/slow-but-steady/yt-videos-list/compare/v0.6.0...main) page to see new additions/modifications that will be available in the NEXT release!

<details>
  <summary><b>See sister <a href="https://github.com/slow-but-steady/YouTube-Channels">YouTube-Channels</a> repository for a list of interesting channels!</b></summary></h3>

- The `YouTube-Channels` sister repository is a separate repository that uses this package to create a list of videos uploaded by every channel supported by the repository.
- The sister repository will update the lists of videos once a week.
- NOTE: In order to minimize the size of the sister repo, the repo contains the list of videos in ONLY the `csv` format, and not in `txt` or `md` format.
</details>

<p align="center">
  <a href="https://github.com/slow-but-steady/yt-videos-list/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/slow-but-steady/yt-videos-list?color=yellow&labelColor=black&style=social&logo=github"></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/slow-but-steady/yt-videos-list?color=blue&labelColor=black&style=social&logo=github"></a>
</p>

<p align="center">
  <a href="https://github.com/slow-but-steady/yt-videos-list/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/slow-but-steady/yt-videos-list?color=brightgreen&labelColor=black"></a>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/yt-videos-list?&labelColor=black&label=PyPI"></a>
  <br>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/slow-but-steady/yt-videos-list?color=purple&labelColor=black">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/slow-but-steady/yt-videos-list?color=purple&labelColor=black">
  <img alt="Lines of code" src="https://img.shields.io/tokei/lines/github/slow-but-steady/yt-videos-list?color=purple&labelColor=black">
  <br>
  <a href="https://github.com/slow-but-steady/yt-videos-list/issues"><img alt="GitHub Open Issues" src="https://img.shields.io/github/issues/slow-but-steady/yt-videos-list?color=red&labelColor=black"></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/issues?q=is%3Aissue+is%3Aclosed"><img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/slow-but-steady/yt-videos-list?color=darkgreen&labelColor=black"></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/pulls"><img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/slow-but-steady/yt-videos-list?color=red&labelColor=black"></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/pulls?q=is%3Apr+is%3Aclosed"><img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed/slow-but-steady/yt-videos-list?color=darkgreen&labelColor=black"></a>
</p>

<p align="center">
  <a href="https://github.com/slow-but-steady/yt-videos-list/releases/latest"><img alt="GitHub most recent (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/slow-but-steady/yt-videos-list?color=blueviolet&labelColor=black&label=most%20recent%20release%20date"></a>
  <br>
  <a href="https://github.com/slow-but-steady/yt-videos-list/releases"><img alt="GitHub release (latest SemVer including pre-releases) version" src="https://img.shields.io/github/v/release/slow-but-steady/yt-videos-list?include_prereleases&labelColor=black&label=GitHub%20release%20%28latest%20SemVer%20including%20pre-releases%29&sort=semver"></a>
  <br>
  <a href="http://github.com/slow-but-steady/yt-videos-list/graphs/commit-activity">
    <img alt="GitHub commit activity/week" src="https://img.shields.io/github/commit-activity/w/slow-but-steady/yt-videos-list?color=lightgreen&labelColor=black">
    <img alt="GitHub commit activity/month" src="https://img.shields.io/github/commit-activity/m/slow-but-steady/yt-videos-list?color=lightgreen&labelColor=black">
    <img alt="GitHub commit activity/year" src="https://img.shields.io/github/commit-activity/y/slow-but-steady/yt-videos-list?color=lightgreen&labelColor=black">
  </a>
  <br>
  <a href="https://github.com/slow-but-steady/yt-videos-list/branches"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/slow-but-steady/yt-videos-list?color=pink&labelColor=black"></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/commits/main"><img alt="GitHub last commit to main (branch)" src="https://img.shields.io/github/last-commit/slow-but-steady/yt-videos-list/main?color=pink&labelColor=black&label=last%20commit%20to%20main"></a>
  <img alt="GitHub commits since latest release (by SemVer including pre-releases)" src="https://img.shields.io/github/commits-since/slow-but-steady/yt-videos-list/latest/main?color=pink&labelColor=black&include_prereleases">
</p>

This package provides a quick, simple way to create a list of all videos posted to any YouTube channel by providing just the URL to that channel's videos. Follow the link to the API in the language you want to work in from the ***API guides*** section below.

This program relies on Selenium so it has built-in dependecy setup for all Selenium webdrivers, but you can also explicitly use submodules of this package to **download Selenium webdriver dependencies for your own projects**. This makes it much easier to work with Selenium even if you update your browser constantly! See the [Explicitly downloading all Selenium dependencies](https://github.com/slow-but-steady/yt-videos-list/blob/main/python/README.md#explicitly-downloading-all-selenium-dependencies) for directions.

#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!

# API guides
### [python](./python/README.md)

# Other Information
<details>
  <summary><b>Dependencies</b></summary>

- The first time you run this package the automated downloader should install everything you need, but in case it doesn't, refer to the link below and/or file an [issue here](https://github.com/slow-but-steady/yt-videos-list/issues).
  - Manual Selenium downloads **[here](https://github.com/slow-but-steady/yt-videos-list/blob/main/docs/dependencies_pseudo_json.txt)**
- The Selenium drivers are all pretty similar but differ in subtle ways, so play around with them and see what's different :)

**NOTE** that you also need the corresponding browser installed to properly run the selenium driver.
- To download the most recent version of the browser you want, go to the page for:
  - [Firefox](https://www.mozilla.org/en-US/firefox/new/)
  - [Opera](https://www.opera.com/)
  - [Chrome](https://www.google.com/chrome/)
  - [Brave](https://brave.com/)
  - [Edge](https://www.microsoft.com/edge)
</details>

<details>
  <summary><b>Interesting information about YouTube</b></summary>

There are two types of YouTube channels: one type is a `user` channel and the other is a `channel` channel.
- `/user/` channel type:
  - sentdex: https://www.youtube.com/user/sentdex
  - Disney: https://www.youtube.com/user/disneysshows
  - Marvel: https://www.youtube.com/user/MARVEL
  - Apple: https://www.youtube.com/user/Apple
- `/channel/` channel type:
  - Tasty: https://www.youtube.com/channel/UCJFp8uSYCjXOMnkUyb3CQ3Q
  - Billie Eilish: https://www.youtube.com/channel/UCiGm_E4ZwYSHV3bcW1pnSeQ
  - Gordon Ramsay: https://www.youtube.com/channel/UCIEv3lZ_tNXHzL3ox-_uUGQ
  - PBS Space Time: https://www.youtube.com/channel/UC7_gcs09iThXybpVgjHZ_7g
- `/c/` shorthand channel type (new, human readable URL that (usually) consistently provides just the name of the channel) - for easy comparison, all examples below correspond to the 4 `user/` and 4 `channel/` channel types listed above using this new URL formatting:
  - sentdex: https://www.youtube.com/c/sentdex/
  - Disney: https://www.youtube.com/c/Disney/
  - Marvel: https://www.youtube.com/c/marvel/
  - Apple: https://www.youtube.com/user/Apple/ (looks like Apple isn't using the new formatting yet)
  - Tasty: https://www.youtube.com/c/buzzfeedtasty/
  - Billie Eilish: https://www.youtube.com/c/BillieEilish/
  - Gordon Ramsay: https://www.youtube.com/user/gordonramsay/ (looks like Gordon Ramsay switched to the `user/` format instead of `c/`)
  - PBS Space Time: https://www.youtube.com/c/pbsspacetime/
</details>

<details>
  <summary><b>Future Features</b></summary>

### Main Features
- [X] take url and scrape the video name and url for every video for that user
- [X] create [txt](https://fileinfo.com/extension/txt), [csv](https://en.wikipedia.org/wiki/Comma-separated_values), [md](https://en.wikipedia.org/wiki/Markdown) files

### Additional Features
- [x] enable custom name for output file
- [x] update previously created file with new videos uploaded since file creation
  - [x] put all urls from file in a (hash) set and check to see if any urls on page (next time program runs on same page) are missing from the (hash) set
- [ ] create web interface
  - [ ] input box for channel url
  - [ ] generate static HTML page with video URLs for output

</details>

<details>
  <summary><b>Technical Specifications</b></summary>

This python3 package supports multi-platform, mutli-driver use and is currently under active development.

Currently supported operating systems include MacOS, Linux32, Linux64, Windows32, and Windows64. Currently supported drivers include Firefox, Opera, Safari (MacOS), Chrome, Brave, and Edge (Windows).

This package provides built-in support for common errors and exceptions, along with helpful hints, including
  - checking to see if the file to be created already exists
  - checking to see if the user explicitly specified a driver to use, and in case they didn't specify a driver, running the program using Firefox as default and showing the user the available driver options in the terminal output
    - explicitly specifying driver using
      - `ListCreator(driver='firefox')`
      - `ListCreator(driver='opera')`
      - `ListCreator(driver='safari')`
      - `ListCreator(driver='chrome')`
      - `ListCreator(driver='brave')`
      - `ListCreator(driver='edge')`
  - running the program in headless mode if using the geckodriver (Firefox) or chromedriver
    - `ListCreator(headless=True)`
  - checking to see if the user has the correct Selenium dependency installed
    - installs and shows the user the commands they can run to install the correct dependency if the user has an incorrect dependency (or hasn't downloaded the dependency at all)
      - program checks the operating system of the user's machine and returns a `curl` command piped into a `tar` command to download the correct dependecy into a directory the program can access without having to add the executable to PATH manually
      - user still needs to pick the correct command to run by following the directions (if autoamted download doesn't complete)
  - checking to see if the result of the scraping returns anything, and prompts the user to verify the `url` argument if nothing is found

### Overview of package structure
#### `__init__.py`

#### `__main__.py`

#### `script.py`

#### `execute.py`

#### `program.py`

#### `file` submodule

#### `download` submodule

#### `notifications.py`



</details>

<details>
<summary><b>Stargazers Over Time</b></summary>

[![Stargazers over time](https://starchart.cc/slow-but-steady/yt-videos-list.svg)](https://starchart.cc/slow-but-steady/yt-videos-list)
</details>

<details>
  <summary><b>Usage Statistics</b></summary>

- [PePy](https://pepy.tech/project/yt-videos-list)
- [PyPi Stats](https://pypistats.org/packages/yt-videos-list)
<p>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Daily Downloads" src="https://img.shields.io/pypi/dd/yt-videos-list?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29" width="275"></a>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Weekly Downloads" src="https://img.shields.io/pypi/dw/yt-videos-list?labelColor=black&color=yellow&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Monthly Downloads" src="https://img.shields.io/pypi/dm/yt-videos-list?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <br>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Weekly Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=week&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads/week%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Monthly Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=month&units=international_system&left_color=black&right_color=blue&left_text=PePY%20Downloads/month%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Total Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=total&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads%20Total%20%28includes%20mirrors%29" width="275"></a>
  <br>
  <img alt="GitHub release (latest by SemVer including pre-releases) downloads" src="https://img.shields.io/github/downloads-pre/slow-but-steady/yt-videos-list/latest/total?labelColor=black&label=GitHub%20release%20%28latest%20by%20SemVer%20including%20pre-releases%29%20downloads%40latest">
</p>
</details>

If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thanks!
