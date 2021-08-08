# Python Quick Start

#### See the [releases](https://github.com/slow-but-steady/yt-videos-list/releases) page to see new additions/modifications for each release!
#### See this [comparison](https://github.com/slow-but-steady/yt-videos-list/compare/v0.6.0...main) page to see new additions/modifications that will be available in the NEXT release!

<details>
  <summary><b>See sister <a href="https://github.com/slow-but-steady/YouTube-Channels">YouTube-Channels</a> repository for a list of interesting channels!</b></summary></h3>

- The `YouTube-Channels` sister repository is a separate repository that uses this package to create a list of videos uploaded by every channel supported by the repository.
- The sister repository will update the lists of videos once a week.
- NOTE: In order to minimize the size of the sister repo, the repo contains the list of videos in ONLY the `csv` format, and not in `txt` or `md` format.
</details>

<p align="center">
  <a href="https://github.com/slow-but-steady/yt-videos-list/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/slow-but-steady/yt-videos-list?color=yellow&labelColor=black"></a>
  <a href="https://docs.python.org/3/index.html">    <img src="https://img.shields.io/badge/python-3.6%2B-blue?labelColor=black"/></a>
  <a href="https://www.python.org/dev/peps/pep-0008"><img src="https://img.shields.io/badge/code%20style-PEP8-yellow.svg?labelColor=black"/></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/slow-but-steady/yt-videos-list?color=blue&labelColor=black"></a>
  <a href="https://github.com/slow-but-steady/yt-videos-list/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/slow-but-steady/yt-videos-list?color=yellow&labelColor=black"></a>
  <br>
  <a href="https://badge.fury.io/py/yt-videos-list"><img src="https://badge.fury.io/py/yt-videos-list.svg" alt="PyPI version" height="20"></a>
  <br>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/yt-videos-list?labelColor=black&label=PyPI%20-%20Wheel"></a>
  <a href="https://pypi.org/project/yt-videos-list/#files/"><img alt="PyPI - Format" src="https://img.shields.io/pypi/format/yt-videos-list?labelColor=black&label=PyPI%20-%20Format"></a>
  <a href="https://pypi.org/project/yt-videos-list/#history/"><img alt="PyPI - Status" src="https://img.shields.io/pypi/status/yt-videos-list?labelColor=black&label=PyPI%20-%20Status"></a>
  <br>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/yt-videos-list?labelColor=black&label=PyPI%20-%20Implementation"></a>
  <a href="https://pypi.org/project/yt-videos-list/"><img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/yt-videos-list?labelColor=black&label=PyPI%20-%20Python%20Version"></a>
  <br>
  <a href="https://codebeat.co/projects/github-com-slow-but-steady-yt_videos_list-master"><img src="https://codebeat.co/badges/46b103ed-da79-4893-96af-ce95c9149532" alt="codebeat badge"/></a>
</p>

<details>
  <summary><b>Python 3.6+ setup (required if not already installed)</b></summary>

This package uses [f-strings](https://cito.github.io/blog/f-strings/) (more [here](https://realpython.com/python-f-strings/)), and so requires Python 3.6+.

If you have an older version of Python, you can download Python 3.9.1 (follow links below) and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.
- [macOS 64-bit installer](https://www.python.org/ftp/python/3.9.1/python-3.9.1-macosx10.9.pkg)
- [Windows x86-64 executable installer](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)
- [Windows x86 executable installer](https://www.python.org/ftp/python/3.9.1/python-3.9.1.exe)
- [Gzipped source tarball](https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz) (most useful for Linux)
</details>

<details>
  <summary><b>Permissions for first run</b></summary>

  This is required to make sure you can download and install the required Selenium binary dependencies.
  <details>
  <summary><b>On Windows: make sure you open <code>Command Prompt</code> or <code>Powershell</code> (both work) in "Run as Administrator" mode</b></summary>

  - shortcut: <kbd>⊞ Win</kbd> + <kbd>X</kbd> + <kbd>A</kbd>
  </details>
  <details>
    <summary><b>On Unix based machines (MacOS, Linux): make sure you have read and write access to <code>/usr/local/bin/</code></b></summary>

  - if you're not sure, open terminal and run `sudo chown $USER /usr/local/bin/`
  </details>
<br>
</details>

<details>
  <summary><b>Installing the package</b></summary>

After you install Python 3.6+ and ensure you have the required permissions as needed, enter the following in your command line:
```shell
# if something isn't working properly, try rerunning this
# the problem may have been fixed with a newer version

pip3 install -U yt-videos-list     # MacOS/Linux
pip  install -U yt-videos-list     # Windows


# if that doesn't work:

python3 -m pip install -U yt-videos-list     # MacOS/Linux
python  -m pip install -U yt-videos-list     # Windows
```
</details>

<details>
  <summary><b>If you're on Windows: make sure you <i>always</i> open <code>Command Prompt</code> or <code>Powershell</code> (both work) in "Run as Administrator" mode!</b></summary>

  - shortcut: <kbd>⊞ Win</kbd> + <kbd>X</kbd> + <kbd>A</kbd>
  - this allows `yt_videos_list` to update selenium webdriver binaries to be compatible with newer browser versions as browsers are updated (e.g. your Firefox browser updates from version 77 to version 82)
    - to see the commands being run, see the `yt_videos_list/docs/dependencies.json` file
</details>

<details>
  <summary><b>Running the package from the python interpreter</b></summary>

```shell
python3     # MacOS/Linux
python      # Windows
```
```python
from yt_videos_list import ListCreator


my_driver = 'firefox' # SUBSTITUTE DRIVER YOU WANT (options below)
lc = ListCreator(driver=my_driver, scroll_pause_time=0.8)


lc.create_list_for(url='https://www.youtube.com/user/schafer5')
lc.create_list_for(url='https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ', log_silently=True)
# Set `log_silently` to `True` to mute program logging to the console.
# The program will log the prgram status and any program information
# to only the log file for the channel being scraped
# (this is useful when scraping multiple channels at once with multi-threading).
# By default, the program logs to both the log file for the channel being scraped AND the console.


# to name the file using the channel ID instead of the channel name, set file_name='id'
# this is useful when scraping multiple channels with the same name:
lc.create_list_for(url='https://www.youtube.com/channel/UCb2EYjrzI6WpNAmPZeihhag', file_name='id')
lc.create_list_for(url='https://www.youtube.com/channel/UCDzYhlGOvGqsYw8IaTKDT8g', file_name='id')

# for more details about this method:
help(lc.create_list_for)


# see the new files that were just created:
import os
os.system('ls -lt | head')                      # MacOS/Linux
os.system('dir /O-D | find "_videos_list"')     # Windows

# for more information on using the module:
help(lc)
```
- `driver` options include:
  - `'firefox'`
  - `'opera'`
  - `'safari'` (MacOS only)
  - `'chrome'`
  - `'brave'`
  - `'edge'` (Windows only!)
- increase `scroll_pause_time` for laggy internet and decrease `scroll_pause_time` for fast internet
</details>

#### If you already scraped a channel and the channel uploaded a new video, simply rerun this program on that channel and this package updates your files to include the newer video(s)!

<details>
  <summary><b>Scraping multiple channels from a file simultaneously with multi-threading</b></summary>

Add the url to every channel you want to extract information from in a `txt` file with every url placed on a new line.
- example: [`channels.txt`](./channels.txt) (NOTE this is a relative link, so this ***might*** not link properly on non-GitHub hosted sites!)

Enter the python interpreter:

```
python3     # MacOS/Linux
python      # Windows
```
```python
from yt_videos_list import ListCreator

lc = ListCreator(driver='firefox', scroll_pause_time=1.2)
lc.create_list_from(path_to_channel_urls_file='channels.txt', number_of_threads=4)

# configuring settings:
lc.create_list_from(
  path_to_channel_urls_file='channels.txt',
  number_of_threads=4,
  min_sleep=1,
  max_sleep=5,
  after_n_channels_pause_for_s=(20, 10),
  log_subthread_status_silently=False,
  log_subthread_info_silently=False
)                                                                     # defaults (keyword argument form)
lc.create_list_from('channels.txt', 4, 1, 5, (20, 10), False, False)  # defaults (positional argument form)
lc.create_list_from('channels.txt', min_sleep=3, max_sleep=10)        # modifying only min_sleep and max_sleep

help(lc.create_list_from) # see API method details
```
- See [Thread about multi-threading with yt_videos_list](https://github.com/slow-but-steady/yt-videos-list/discussions/11) for more information!

</details>

<details>
  <summary><b>Explicitly downloading all Selenium dependencies</b></summary>

Ideal if you use Selenium for other projects 😎
- Make sure you already have the `yt-videos-list` package installed (follow directions above for getting set up), then run the following:
```shell
pip3 install -U yt-videos-list # MacOS/Linux: ensure latest package
python3                        # MacOS/Linux: enter python interpreter
pip install -U yt-videos-list  # Windows:     ensure latest package
python                         # Windows:     enter python interpreter
```
```python
from yt_videos_list.download import selenium_webdriver_dependencies
selenium_webdriver_dependencies.download_all()
```
That's all! 🤓
</details>

<details>
  <summary><b>More API information</b></summary>

---
**NOTE** that you can also access all the information below from the Python interpreter by entering
```python
import yt_videos_list
help(yt_videos_list)
```

---
```python
# default options for the ListCreator object

ListCreator(
  txt=True,
  csv=True,
  md=True,
  reverse_chronological=True,
  headless=False,
  scroll_pause_time=0.8,
  driver='firefox',
  cookie_consent=False
  )
```
There are a number of optional arguments you can specify during the instantiation of the ListCreator object. The preceding arguments are run by default, but in case you want more flexibility, you can specify the:
- `driver` argument:
  - Firefox (default)
  - Opera
  - Safari (MacOS only)
  - Chrome
  - Brave
  - Edge (Windows only)
    - `driver='firefox'`
    - `driver='opera'`
    - `driver='safari'`
    - `driver='chrome'`
    - `driver='brave'`
    - `driver='edge'`
- `cookie_consent` argument:
  - `False` (default) - block all cookie options if prompted by YouTube (at consent.youtube.com)
  - `True` - accept all cookie options if prompted by YouTube (also at consent.youtube.com)
    - `cookie_consent=False` (default) OR `cookie_consent=True`
- `txt`, `csv`, `md` file type argument:
  - `True` (default) - create a file for the specified type
  - `False` - do not create a file for the specified type
    - `txt=True`  (default) OR `txt=False`
    - `csv=True`  (default) OR `csv=False`
    - ` md=True`  (default) OR ` md=False`
- `file_suffix` argument:
  - `True` (default) - add a file suffix to the output file name
    - `ChannelName_reverse_chronological_videos_list.csv`
    - `ChannelName_chronological_videos_list.csv`
  - `False` - do NOT add a file suffix to the output file name
    - this means if a reverse chronological file and a chronological file is made for the same channel, they will have the same name!
    - `ChannelName.csv` (reverse chronological output file)
    - `ChannelName.csv` (chronological output file)
      -> `file_suffix=True`  (default) OR `file_suffix=False`
- `all_video_data_in_memory` argument:
  - `False` (default) - do not scrape the entire page
  - `True`            - scrape the entire page (must ALSO set the `video_data_returned` attribute to `True` to return this data!)
    - `all_video_data_in_memory=False` (default) OR `all_video_data_in_memory=True`
- `video_data_returned` argument:
  - `False` (default) - do not return video data collected from the current scrape job (return dummy data instead: `[[0, '', '', '']]`)
  - `True` - return video data collected from the current scrape job
    - if `all_video_data_in_memory` attribute set to `False`, the returned data MIGHT not be the full data, and video numbering MIGHT be incorrect
    - set `all_video_data_in_memory` attribute to `True` to return ALL video data for channel (video number will then also ALWAYS be correct)
      - `video_data_returned=False` (default) OR `video_data_returned=True`
- `video_id_only` argument:
  - `False` (default) - include      the full URL             to video: `https://www.youtube.com/watch?v=ElevenChars`
  - `True`            - include only the identifier parameter to video:                                 `ElevenChars`
    - `video_id_only=False` (default) OR `video_id_only=True`
- `reverse_chronological` argument:
  - `True` (default) - write the files in order from most recent video to the oldest video
  - `False` - write the files in order from oldest video to the most recent video
    - `reverse_chronological=True` (default) OR `reverse_chronological=False`
- `headless` argument:
  - `False` (default) - run the driver with an open Selenium instance for viewing
  - `True` - run the driver in "invisible" mode
    - `headless=False` (default) OR `headless=True`
- `scroll_pause_time` argument:
  - any float values greater than `0` (default `0.8`)
    - The value you provide will be how long the program waits before trying to scroll the videos list page down for the channel you want to scrape. For fast internet connections, you may want to reduce the value, and for slow connections you may want to increase the value.
  - `scroll_pause_time=0.8` (default)
  - CAUTION: reducing this value too much will result in the program not capturing all the videos, so be careful! Experiment :)
- `verify_page_bottom_n_times` argument:
  - any int values greater than `0` (defaults to `3`)
  - NOTE: this argument is only used when CREATING a new file for a new channel, and is unused when UPDATING an existing file for an already scraped channel.
  - The value you provide will be how many times the program needs to verify it acually reached the bottom of the page before accepting it is the bottom of the page, and starting to write the information to the output file(s).
  - For channels that have uploaded THOUSANDS of videos, increase this value to a large number that you think should be sufficient to verify the program reached the bottom of the page.
  - To determine HOW large of a value you should provide, determine the length of time you'd like to wait before being reasonably sure that you reached the bottom of the page and it's not just YouTube's server trying to fetch the response from an old database entry, and divide the time you decided to wait by the `scroll_pause_time` argument.
    - For example, if you want to wait 45 seconds and you set the `scrioll_pause_time` value to `1.0`:
      -> `your_time / scroll_pause_time`
      -> `45 / 1.0`
      -> `45`
      -> therefore: `verify_page_bottom_n_times=45`
    - For channels with only a couple hundred videos (or less), the default value of verify_`page_bottom_n_times=3` **should** be sufficient.
  - See commit a68f8f62e5c343cbb0641125e271bb96cc4f0750 for more details.
- `file_buffering` argument:
  - any `int` values greater than `0` (default `-1`, which uses the default OS setting)
  - LEAVE THIS ALONE IF YOU'RE UNSURE!
  - Documentation:
    - https://docs.python.org/3/library/functions.html#open
  - Deep dive:
    - https://stackoverflow.com/questions/3167494/how-often-does-python-flush-to-a-file
    - https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method
      - https://stackoverflow.com/questions/230751/how-can-i-flush-the-output-of-the-print-function
      - https://en.wikipedia.org/wiki/Data_buffer
      - https://stackoverflow.com/questions/1450551/buffered-vs-unbuffered-io
    - https://www.quora.com/What-does-flushing-files-or-Stdin-do-in-Python
    - https://www.quora.com/Whats-the-difference-between-buffered-I-O-and-unbuffered-I-O
    - https://stackoverflow.com/questions/8409050/unix-buffered-vs-unbuffered-i-o
    - https://medium.com/@bramblexu/three-ways-to-close-buffer-for-stdout-stdin-stderr-in-python-8be694bd2737
    - https://www.quora.com/In-C-what-does-buffering-I-O-or-buffered-I-O-mean

</details>

<details>
<summary><b>Cloning and running locally</b></summary>

To clone the repository and install the most updated version of the package that may not yet be available on the latest release through [PyPI](pypi.org/project/yt-videos-list/), run:
```
git clone https://github.com/slow-but-steady/yt-videos-list.git

cd yt_videos_list/python # MacOS/Linux
pip3 install .           # MacOS/Linux
# if that doesn't work:
python3 -m pip install . # MacOS/Linux

cd yt_videos_list\python # Windows
pip install .            # Windows
# if that doesn't work:
python -m pip install .  # Windows
```
To make your own changes to the `yt_videos_list` python package and run the changes locally:
```
# make changes to the codebase in the
# ===> /dev <=== directory
python3 minifier.py           # MacOS/Linux
pip3 install .                # MacOS/Linux

python minifier.py            # Windows
pip install .                 # Windows
```
NOTE that the changes you make to the codebase SHOULD BE MADE in the `yt_videos_list/python/dev` directory!!
  - the code in the `yt_videos_list/python/yt-videos-list` directory is minified with
    - leading indents stipped to the minimum (1 space for each nested scope)
    - whitespace for padding (e.g. extra spaces to align variable assignments) stripped
    - comments stripped
  - as a result, the code in the `yt_videos_list/python/yt-videos-list` directory is NOT human readable, and the `yt_videos_list/python/dev` directory should be used for development instead!
    - the `minifier.py` module performs all the code preprocessing and packages the code from `yt_videos_list/python/dev` into the final version seen in the `yt_videos_list/python/yt-videos-list` directory
    - so running `minifier.py` ***before*** installing the local package with `pip install .` (Windows) or `pip3 install .` is essential!
</details>

<details>
<summary><b>Running tests</b></summary>

The tests use the custom `ThreadWithResult` subclass of `threading.Thread` provided by the `save-thread-result` package, so make sure you install that module using
```
pip3 install -U save-thread-result     # MacOS/Linux
pip  install -U save-thread-result     # Windows

# if that doesn't work:

python3 -m pip install -U save-thread-result     # MacOS/Linux
python  -m pip install -U save-thread-result     # Windows
```

Then, make sure you're in the `yt_videos_list/python` directory, then run:
```
tests\run_tests.bat     # Windows
####       Any shell on   MacOS/Linux
bash tests/run_tests.sh # this works
csh  tests/run_tests.sh # this works
dash tests/run_tests.sh # this works
ksh  tests/run_tests.sh # this also works
tcsh tests/run_tests.sh # this works too
zsh  tests/run_tests.sh # this works as well
# you can try other shells and
# they should work too, since
# there's no special syntax in
# the run_tests.sh file
```
</details>

<details>
<summary><b>Stargazers Over Time</b></summary>

[![Stargazers over time](https://starchart.cc/slow-but-steady/yt-videos-list.svg)](https://starchart.cc/slow-but-steady/yt-videos-list)
</details>

<details>
  <summary><b>Usage Statistics</b></summary>

- [PePy](https://pepy.tech/project/yt-videos-list)
- [PyPi Stats](https://pypistats.org/packages/yt-videos-list)
</details>
<p>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Daily Downloads" src="https://img.shields.io/pypi/dd/yt-videos-list?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29" width="275"></a>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Weekly Downloads" src="https://img.shields.io/pypi/dw/yt-videos-list?labelColor=black&color=yellow&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <a href="https://pypistats.org/packages/yt-videos-list"><img alt="PyPI - Monthly Downloads" src="https://img.shields.io/pypi/dm/yt-videos-list?labelColor=black&color=blue&label=PyPI%20downloads%20%28excludes%20mirrors%29"width="275"></a>
  <br>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Weekly Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=week&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads/week%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Monthly Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=month&units=international_system&left_color=black&right_color=blue&left_text=PePY%20Downloads/month%20%28includes%20mirrors%29" width="275"></a>
  <a href="https://pepy.tech/project/yt-videos-list"><img alt="PePY Total Downloads" src="https://static.pepy.tech/personalized-badge/yt-videos-list?period=total&units=international_system&left_color=black&right_color=yellow&left_text=PePY%20Downloads%20Total%20%28includes%20mirrors%29" width="275"></a>
  <br>
</p>

#### [Back to main page](https://github.com/slow-but-steady/yt-videos-list/)
If you found this interesting or useful, **please consider starring this repo** so other people can more easily find and use this. Thanks!
